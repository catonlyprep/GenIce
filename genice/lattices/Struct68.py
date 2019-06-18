# coding: utf-8
"""
Data source:
[C14,Struct68] Dutour Sikirić, Mathieu, Olaf Delgado-Friedrichs, and Michel Deza. “Space Fullerenes: a Computer Search for New Frank-Kasper Structures” Acta Crystallographica Section A Foundations of Crystallography 66.Pt 5 (2010): 602–615.
[sV] Jeffrey, G A. “Hydrate Inclusion Compounds.” Inclusion Compounds 1 (1984): 135–190.

Cage composition:
 (12,14,15,16) = (8,0,0,4,)
"""

pairs="""
13 17
21 16
7 22
44 33
32 38
38 34
19 67
24 4
21 39
65 49
59 17
44 36
28 14
20 26
6 9
42 37
7 17
49 56
50 57
11 15
16 11
26 31
38 55
50 37
29 61
52 12
59 35
32 41
5 55
8 24
65 14
0 62
58 34
61 57
23 65
61 63
44 51
29 45
13 66
3 15
28 66
41 25
59 57
34 25
48 5
28 67
48 16
12 66
59 33
41 4
18 20
20 19
54 30
41 14
0 49
30 34
37 22
50 36
23 61
28 0
7 8
62 24
42 27
48 10
56 27
4 1
19 48
8 66
63 3
9 21
7 60
16 43
2 15
60 4
19 12
51 46
46 63
30 12
50 56
33 1
40 64
29 33
55 39
22 35
62 27
54 43
29 60
40 11
9 40
56 17
6 47
2 47
52 24
45 22
67 32
20 38
51 35
18 58
54 15
30 5
0 1
36 40
45 6
67 43
23 51
42 14
32 53
58 43
62 58
18 52
2 64
35 47
57 64
23 37
54 53
39 3
10 47
13 25
18 21
8 42
46 11
31 63
46 10
13 1
31 64
27 25
39 53
6 3
44 49
26 10
26 9
65 60
52 53
2 5
31 55
36 45
"""

waters="""
0.45594 0.54406 0.625
0.33333 0.66667 0.67149
0.54406 0.08812 0.125
0.91189 0.45594 0.125
0.08811 0.54406 0.625
0.46072 0.92145 0.25
0.95594 0.29405 0.0625
0.78928 0.21072 0.75
0.87261 0.12739 0.64102
0.12739 0.25478 0.14102
0.74522 0.87261 0.14102
0.54406 0.45595 0.125
0.70595 0.04406 0.4375
0.45595 0.91189 0.625
0.87261 0.74522 0.64102
0.66667 0.33333 0.17149
0.46073 0.53928 0.25
0.53928 0.07855 0.75
0.12739 0.25478 0.35899
0.74522 0.87261 0.35899
0.0 0.0 0.3125
0.21072 0.42145 0.25
0.87261 0.12739 0.85899
0.87261 0.74522 0.85899
0.04406 0.33811 0.5625
0.29406 0.95595 0.5625
0.0 0.0 0.1875
0.25478 0.12739 0.64102
0.66189 0.70595 0.5625
0.08812 0.54406 0.875
0.54406 0.08812 0.375
0.12739 0.87261 0.14102
0.95594 0.66189 0.4375
0.33334 0.66667 0.82852
0.33811 0.04406 0.4375
0.66189 0.95594 0.9375
0.29406 0.33811 0.9375
0.0 0.0 0.8125
0.12739 0.87261 0.35899
0.07855 0.53928 0.25
0.33811 0.29406 0.0625
0.04406 0.70595 0.5625
0.0 0.0 0.6875
0.54406 0.45595 0.375
0.45594 0.54406 0.875
0.04406 0.33811 0.9375
0.70595 0.66189 0.0625
0.70595 0.04406 0.0625
0.57856 0.78928 0.25
0.53928 0.46072 0.75
0.25478 0.12739 0.85899
0.66189 0.70595 0.9375
0.95595 0.29406 0.4375
0.91189 0.45594 0.375
0.66667 0.33333 0.32852
0.21073 0.78928 0.25
0.42145 0.21072 0.75
0.29405 0.95594 0.9375
0.33811 0.29406 0.4375
0.45595 0.91189 0.875
0.92145 0.46072 0.75
0.04406 0.70595 0.9375
0.29405 0.33811 0.5625
0.95594 0.66189 0.0625
0.33811 0.04406 0.0625
0.78928 0.57856 0.75
0.66189 0.95594 0.5625
0.70595 0.66189 0.4375
"""

coord= "relative"

cages="""
12 0.0 -1.0 0.5
12 -0.17622 -0.35245 0.25
16 -0.66667 -0.33333 -0.56406
12 0.35245 0.17623 0.25
16 -0.33333 -0.66667 0.56406
12 0.0 1.0 0.0
12 0.17623 -0.17622 0.75
12 -0.17623 0.17622 0.25
16 0.66667 0.33333 -0.06406
12 -0.35245 -0.17623 0.75
16 0.33333 0.66667 0.06406
12 0.17623 0.35245 -0.25
"""

bondlen = 3


cell = """
13.46100100093214 0.0 0.0
-6.730500500466066 11.657568827174991 0.0
1.352010066258678e-15 2.341750127104594e-15 22.08
"""

density = 0.5866191722917903



from genice.cell import cellvectors
cell = cellvectors(a=13.46100100093214,
                   b=13.46100100093214,
                   c=22.08,
                   C=119.99999999999999)
