# ThinkerJudge
Evaluation of moves from World Championship Games. [Analysis data](https://github.com/fsmosca/ThinkerJudge/blob/main/docs/human_eval.csv) can be found in the docs folder. Games in [pgn files](https://github.com/fsmosca/ThinkerJudge/tree/main/docs/pgn) are in the docs folder as well.

Moves are evaluated by Stockfish 13 dev 2020-12-14 NNUE at 5s/position on 4 threads with i7-2600K processor. Calculation of errors starts at move 12 and it is ended once the score of the game move and engine move are more than 500cp or less than -500cp.

### A. Average error in centipawn comparison

![error](https://i.imgur.com/ODKUR5q.png)

### B. Features

#### Fischer-Spassky 1972
```
Event: World Championship 28th
Date: 1972.??.??
A. Average error in centipawn (low is better)
+-----------+-----------+-----------+-----------------+
|   GameNum |   Fischer |   Spassky |   Fischer_score |
+===========+===========+===========+=================+
|         1 |       8.7 |       0.7 |             0   |
+-----------+-----------+-----------+-----------------+
|         3 |       9.5 |      29.3 |             1   |
+-----------+-----------+-----------+-----------------+
|         4 |      16.2 |      13.4 |             0.5 |
+-----------+-----------+-----------+-----------------+
|         5 |       0.1 |       3.6 |             1   |
+-----------+-----------+-----------+-----------------+
|         6 |       7.8 |      25.5 |             1   |
+-----------+-----------+-----------+-----------------+
|         7 |      25.4 |      23.3 |             0.5 |
+-----------+-----------+-----------+-----------------+
|         8 |       6.1 |      23.8 |             1   |
+-----------+-----------+-----------+-----------------+
|         9 |       0.2 |       6.7 |             0.5 |
+-----------+-----------+-----------+-----------------+
|        10 |      13.7 |      25.1 |             1   |
+-----------+-----------+-----------+-----------------+
|        11 |      51   |       5.7 |             0   |
+-----------+-----------+-----------+-----------------+
|        12 |       3.8 |       2.6 |             0.5 |
+-----------+-----------+-----------+-----------------+
|        13 |      18.3 |      20.7 |             1   |
+-----------+-----------+-----------+-----------------+
|        14 |      13.8 |      12.1 |             0.5 |
+-----------+-----------+-----------+-----------------+
|        15 |      16.9 |      23.8 |             0.5 |
+-----------+-----------+-----------+-----------------+
|        16 |       2.2 |       1.2 |             0.5 |
+-----------+-----------+-----------+-----------------+
|        17 |       1.9 |       3.1 |             0.5 |
+-----------+-----------+-----------+-----------------+
|        18 |      26.1 |      21.2 |             0.5 |
+-----------+-----------+-----------+-----------------+
|        19 |       3.4 |      10.8 |             0.5 |
+-----------+-----------+-----------+-----------------+
|        20 |       5.7 |       2.7 |             0.5 |
+-----------+-----------+-----------+-----------------+
|        21 |       4.2 |      15.2 |             1   |
+-----------+-----------+-----------+-----------------+

B. Overall average error in centipawn (low is better)
+-----------+-----------+
|   Fischer |   Spassky |
+===========+===========+
|      11.8 |      13.5 |
+-----------+-----------+

C. Move Number with 50 to 100 cp error from a playable position (-50/50) cp, (high or None is better)
+-----------+-----------+-----------+-----------------+
|   GameNum | Fischer   | Spassky   |   Fischer_score |
+===========+===========+===========+=================+
|         1 | 29        | None      |             0   |
+-----------+-----------+-----------+-----------------+
|         3 | 14        | 18        |             1   |
+-----------+-----------+-----------+-----------------+
|         4 | None      | None      |             0.5 |
+-----------+-----------+-----------+-----------------+
|         5 | None      | None      |             1   |
+-----------+-----------+-----------+-----------------+
|         6 | None      | 20        |             1   |
+-----------+-----------+-----------+-----------------+
|         7 | None      | None      |             0.5 |
+-----------+-----------+-----------+-----------------+
|         8 | None      | 15        |             1   |
+-----------+-----------+-----------+-----------------+
|         9 | None      | None      |             0.5 |
+-----------+-----------+-----------+-----------------+
|        10 | None      | 16        |             1   |
+-----------+-----------+-----------+-----------------+
|        11 | 15        | 14        |             0   |
+-----------+-----------+-----------+-----------------+
|        12 | 35        | None      |             0.5 |
+-----------+-----------+-----------+-----------------+
|        13 | None      | 60        |             1   |
+-----------+-----------+-----------+-----------------+
|        14 | 21        | None      |             0.5 |
+-----------+-----------+-----------+-----------------+
|        15 | 15        | None      |             0.5 |
+-----------+-----------+-----------+-----------------+
|        16 | None      | None      |             0.5 |
+-----------+-----------+-----------+-----------------+
|        17 | None      | None      |             0.5 |
+-----------+-----------+-----------+-----------------+
|        18 | None      | 27        |             0.5 |
+-----------+-----------+-----------+-----------------+
|        19 | None      | None      |             0.5 |
+-----------+-----------+-----------+-----------------+
|        20 | 34        | None      |             0.5 |
+-----------+-----------+-----------+-----------------+
|        21 | None      | None      |             1   |
+-----------+-----------+-----------+-----------------+

D. Move Number with 101 to 300 cp error from a playable position (-50/50) cp, (high or None is better)
+-----------+-----------+-----------+-----------------+
|   GameNum | Fischer   | Spassky   |   Fischer_score |
+===========+===========+===========+=================+
|         1 | None      | None      |             0   |
+-----------+-----------+-----------+-----------------+
|         3 | None      | None      |             1   |
+-----------+-----------+-----------+-----------------+
|         4 | 19        | None      |             0.5 |
+-----------+-----------+-----------+-----------------+
|         5 | None      | None      |             1   |
+-----------+-----------+-----------+-----------------+
|         6 | None      | None      |             1   |
+-----------+-----------+-----------+-----------------+
|         7 | None      | 12        |             0.5 |
+-----------+-----------+-----------+-----------------+
|         8 | None      | None      |             1   |
+-----------+-----------+-----------+-----------------+
|         9 | None      | None      |             0.5 |
+-----------+-----------+-----------+-----------------+
|        10 | None      | 38        |             1   |
+-----------+-----------+-----------+-----------------+
|        11 | None      | None      |             0   |
+-----------+-----------+-----------+-----------------+
|        12 | None      | None      |             0.5 |
+-----------+-----------+-----------+-----------------+
|        13 | None      | 23        |             1   |
+-----------+-----------+-----------+-----------------+
|        14 | 20        | None      |             0.5 |
+-----------+-----------+-----------+-----------------+
|        15 | 12        | None      |             0.5 |
+-----------+-----------+-----------+-----------------+
|        16 | None      | None      |             0.5 |
+-----------+-----------+-----------+-----------------+
|        17 | None      | None      |             0.5 |
+-----------+-----------+-----------+-----------------+
|        18 | None      | 18        |             0.5 |
+-----------+-----------+-----------+-----------------+
|        19 | None      | None      |             0.5 |
+-----------+-----------+-----------+-----------------+
|        20 | None      | None      |             0.5 |
+-----------+-----------+-----------+-----------------+
|        21 | None      | 34        |             1   |
+-----------+-----------+-----------+-----------------+

E. Move Number with 301 to 500 cp error from a playable position (-50/50) cp, (high or None is better)
+-----------+-----------+-----------+-----------------+
|   GameNum | Fischer   | Spassky   |   Fischer_score |
+===========+===========+===========+=================+
|         1 | None      | None      |             0   |
+-----------+-----------+-----------+-----------------+
|         3 | None      | None      |             1   |
+-----------+-----------+-----------+-----------------+
|         4 | None      | None      |             0.5 |
+-----------+-----------+-----------+-----------------+
|         5 | None      | None      |             1   |
+-----------+-----------+-----------+-----------------+
|         6 | None      | None      |             1   |
+-----------+-----------+-----------+-----------------+
|         7 | None      | None      |             0.5 |
+-----------+-----------+-----------+-----------------+
|         8 | None      | None      |             1   |
+-----------+-----------+-----------+-----------------+
|         9 | None      | None      |             0.5 |
+-----------+-----------+-----------+-----------------+
|        10 | None      | None      |             1   |
+-----------+-----------+-----------+-----------------+
|        11 | None      | None      |             0   |
+-----------+-----------+-----------+-----------------+
|        12 | None      | None      |             0.5 |
+-----------+-----------+-----------+-----------------+
|        13 | None      | None      |             1   |
+-----------+-----------+-----------+-----------------+
|        14 | None      | None      |             0.5 |
+-----------+-----------+-----------+-----------------+
|        15 | None      | 31        |             0.5 |
+-----------+-----------+-----------+-----------------+
|        16 | None      | None      |             0.5 |
+-----------+-----------+-----------+-----------------+
|        17 | None      | None      |             0.5 |
+-----------+-----------+-----------+-----------------+
|        18 | None      | None      |             0.5 |
+-----------+-----------+-----------+-----------------+
|        19 | None      | None      |             0.5 |
+-----------+-----------+-----------+-----------------+
|        20 | None      | None      |             0.5 |
+-----------+-----------+-----------+-----------------+
|        21 | None      | None      |             1   |
+-----------+-----------+-----------+-----------------+

F. Rating according to Stockfish 13 dev NNUE
+-----------+-----------+-----------+
|   GameNum |   Fischer |   Spassky |
+===========+===========+===========+
|         1 |      2753 |      2859 |
+-----------+-----------+-----------+
|         3 |      2769 |      2527 |
+-----------+-----------+-----------+
|         4 |      2642 |      2703 |
+-----------+-----------+-----------+
|         5 |      2879 |      2861 |
+-----------+-----------+-----------+
|         6 |      2833 |      2712 |
+-----------+-----------+-----------+
|         7 |      2490 |      2474 |
+-----------+-----------+-----------+
|         8 |      2821 |      2678 |
+-----------+-----------+-----------+
|         9 |      2851 |      2825 |
+-----------+-----------+-----------+
|        10 |      2694 |      2522 |
+-----------+-----------+-----------+
|        11 |      2678 |      2870 |
+-----------+-----------+-----------+
|        12 |      2828 |      2860 |
+-----------+-----------+-----------+
|        13 |      2444 |      2358 |
+-----------+-----------+-----------+
|        14 |      2717 |      2742 |
+-----------+-----------+-----------+
|        15 |      2694 |      2624 |
+-----------+-----------+-----------+
|        16 |      2852 |      2843 |
+-----------+-----------+-----------+
|        17 |      2872 |      2846 |
+-----------+-----------+-----------+
|        18 |      2476 |      2579 |
+-----------+-----------+-----------+
|        19 |      2850 |      2764 |
+-----------+-----------+-----------+
|        20 |      2767 |      2812 |
+-----------+-----------+-----------+
|        21 |      2839 |      2670 |
+-----------+-----------+-----------+
```

#### Calsen-Anand 2013

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

F. Rating according to Stockfish 13 dev NNUE
+-----------+-----------+---------+
|   GameNum |   Carlsen |   Anand |
+===========+===========+=========+
|         1 |      2902 |    2879 |
+-----------+-----------+---------+
|         2 |      2880 |    2887 |
+-----------+-----------+---------+
|         3 |      2792 |    2769 |
+-----------+-----------+---------+
|         4 |      2783 |    2713 |
+-----------+-----------+---------+
|         5 |      2887 |    2679 |
+-----------+-----------+---------+
|         6 |      2837 |    2671 |
+-----------+-----------+---------+
|         7 |      2885 |    2853 |
+-----------+-----------+---------+
|         8 |      2898 |    2892 |
+-----------+-----------+---------+
|         9 |      2802 |    2785 |
+-----------+-----------+---------+
|        10 |      2677 |    2652 |
+-----------+-----------+---------+
```

### C. References
* [Guid and Bratko 2006](https://ailab.si/matej/doc/Computer_Analysis_of_World_Chess_Champions.pdf)

### D. Credits
* [PGN Mentor](https://www.pgnmentor.com/files.html)
* [Stockfish](https://stockfishchess.org/)
