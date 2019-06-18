# coding: utf-8
"""
Data source: Dutour Sikirić, Mathieu, Olaf Delgado-Friedrichs, and Michel Deza. “Space Fullerenes: a Computer Search for New Frank-Kasper Structures” Acta Crystallographica Section A Foundations of Crystallography 66.Pt 5 (2010): 602–615.

Cage composition:
 (12,14,15,16) = (14,4,4,4,)
"""

pairs="""
5 77
135 53
21 92
43 4
136 98
28 82
28 59
89 58
131 142
67 1
59 37
34 139
18 115
14 113
66 50
143 104
35 27
115 140
85 49
5 7
18 4
89 82
136 88
36 29
145 41
105 0
140 93
101 13
99 75
109 76
5 97
11 38
131 26
12 39
0 55
38 129
134 146
137 118
62 72
81 9
102 117
126 123
88 14
25 22
105 117
44 112
29 144
106 69
88 51
80 122
139 36
126 109
30 86
56 14
23 131
77 11
102 48
32 7
90 8
67 79
27 130
125 147
40 14
33 90
59 79
143 56
61 80
128 7
106 95
94 107
137 17
15 43
45 87
129 9
68 147
50 88
39 99
128 90
130 91
2 17
105 123
19 40
20 40
83 106
3 138
64 119
3 137
2 138
115 24
70 129
69 130
134 112
15 101
89 120
145 107
30 100
100 98
37 95
13 50
117 109
10 146
96 55
56 98
118 76
54 56
121 96
26 47
36 41
139 67
48 58
83 92
33 60
12 147
44 124
105 57
140 43
121 6
6 120
74 128
126 46
62 24
30 101
103 143
114 27
52 96
102 130
32 33
136 101
46 53
140 72
83 91
21 17
92 81
19 71
73 45
77 121
132 29
33 111
110 37
71 73
51 42
122 13
63 93
135 124
84 131
77 23
94 70
111 98
66 57
102 133
119 138
63 15
31 45
46 113
97 83
103 61
13 65
58 41
89 107
31 15
93 8
108 124
34 44
12 52
145 26
85 11
78 16
136 4
78 63
119 125
127 118
138 121
127 87
32 23
95 21
18 111
82 99
71 75
97 132
103 113
116 86
80 66
87 72
145 141
139 74
18 86
110 69
76 133
3 52
115 90
84 79
85 60
73 27
104 146
85 97
135 93
110 82
1 144
25 51
42 123
84 104
60 100
95 1
7 21
134 144
24 74
48 0
3 22
126 75
116 47
74 132
125 6
57 68
125 9
143 142
28 94
31 114
19 124
79 41
0 120
104 141
80 42
84 94
22 65
19 46
34 10
107 38
34 62
20 61
32 49
64 81
127 22
122 25
78 30
78 24
4 25
123 39
10 53
11 26
37 133
109 87
60 16
137 81
71 57
70 96
68 99
54 47
135 134
64 91
31 65
132 16
133 17
122 86
54 141
8 144
92 49
42 113
35 75
114 118
45 108
58 69
64 114
50 147
2 91
128 1
142 111
39 55
10 103
28 55
117 73
20 44
141 112
48 59
106 29
66 40
20 54
119 65
129 49
112 36
35 110
146 67
35 76
38 6
5 2
51 12
116 142
47 100
68 120
52 9
63 108
62 108
127 43
16 8
61 116
53 72
23 70
"""

waters="""
0.52958 0.71109 0.0
0.83485 0.01207 0.30681
0.02958 0.78892 0.0
0.15417 0.64074 0.18181
0.15913 0.37609 0.30681
0.07948 0.90876 0.0
0.34046 0.76284 0.81819
0.03974 0.95438 0.18181
0.94491 0.15486 0.5
0.21941 0.73328 0.5
0.65955 0.23716 0.18181
0.28 0.96012 0.81819
0.3502 0.59717 0.375
0.22 0.46012 0.81819
0.44491 0.34514 0.5
0.03454 0.41081 0.625
0.02439 0.13189 0.69319
0.96546 0.77092 0.18181
0.15955 0.26284 0.18181
0.64981 0.40283 0.625
0.53455 0.27092 0.81819
0.97561 0.86811 0.30681
0.12458 0.53355 0.125
0.28 0.96012 0.18181
0.97042 0.21109 0.0
0.22 0.46012 0.18181
0.37542 0.03355 0.875
0.84087 0.62391 0.69319
0.54452 0.82053 0.30681
0.83485 0.01207 0.69319
0.15955 0.26284 0.81819
0.0 0.5 0.75
0.16516 0.98793 0.30681
0.14981 0.09717 0.375
0.72042 0.2214 0.0
0.76577 0.64173 0.5
0.72 0.03988 0.81819
0.76493 0.82345 0.30681
0.34087 0.87609 0.69319
0.47561 0.63189 0.30681
0.52439 0.36811 0.69319
0.62458 0.96645 0.875
0.46026 0.45438 0.18181
0.03454 0.41081 0.375
0.65955 0.23716 0.81819
0.87542 0.46645 0.875
0.64981 0.40283 0.375
0.34584 0.14074 0.81819
0.65458 0.79078 0.0
0.16515 0.91966 0.5
0.33485 0.48793 0.69319
0.33485 0.48793 0.30681
0.26493 0.67655 0.30681
0.73507 0.32345 0.30681
0.45548 0.17947 0.69319
0.46546 0.72908 0.18181
0.40559 0.23104 0.5
0.53974 0.54562 0.81819
0.65417 0.85926 0.81819
0.65417 0.85926 0.18181
0.14981 0.09717 0.625
0.47042 0.28892 0.0
0.84542 0.29078 0.0
0.95548 0.32053 0.69319
0.04452 0.67947 0.69319
0.12458 0.53355 0.875
0.46026 0.45438 0.81819
0.72 0.03988 0.18181
0.47561 0.63189 0.69319
0.76493 0.82345 0.69319
0.34087 0.87609 0.30681
0.66516 0.51207 0.69319
0.84584 0.35926 0.18181
0.78 0.53988 0.81819
0.92053 0.09124 0.0
0.66515 0.58034 0.5
0.84087 0.62391 0.30681
0.23406 0.90361 0.0
0.03455 0.22908 0.81819
0.62458 0.96645 0.125
0.42053 0.40876 0.0
0.09441 0.73104 0.5
0.59441 0.76896 0.5
0.97561 0.86811 0.69319
0.5 0.0 0.25
0.16516 0.98793 0.69319
0.22042 0.27861 0.0
0.87542 0.46645 0.125
0.33485 0.41966 0.5
0.54452 0.82053 0.69319
0.02439 0.13189 0.30681
0.96546 0.77092 0.81819
0.05509 0.84514 0.5
0.90559 0.26896 0.5
0.46546 0.91081 0.375
0.8502 0.90283 0.375
0.34046 0.76284 0.18181
0.03974 0.95438 0.81819
0.28059 0.23328 0.5
0.55509 0.65486 0.5
0.23507 0.17655 0.69319
0.15913 0.37609 0.69319
0.77958 0.7214 0.0
0.53455 0.27092 0.18181
0.53454 0.08919 0.375
0.57948 0.59124 0.0
0.8502 0.90283 0.625
0.46546 0.91081 0.625
0.84584 0.35926 0.81819
0.78 0.53988 0.18181
0.71941 0.76673 0.5
0.23507 0.17655 0.30681
0.65913 0.12391 0.69319
0.52439 0.36811 0.30681
0.96546 0.58919 0.625
0.03455 0.22908 0.18181
0.34542 0.20922 0.0
0.73406 0.5964 0.0
0.96546 0.58919 0.375
0.15417 0.64074 0.81819
0.46546 0.72908 0.81819
0.27958 0.77861 0.0
0.26594 0.40361 0.0
0.53974 0.54562 0.18181
0.73507 0.32345 0.69319
0.26493 0.67655 0.69319
0.66516 0.51207 0.30681
0.0 0.5 0.25
0.96026 0.04562 0.18181
0.26577 0.85828 0.5
0.84046 0.73716 0.81819
0.37542 0.03355 0.125
0.96026 0.04562 0.81819
0.84046 0.73716 0.18181
0.73424 0.14173 0.5
0.78059 0.26673 0.5
0.23424 0.35828 0.5
0.04452 0.67947 0.30681
0.15458 0.70922 0.0
0.76594 0.0964 0.0
0.95548 0.32053 0.30681
0.53454 0.08919 0.625
0.34584 0.14074 0.18181
0.45548 0.17947 0.30681
0.83485 0.08034 0.5
0.5 0.0 0.75
0.65913 0.12391 0.30681
0.3502 0.59717 0.625
"""

coord= "relative"

cages="""
14 0.45938 0.88877 0.0
12 0.0 0.0 0.5
15 0.34271 0.04359 0.5
16 -0.15896 -0.09061 0.0
12 0.84105 0.18248 -0.22725
12 0.34105 0.31752 0.22725
12 -0.09755 -0.25447 0.5
16 0.34104 0.59061 0.0
12 0.09755 0.25447 0.5
12 0.5 0.5 -0.5
15 0.15729 0.54359 -0.5
14 -0.04062 -0.38877 0.0
16 0.65896 0.40939 0.0
12 -0.84105 -0.18248 0.22725
12 -0.34105 -0.31752 -0.22725
12 -0.15895 -0.81752 0.22725
15 0.84271 0.45641 -0.5
12 0.59755 0.24553 -0.5
14 0.04062 0.38877 0.0
15 -0.34271 -0.04359 0.5
12 0.15895 0.81752 -0.22725
14 0.54062 0.11123 0.0
12 -0.34105 -0.31752 0.22725
12 0.34105 0.31752 -0.22725
12 0.40245 0.75447 -0.5
16 0.15896 0.09061 0.0
"""

bondlen = 3


cell = """
22.29787574334263 26.193104175639082 13.5197850518029
"""

density = 0.5602388491410102



from genice.cell import cellvectors
cell = cellvectors(a=22.29787574334263,
                   b=26.193104175639082,
                   c=13.5197850518029)
