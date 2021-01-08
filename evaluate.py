#!/usr/bin/env python


"""
Read games in pgn file and save its analysis.

Setup:
  Install python 3.8 or newer

requirements:
  pip install -r requirements.txt
"""


__version__ = 'v1.2.0'
__author__ = 'fsmosca'
__script_name__ = 'Chess Positions Evaluator'
__goal__ = 'Read games in pgn file and save its analysis.'


import argparse
import time
import logging
import ast
from pathlib import Path

import chess.pgn
import chess.engine


logging.basicConfig(level=logging.DEBUG, filename='evaluate.log',
                    filemode='w')


class GameAnalyzer:
    def __init__(self, engine_file, engine_options, output_eval_file,
                 input_pgn, output_pgn, depth=1000, movetime_ms=60000,
                 min_move=1, max_move=1000):
        self.engine_file = engine_file
        self.engine_options = engine_options
        self.output_eval_file = output_eval_file
        self.input_pgn = input_pgn

        if output_pgn is None:
            output_file = Path(self.input_pgn).name

            # Save the output in the folder where evaluate.py is located.
            self.output_pgn = f'out_{output_file}'
        else:
            self.output_pgn = output_pgn

        self.depth = depth
        self.movetime_ms = movetime_ms
        self.min_move = min_move
        self.max_move = max_move

    @staticmethod
    def piece_count(board):
        """
        Total count of pieces and pawns including the king.
        """
        return len(board.piece_map())

    def set_engine_options(self, engine):
        """
        Set engine options like threads, hash etc.

        Command line examples:
        --engine-options "{'Threads': 2}" or
        --engine-options "{'Threads': 2, 'Hash': 256}" or
        --engine-options "{'Threads': 2, 'Hash': 256, 'SyzygyPath': 'F:/Chess/EGTB/syzygy_3456'}"
        """
        if self.engine_options is not None:
            options = ast.literal_eval(self.engine_options)
            for k, v in options.items():
                engine.configure({k: v})

    def annotate(self, game, gcnt):
        """
        Analyze game and save the game analysis in pgn file and position
        evaluations in csv file.
        """
        ev = game.headers['Event']
        da = game.headers['Date']

        rd = game.headers['Round']
        if rd == '?':
            rd = gcnt

        wp = game.headers['White'].split(',')[0]
        bp = game.headers['Black'].split(',')[0]
        res = game.headers['Result']

        # Start engine.
        engine = chess.engine.SimpleEngine.popen_uci(self.engine_file)
        self.set_engine_options(engine)

        # Save the analyzed game.
        my_game = chess.pgn.Game()
        my_node = my_game

        # Copy header.
        for k, v in game.headers.items():
            my_game.headers[k] = v

        # Add annotator tag.
        my_game.headers['Annotator'] = engine.id['name']

        # Parse the game.
        for node in game.mainline():
            game_move = node.move
            board_after_move = node.board()
            parent_node = node.parent
            board = parent_node.board()
            fmvn = board.fullmove_number
            stm = 'white' if board.turn else 'black'

            # Respect minimum move number option.
            if fmvn < self.min_move:
                my_node = my_node.add_main_variation(game_move)
                continue

            if fmvn > self.max_move:
                my_node = my_node.add_main_variation(game_move)

                # Continue writing the game move but do not analyze.
                continue

            num_pcs = GameAnalyzer.piece_count(board)

            # If depth is reached first then the analysis will be stopped.
            # However if movetime is reached first analysis will be stopped.
            # depth default: 1000, movetime_ms default: 60000 or 60sec
            limit = chess.engine.Limit(depth=self.depth, time=self.movetime_ms/1000)

            # Evaluate this board position with the engine.
            engine_info = engine.analyse(board, limit=limit, multipv=1)
            engine_score = engine_info[0]['score'].relative.score(mate_score=32000)
            engine_pv = engine_info[0]['pv'][0:1]
            engine_move = engine_info[0]['pv'][0]
            engine_depth = engine_info[0]['depth']

            my_comment = f'{engine_score / 100:0.2f}/{engine_depth}'
            my_node.add_line(engine_pv, comment=my_comment)

            game_over = board_after_move.is_game_over(claim_draw=False)

            # Evaluate the position after making the move on the board,
            # negate the score and save it.
            if not game_over:
                if engine_move == game_move:
                    move_score = engine_score
                    move_depth = engine_depth
                else:
                    move_info = engine.analyse(board_after_move, limit=limit, multipv=1)
                    move_score = -move_info[0]['score'].relative.score(mate_score=32000)
                    move_depth = move_info[0]['depth']
            else:
                if board_after_move.is_checkmate():
                    move_score = -31999  # The side to move is mated.
                    move_depth = 245  # stockfish max depth, this info will be saved in analysis file.
                else:
                    # Most probably a draw by repetition, fifty-move,
                    # insufficient mating material and stalemate.
                    move_score = 0
                    move_depth = 245

            move_comment = f'{move_score / 100:0.2f}/{move_depth}'

            err = engine_score - move_score
            with open(self.output_eval_file, 'a') as w:
                w.write(
                    f'{ev};{da};{rd};{wp};{bp};{fmvn};{board.epd()};{stm};{num_pcs};{game_move};{engine_move};{move_score};{engine_score};{err};{engine_depth};{res}\n')

            my_node = my_node.add_main_variation(
                game_move, comment=move_comment)

        engine.quit()

        # Write the game into a file in append mode.
        with open(self.output_pgn, 'a') as w:
            w.write(f'{my_game}\n\n')

    def parse_games(self):
        start_time = time.perf_counter()

        game_cnt = 0

        with open(self.input_pgn) as pgn:
            while True:
                game = chess.pgn.read_game(pgn)
                if game is None:
                    break

                game_cnt += 1

                # Show progress in console.
                print(f'game: {game_cnt}')

                self.annotate(game, game_cnt)

        print(f'Elapse (sec): {time.perf_counter() - start_time:0.3f}')


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        prog='%s %s' % (__script_name__, __version__),
        description=__goal__,
        epilog='%(prog)s')
    parser.add_argument('--input-pgn', required=True, type=str,
                        help='Input pgn filename (required).')
    parser.add_argument('--output-pgn', required=False, type=str,
                        help='Output filename (not required), default is out_<input_pgn>.')
    parser.add_argument('--engine-file', required=True, type=str,
                        help='Input engine filename (required). Example:\n'
                             '--engine-file "c:/chess/engines/stockfish/sf12.exe"')
    parser.add_argument('--movetime-ms', required=False, type=int,
                        help='Input engine analysis time in milliseconds or ms (not required), default=60000 or 60sec.',
                        default=60000)
    parser.add_argument('--depth', required=False, type=int,
                        help='Input engine analysis depth (not required), default=1000.',
                        default=1000)
    parser.add_argument('--min-move', required=False, type=int,
                        help='The minimum move number to start the analysis (not required), default=1.',
                        default=1)
    parser.add_argument('--max-move', required=False, type=int,
                        help='The maximum move number to end the analysis (not required), default=1000.',
                        default=1000)
    parser.add_argument('--engine-options', required=False,
                        help='Input engine options (not required), engine default options will be used. Example:\n'
                             '--engine-options "{\'Threads\': 2, \'Hash\': 128}" or\n'
                             '--engine-options "{\'Threads\': 2, \'SyzygyPath\': \'F:/Chess/EGTB/syzygy_3456\'}" or\n'
                             '--engine-options "{\'Backend\': \'cudnn-fp16\'}"')
    parser.add_argument('--output-eval-file', required=False, type=str,
                        help='The file in csv format where the analysis will be saved (not required), default=human_eval.csv.',
                        default='human_eval.csv')
    parser.add_argument('-v', '--version', action='version',
                        version=f'{__version__}')

    args = parser.parse_args()

    a = GameAnalyzer(args.engine_file, args.engine_options,
                     args.output_eval_file, args.input_pgn,
                     args.output_pgn, depth=args.depth,
                     movetime_ms=args.movetime_ms, min_move=args.min_move,
                     max_move=args.max_move)

    a.parse_games()


if __name__ == "__main__":
    main()
