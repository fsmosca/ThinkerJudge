# ThinkerJudge
Evaluation of moves from World Championship Games. [Analysis data](https://github.com/fsmosca/ThinkerJudge/blob/main/docs/human_eval.csv) can be found in the docs folder.

### Average error in centipawn comparison

![error](https://i.imgur.com/ODKUR5q.png)

### Features
#### Calsen-Anand 2013

```
Event: WCh 2013
Date: 2013.11.22
A. Average error in centipawn (low is better)
+-----------+-----------+---------+-----------------+
|   GameNum |   Carlsen |   Anand |   Carlsen_score |
|-----------+-----------+---------+-----------------|
|         1 |      -1.8 |    10.4 |             0.5 |
|         2 |       3.3 |     2.9 |             0.5 |
|         3 |       6.1 |     5.4 |             0.5 |
|         4 |       5   |     8.1 |             0.5 |
|         5 |       0.9 |    12.3 |             1   |
|         6 |       1.5 |     9.9 |             1   |
|         7 |       1.6 |     2.6 |             0.5 |
|         8 |       0.2 |     0.8 |             0.5 |
|         9 |      11.1 |    16.6 |             1   |
|        10 |       9.7 |     9.9 |             0.5 |
+-----------+-----------+---------+-----------------+

B. Overall average error in centipawn (low is better)
+-----------+---------+
|   Carlsen |   Anand |
|-----------+---------|
|       3.8 |     7.9 |
+-----------+---------+

C. Move Number with 50 to 100 cp error from a playable position (-50/50) cp, (high or None is better)
+-----------+-----------+---------+-----------------+
|   GameNum | Carlsen   | Anand   |   Carlsen_score |
|-----------+-----------+---------+-----------------|
|         1 | None      | None    |             0.5 |
|         2 | None      | None    |             0.5 |
|         3 | 26        | None    |             0.5 |
|         4 | None      | 18      |             0.5 |
|         5 | None      | 45      |             1   |
|         6 | None      | None    |             1   |
|         7 | None      | None    |             0.5 |
|         8 | None      | None    |             0.5 |
|         9 | 22        | 18      |             1   |
|        10 | None      | 26      |             0.5 |
+-----------+-----------+---------+-----------------+

D. Move Number with 101 to 300 cp error from a playable position (-50/50) cp, (high or None is better)
+-----------+-----------+---------+-----------------+
|   GameNum | Carlsen   | Anand   |   Carlsen_score |
|-----------+-----------+---------+-----------------|
|         1 | None      | None    |             0.5 |
|         2 | None      | None    |             0.5 |
|         3 | None      | None    |             0.5 |
|         4 | None      | 28      |             0.5 |
|         5 | None      | None    |             1   |
|         6 | None      | None    |             1   |
|         7 | None      | None    |             0.5 |
|         8 | None      | None    |             0.5 |
|         9 | 18        | None    |             1   |
|        10 | None      | None    |             0.5 |
+-----------+-----------+---------+-----------------+

E. Move Number with 301 to 500 cp error from a playable position (-50/50) cp, (high or None is better)
+-----------+-----------+---------+-----------------+
|   GameNum | Carlsen   | Anand   |   Carlsen_score |
|-----------+-----------+---------+-----------------|
|         1 | None      | None    |             0.5 |
|         2 | None      | None    |             0.5 |
|         3 | None      | None    |             0.5 |
|         4 | None      | None    |             0.5 |
|         5 | None      | None    |             1   |
|         6 | None      | 60      |             1   |
|         7 | None      | None    |             0.5 |
|         8 | None      | None    |             0.5 |
|         9 | None      | None    |             1   |
|        10 | None      | None    |             0.5 |
+-----------+-----------+---------+-----------------+

F. Rating according to Stockfish 13 dev NNUE
+-----------+-----------+---------+
|   GameNum |   Carlsen |   Anand |
|-----------+-----------+---------|
|         1 |      2902 |    2879 |
|         2 |      2880 |    2887 |
|         3 |      2792 |    2769 |
|         4 |      2783 |    2713 |
|         5 |      2887 |    2679 |
|         6 |      2837 |    2671 |
|         7 |      2885 |    2853 |
|         8 |      2898 |    2892 |
|         9 |      2802 |    2785 |
|        10 |      2677 |    2652 |
+-----------+-----------+---------+
```
