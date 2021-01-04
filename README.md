# ThinkerJudge
Moves from World Championship Games are analyzed using Stockfish engine. [Analysis data](https://github.com/fsmosca/ThinkerJudge/blob/main/docs/human_eval.csv) and games in [pgn files](https://github.com/fsmosca/ThinkerJudge/tree/main/docs/pgn) can be found in docs folder.

Moves are evaluated by Stockfish 13 dev 2020-12-14 NNUE at 5s/position on 4 threads with i7-2600K processor. Calculation of errors starts at move 12 and it is ended once the score of the game move and engine move are more than 500cp or less than -500cp.

You can use evaluate.py using different engine and analysis conditions to analyze the games and use stats.py to generate stats from the resulting analysis.

### Setup
* Install python 3.8 or later
* Download this [repository](https://github.com/fsmosca/ThinkerJudge/archive/main.zip)
* Install dependency
  * pip install -r requirements.txt
  
### Command line
##### 1. Analyze the positions in the game on the pgn file.  
```
python evaluate.py --input-pgn ./docs/pgn/WorldChamp1972.pgn --engine-file stockfish_12 --engine-options "{'Threads': 2, 'Hash': 256, 'SyzygyPath': 'F:/Chess/EGTB/syzygy_3456'}" --movetime-ms 5000`
```

The analyzed games will be saved in `out_WorldChamp1972.pgn` and the analyzed positions will be saved in `human_eval.csv` which can be used to generate average errors of players. You can download [Stockfish](https://stockfishchess.org/) and [Lc0](https://github.com/LeelaChessZero/lc0) engine and use them for analysis.

See the [help page](https://github.com/fsmosca/ThinkerJudge/wiki/Help) for more command line options.

##### 2. Generate stats
This will generate plot in png format and save stats to stats.txt. Head to head average error per game are also saved in csv format.  
`python stats.py >stats.txt`

### A. Average error in centipawn comparison

![error](https://i.imgur.com/ODKUR5q.png)

### B. Features
Fully [generated stats](https://github.com/fsmosca/ThinkerJudge/blob/main/docs/stats.txt) can be found in docs folder.

#### Carlsen-Anand
```
Event: WCh 2013
Date: 2013.11.22
A. Average error in centipawn (low is better)
+-----------+-----------+---------+-----------------+
|   GameNum |   Carlsen |   Anand |   Carlsen_score |
+===========+===========+=========+=================+
|         1 |      -1.8 |    10.4 |             0.5 |
+-----------+-----------+---------+-----------------+
|         2 |       3.3 |     2.9 |             0.5 |
+-----------+-----------+---------+-----------------+
|         3 |       6.1 |     5.4 |             0.5 |
+-----------+-----------+---------+-----------------+
|         4 |       5   |     8.1 |             0.5 |
+-----------+-----------+---------+-----------------+
|         5 |       0.9 |    12.3 |             1   |
+-----------+-----------+---------+-----------------+
|         6 |       1.5 |     9.9 |             1   |
+-----------+-----------+---------+-----------------+
|         7 |       1.6 |     2.6 |             0.5 |
+-----------+-----------+---------+-----------------+
|         8 |       0.2 |     0.8 |             0.5 |
+-----------+-----------+---------+-----------------+
|         9 |      11.1 |    16.6 |             1   |
+-----------+-----------+---------+-----------------+
|        10 |       9.7 |     9.9 |             0.5 |
+-----------+-----------+---------+-----------------+

B. Overall average error in centipawn (low is better)
+-----------+---------+
|   Carlsen |   Anand |
+===========+=========+
|       3.8 |     7.9 |
+-----------+---------+

C. Move Number with 50 to 100 cp error from a playable position (-50/50) cp, (high or None is better)
+-----------+-----------+---------+-----------------+
|   GameNum | Carlsen   | Anand   |   Carlsen_score |
+===========+===========+=========+=================+
|         1 | None      | None    |             0.5 |
+-----------+-----------+---------+-----------------+
|         2 | None      | None    |             0.5 |
+-----------+-----------+---------+-----------------+
|         3 | 26        | None    |             0.5 |
+-----------+-----------+---------+-----------------+
|         4 | None      | 18      |             0.5 |
+-----------+-----------+---------+-----------------+
|         5 | None      | 45      |             1   |
+-----------+-----------+---------+-----------------+
|         6 | None      | None    |             1   |
+-----------+-----------+---------+-----------------+
|         7 | None      | None    |             0.5 |
+-----------+-----------+---------+-----------------+
|         8 | None      | None    |             0.5 |
+-----------+-----------+---------+-----------------+
|         9 | 22        | 18      |             1   |
+-----------+-----------+---------+-----------------+
|        10 | None      | 26      |             0.5 |
+-----------+-----------+---------+-----------------+

D. Move Number with 101 to 300 cp error from a playable position (-50/50) cp, (high or None is better)
+-----------+-----------+---------+-----------------+
|   GameNum | Carlsen   | Anand   |   Carlsen_score |
+===========+===========+=========+=================+
|         1 | None      | None    |             0.5 |
+-----------+-----------+---------+-----------------+
|         2 | None      | None    |             0.5 |
+-----------+-----------+---------+-----------------+
|         3 | None      | None    |             0.5 |
+-----------+-----------+---------+-----------------+
|         4 | None      | 28      |             0.5 |
+-----------+-----------+---------+-----------------+
|         5 | None      | None    |             1   |
+-----------+-----------+---------+-----------------+
|         6 | None      | None    |             1   |
+-----------+-----------+---------+-----------------+
|         7 | None      | None    |             0.5 |
+-----------+-----------+---------+-----------------+
|         8 | None      | None    |             0.5 |
+-----------+-----------+---------+-----------------+
|         9 | 18        | None    |             1   |
+-----------+-----------+---------+-----------------+
|        10 | None      | None    |             0.5 |
+-----------+-----------+---------+-----------------+

E. Move Number with 301 to 500 cp error from a playable position (-50/50) cp, (high or None is better)
+-----------+-----------+---------+-----------------+
|   GameNum | Carlsen   | Anand   |   Carlsen_score |
+===========+===========+=========+=================+
|         1 | None      | None    |             0.5 |
+-----------+-----------+---------+-----------------+
|         2 | None      | None    |             0.5 |
+-----------+-----------+---------+-----------------+
|         3 | None      | None    |             0.5 |
+-----------+-----------+---------+-----------------+
|         4 | None      | None    |             0.5 |
+-----------+-----------+---------+-----------------+
|         5 | None      | None    |             1   |
+-----------+-----------+---------+-----------------+
|         6 | None      | 60      |             1   |
+-----------+-----------+---------+-----------------+
|         7 | None      | None    |             0.5 |
+-----------+-----------+---------+-----------------+
|         8 | None      | None    |             0.5 |
+-----------+-----------+---------+-----------------+
|         9 | None      | None    |             1   |
+-----------+-----------+---------+-----------------+
|        10 | None      | None    |             0.5 |
+-----------+-----------+---------+-----------------+
```

### C. References
* [Guid and Bratko 2006](https://ailab.si/matej/doc/Computer_Analysis_of_World_Chess_Champions.pdf)

### D. Credits
* [PGN Mentor](https://www.pgnmentor.com/files.html)
* [Stockfish](https://stockfishchess.org/)
* [Python Chess](https://github.com/niklasf/python-chess)
