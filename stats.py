#!/usr/bin/env python


"""
Generate stats based on analysis data.


Setup:
  Install python 3.8 or newer
"""


__version__ = 'v1.1.0'
__author__ = 'fsmosca'
__script_name__ = 'stats'
__goal__ = 'Generate stats based on analysis data.'


from pathlib import Path
import argparse

import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt


def game_info(fn):
    """
    Count number of games and get names of players in the pgn file.
    """
    cnt, wp, bp, is_player_recorded = 0, None, None, False

    with open(fn) as f:
        for lines in f:
            line = lines.strip()
            if '[Result ' in line:
                cnt += 1

            if not is_player_recorded:
                if '[White ' in line:
                    wp = line.split('"')[1]
                    wp = wp.split(',')[0]
                elif '[Black ' in lines:
                    bp = line.split('"')[1]
                    bp = bp.split(',')[0]
                    is_player_recorded = True

    return wp, bp, cnt


def update_data(names, errors, years, name1, name2, error1, error2, year):
    """
    Update data for table generation and plots.
    """
    names.append(name1)
    names.append(name2)
    errors.append(error1)
    errors.append(error2)
    years.append(year)
    years.append(year)

    return names, errors, years


def get_error(eval_fn, game_cnt, player_name1,
              player_name2, max_score=200, start_move_num=12):
    event, date = None, None

    playable_score = 50
    first_error_min, first_error_max = 50, 100
    second_error_min, second_error_max = 101, 300
    third_error_min, third_error_max = 301, 500

    names = [player_name1, player_name2]

    df = pd.read_csv(eval_fn, sep=';', engine='python', header=None)
    df.columns = ['Event', 'Date', 'Round', 'White', 'Black', 'MoveNum',
                  'EPD', 'STM', 'Pcs', 'gMove', 'eMove', 'gScore',
                  'eScore', 'Error', 'Depth', 'Result']

    # Calculate the engine's analysis average depth at op, mid and end phases.
    df_average_depth = df[df['Pcs'] >= 28]
    mean_depth_op = df_average_depth['Depth'].mean()

    df_average_depth = df[(df['Pcs'] <= 27) & (df['Pcs'] >= 9)]
    mean_depth_mid = df_average_depth['Depth'].mean()

    df_average_depth = df[df['Pcs'] <= 8]
    mean_depth_end = df_average_depth['Depth'].mean()

    # Add Score column for the generated table.
    df.loc[df['Result'] == '1/2-1/2', 'Score'] = 0.5
    df.loc[((df['STM'] == 'white') & (df['Result'] == '1-0')), 'Score'] = 1.0
    df.loc[((df['STM'] == 'white') & (df['Result'] == '0-1')), 'Score'] = 0.0
    df.loc[((df['STM'] == 'black') & (df['Result'] == '1-0')), 'Score'] = 0.0
    df.loc[((df['STM'] == 'black') & (df['Result'] == '0-1')), 'Score'] = 1.0

    # Record average error.
    average_error = {names[0]: [], names[1]: [], f'{names[0]}_score': []}
    movenum_first_error = {names[0]: [], names[1]: [], f'{names[0]}_score': []}
    movenum_second_error = {names[0]: [], names[1]: [], f'{names[0]}_score': []}
    movenum_third_error = {names[0]: [], names[1]: [], f'{names[0]}_score': []}

    # Loop thru the player names.
    for num, name in enumerate(names):
        opp_name = names[1] if num == 0 else names[0]

        # Loop thru the rounds and games.
        for i in range(1, game_cnt + 1):
            dfr = df[df['Round'] == i]

            if dfr['White'].str.contains(name).any() and dfr['Black'].str.contains(opp_name).any():
                df2 = dfr.loc[(dfr['White'] == name) & (dfr['STM'] == 'white') & (dfr['Black'] == opp_name)]
                all_mean = round(df2.loc[(abs(df2['gScore']) <= max_score)
                                         & (abs(df2['eScore']) <= max_score)
                                         & (abs(df2['MoveNum']) >= start_move_num), 'Error'].mean(), 1)
                average_error[name].append(all_mean)

                # If first player
                if num == 0:
                    sc = df2['Score'].iloc[0]
                    average_error[f'{names[0]}_score'].append(sc)
                    movenum_first_error[f'{names[0]}_score'].append(sc)
                    movenum_second_error[f'{names[0]}_score'].append(sc)
                    movenum_third_error[f'{names[0]}_score'].append(sc)

                    event = df2['Event'].iloc[0]
                    date = df2['Date'].iloc[0]

                # White player, first error
                df_first_error = df2[(df2['Error'] >= first_error_min) & (
                    df2['Error'] <= first_error_max) & (
                    df2['eScore'] >= -playable_score) & (
                    df2['eScore'] <= playable_score) & (df2['MoveNum'] >= start_move_num)]

                error_move = 'None'
                if df_first_error.empty:
                    pass
                else:
                    try:
                        error_move = df_first_error['MoveNum'].iloc[0]
                    except IndexError:
                        pass
                movenum_first_error[name].append(error_move)

                # White player, second error
                df_second_error = df2[(df2['Error'] >= second_error_min) & (
                    df2['Error'] <= second_error_max) & (
                    df2['eScore'] >= -playable_score) & (
                    df2['eScore'] <= playable_score) & (df2['MoveNum'] >= start_move_num)]

                error_move = 'None'
                if df_second_error.empty:
                    pass
                else:
                    try:
                        error_move = df_second_error['MoveNum'].iloc[0]
                    except IndexError:
                        pass
                movenum_second_error[name].append(error_move)

                # White player, third error
                df_third_error = df2[(df2['Error'] >= third_error_min) & (
                    df2['Error'] <= third_error_max) & (
                    df2['eScore'] >= -playable_score) & (
                    df2['eScore'] <= playable_score) & (df2['MoveNum'] >= start_move_num)]

                error_move = 'None'
                if df_third_error.empty:
                    pass
                else:
                    try:
                        error_move = df_third_error['MoveNum'].iloc[0]
                    except IndexError:
                        pass
                movenum_third_error[name].append(error_move)

            # Black player
            elif dfr['Black'].str.contains(name).any() and dfr['White'].str.contains(opp_name).any():
                df2 = dfr.loc[(dfr['Black'] == name) & (dfr['STM'] == 'black') & (dfr['White'] == opp_name)]
                all_mean = round(df2.loc[(abs(df2['gScore']) <= max_score) & (
                    abs(df2['eScore']) <= max_score) & (
                    abs(df2['MoveNum']) >= start_move_num), 'Error'].mean(), 1)
                average_error[name].append(all_mean)

                if num == 0:
                    sc = df2['Score'].iloc[0]
                    average_error[f'{names[0]}_score'].append(sc)
                    movenum_first_error[f'{names[0]}_score'].append(sc)
                    movenum_second_error[f'{names[0]}_score'].append(sc)
                    movenum_third_error[f'{names[0]}_score'].append(sc)

                # Black player, first error
                df_first_error = df2[(df2['Error'] >= first_error_min) & (
                    df2['Error'] <= first_error_max) & (
                    df2['eScore'] >= -playable_score) & (
                    df2['eScore'] <= playable_score) & (df2['MoveNum'] >= start_move_num)]

                error_move = 'None'
                if df_first_error.empty:
                    pass
                else:
                    try:
                        error_move = df_first_error['MoveNum'].iloc[0]
                    except IndexError:
                        pass
                movenum_first_error[name].append(error_move)

                # Black player, second error
                df_second_error = df2[(df2['Error'] >= second_error_min) & (
                    df2['Error'] <= second_error_max) & (
                    df2['eScore'] >= -playable_score) & (
                    df2['eScore'] <= playable_score) & (df2['MoveNum'] >= start_move_num)]

                error_move = 'None'
                if df_second_error.empty:
                    pass
                else:
                    try:
                        error_move = df_second_error['MoveNum'].iloc[0]
                    except IndexError:
                        pass
                movenum_second_error[name].append(error_move)

                # Black player, third error
                df_third_error = df2[(df2['Error'] >= third_error_min) & (
                    df2['Error'] <= third_error_max) & (
                    df2['eScore'] >= -playable_score) & (
                    df2['eScore'] <= playable_score) & (df2['MoveNum'] >= start_move_num)]

                error_move = 'None'
                if df_third_error.empty:
                    pass
                else:
                    try:
                        error_move = df_third_error['MoveNum'].iloc[0]
                    except IndexError:
                        pass
                movenum_third_error[name].append(error_move)

    print(f'Event: {event}')
    print(f'Date: {date}')
    print('A. Average error in centipawn (low is better)')
    error_per_game = pd.DataFrame.from_dict(average_error)

    # Skip game 2 if player is Fischer.
    if player_name1 == 'Fischer' or player_name2 == 'Fischer':
        new_col = [i for i in range(1, game_cnt + 1) if i != 2]
    else:
        new_col = [i for i in range(1, game_cnt + 1)]
    error_per_game.insert(loc=0, column='GameNum', value=new_col)

    print(tabulate(error_per_game, headers='keys', tablefmt='grid', showindex=False))
    print()
    year_played = date.split(".")[0]
    error_per_game.to_csv(f'average_error_cp_{player_name1}_vs_{player_name2}_{year_played}.csv', index=False)

    print('B. Overall average error in centipawn (low is better)')
    means = {names[0]: 0, names[1]: 0}
    means.update({names[0]: round(error_per_game[names[0]].mean(), 1)})
    means.update({names[1]: round(error_per_game[names[1]].mean(), 1)})
    overall_mean = pd.DataFrame(means, index=[0])
    print(tabulate(overall_mean, headers='keys', tablefmt='grid', showindex=False))
    print()

    print(f'C. Move Number with {first_error_min} to {first_error_max} '
          f'cp error from a playable position ({-playable_score}/{playable_score}) cp, '
          '(high or None is better)')
    movenum_error_per_game = pd.DataFrame.from_dict(movenum_first_error)

    if player_name1 == 'Fischer' or player_name2 == 'Fischer':
        new_col = [i for i in range(1, game_cnt + 1) if i != 2]
    else:
        new_col = [i for i in range(1, game_cnt + 1)]

    movenum_error_per_game.insert(loc=0, column='GameNum', value=new_col)

    print(tabulate(movenum_error_per_game, headers='keys', tablefmt='grid', showindex=False))
    print()

    print(f'D. Move Number with {second_error_min} to {second_error_max} '
          f'cp error from a playable position ({-playable_score}/{playable_score}) cp, '
          '(high or None is better)')
    movenum_error_per_game = pd.DataFrame.from_dict(movenum_second_error)

    if player_name1 == 'Fischer' or player_name2 == 'Fischer':
        new_col = [i for i in range(1, game_cnt + 1) if i != 2]
    else:
        new_col = [i for i in range(1, game_cnt + 1)]

    movenum_error_per_game.insert(loc=0, column='GameNum', value=new_col)

    print(tabulate(movenum_error_per_game, headers='keys', tablefmt='grid', showindex=False))
    print()

    print(f'E. Move Number with {third_error_min} to {third_error_max} '
          f'cp error from a playable position ({-playable_score}/{playable_score}) cp, '
          '(high or None is better)')
    movenum_error_per_game = pd.DataFrame.from_dict(movenum_third_error)

    if player_name1 == 'Fischer' or player_name2 == 'Fischer':
        new_col = [i for i in range(1, game_cnt + 1) if i != 2]
    else:
        new_col = [i for i in range(1, game_cnt + 1)]

    movenum_error_per_game.insert(loc=0, column='GameNum', value=new_col)

    print(tabulate(movenum_error_per_game, headers='keys',
                   tablefmt='grid', showindex=False))
    print()

    return round(error_per_game[names[0]].mean(), 1),\
           round(error_per_game[names[1]].mean(), 1),\
           date.split('.')[0],\
           mean_depth_op, mean_depth_mid, mean_depth_end


def plot(df, opph, midph, endph, fn='mean_cp_error.png'):
    """
    Plot average error.
    """
    df.sort_values('CpError', inplace=True, ascending=True)

    fig, ax = plt.subplots(figsize=(6, 4))

    name = df['name']
    cperror = df['CpError']
    year = df['year']
    bar_width = 0.6
    colors = [f'C{i}' for i in range(len(name))]

    name = [f'{n} {y}' for n, y in zip(name, year)]

    text_right_margin = 1.0
    ax.barh(name, cperror, bar_width, left=text_right_margin, align='center', color=colors)
    for i, v in enumerate(cperror):
        ax.text(v, i + 0.10, str(v), color='black', fontweight='bold', fontsize=6)

    ax.tick_params(labelsize=6)

    ax.invert_yaxis()
    ax.set_xlabel('Average Error in centipawn', fontsize=6)
    fig.suptitle("Evaluation of Moves from World Championship Games", fontsize=8)
    ax.set_title('by Stockfish 13 dev 2020-12-14 NNUE, '
                 f'average_depth[ope: {opph:0.0f}, '
                 f'mid: {midph:0.0f}, end: {endph:0.0f}]', fontsize=6)
    plt.savefig(fn, dpi=300, bbox_inches='tight')


def main():
    parser = argparse.ArgumentParser(
        prog='%s %s' % (__script_name__, __version__),
        description=__goal__, epilog='%(prog)s')
    parser.add_argument('--pgn-folder', required=True,
                        help='Input folder location of pgn files (required).')
    parser.add_argument('--analysis-file', required=True,
                        help='Input filename or path and filename of the analysis file (required).')
    parser.add_argument('--evaluation-start-move', required=False, default=12, type=int,
                        help='Input move number to start calculating the stats, default=12.')

    args = parser.parse_args()

    max_score = 500  # score to stop error calculation +/-max_score
    start_move = args.evaluation_start_move
    analysisfn = args.analysis_file  # './docs/human_eval.csv'

    pgn_files = Path(args.pgn_folder).glob('**/*.pgn')
    game_files = [f for f in pgn_files]

    names, errors, years = [], [], []

    # Get player data for table and plot generations.
    for file in game_files:
        name1, name2, games = game_info(file)

        # 1. Get data from analysis file.
        error1, error2, year, opph, midph, endph = get_error(
            analysisfn, games, name1, name2, max_score=max_score,
            start_move_num=start_move)

        # 2. Update data for table and plot generations.
        names, errors, years = update_data(
            names, errors, years, name1, name2, error1, error2, year)

    # Print average error table and plot.
    data = {'name': names, 'CpError': errors, 'year': years}
    df = pd.DataFrame(data)
    df.sort_values('CpError', inplace=True, ascending=True)

    # Print average errors table.
    print('Overall Player Average Centipawn Error')
    print(tabulate(df, headers='keys',
                   tablefmt='grid', showindex=False))

    # Plot the average error in centipawn
    plot(df, opph, midph, endph, fn='mean_cp_error.png')


if __name__ == "__main__":
    main()
