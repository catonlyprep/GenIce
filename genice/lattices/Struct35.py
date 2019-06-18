# coding: utf-8
"""
Data source: Dutour Sikirić, Mathieu, Olaf Delgado-Friedrichs, and Michel Deza. “Space Fullerenes: a Computer Search for New Frank-Kasper Structures” Acta Crystallographica Section A Foundations of Crystallography 66.Pt 5 (2010): 602–615.

Cage composition:
 (12,14,15,16) = (12,10,4,2,)
"""

pairs="""
97 15
15 100
1 120
6 44
151 45
122 104
71 31
59 132
90 100
45 23
68 126
72 49
55 117
6 56
9 75
98 132
62 127
9 73
80 108
152 139
64 33
147 93
94 151
59 69
54 144
96 50
27 89
66 39
36 107
119 4
112 40
44 147
97 80
3 100
6 137
31 130
60 47
133 13
114 84
135 21
2 137
77 48
67 147
48 151
25 136
1 67
7 51
145 86
110 32
3 40
105 28
102 13
143 84
3 21
40 95
106 31
2 42
30 14
80 21
125 46
90 19
49 111
124 146
110 152
4 13
129 35
25 59
122 119
107 113
44 61
32 31
112 111
145 5
114 137
65 35
120 61
70 20
81 158
19 25
113 159
7 68
28 26
21 0
12 61
84 141
53 122
29 142
12 122
91 117
24 141
94 9
17 102
76 112
77 87
5 107
15 95
36 29
121 149
16 157
142 113
123 65
143 62
96 22
138 58
47 89
62 67
18 43
101 131
50 74
97 124
158 36
8 131
23 69
78 123
44 104
10 42
74 63
100 126
72 134
58 157
87 11
145 60
110 158
23 102
141 61
63 17
71 152
0 126
33 157
89 28
72 153
18 11
114 152
134 65
19 98
56 67
16 70
90 153
97 118
149 1
22 24
5 54
82 153
155 14
77 154
71 156
82 118
26 60
40 108
53 91
139 155
75 154
7 116
130 79
70 57
113 46
130 125
136 48
88 45
103 140
127 93
64 156
51 144
43 132
134 0
92 102
37 51
148 34
73 43
52 63
18 111
8 98
138 56
121 109
92 99
90 124
2 127
148 39
3 98
128 0
107 140
95 123
149 50
158 155
86 78
66 130
18 55
22 4
99 38
104 74
135 124
76 87
103 46
103 34
51 159
46 39
50 147
108 65
154 4
10 62
35 26
150 92
93 150
73 146
129 80
94 131
134 28
41 30
115 141
70 1
117 119
27 153
116 35
36 148
86 15
43 83
10 156
125 58
111 131
112 132
142 37
16 56
30 85
81 33
58 142
55 154
81 37
155 34
118 11
83 69
157 79
41 144
86 68
83 52
109 150
91 133
60 148
151 91
27 126
129 128
121 53
45 52
32 29
26 85
101 48
115 137
139 79
41 34
85 39
136 75
88 74
144 140
8 135
22 12
145 129
115 93
96 150
106 57
53 38
106 120
49 108
71 143
64 103
2 16
118 49
87 59
92 88
10 138
9 52
8 73
149 12
14 37
119 63
11 146
20 84
24 38
57 79
32 138
101 76
117 83
105 159
116 78
136 23
72 135
115 99
33 42
104 99
76 82
89 54
5 105
125 156
82 95
106 6
7 128
81 140
110 42
68 54
20 127
77 133
159 85
114 57
25 146
75 17
69 133
78 47
128 105
66 29
38 13
96 17
116 30
101 19
109 24
47 41
27 123
64 139
121 88
143 120
109 20
66 14
94 55
"""

waters="""
0.6831 0.625 0.07327
0.5 0.6835 0.60279
0.8169 0.3165 0.66806
0.875 0.5 0.15358
0.25 0.0 0.42547
0.8081 0.0 0.96475
0.0 0.625 0.63704
0.875 0.5 0.98048
0.6835 0.6915 0.22552
0.6835 0.8169 0.33194
0.6915 0.0 0.7123
0.125 0.0 0.24805
0.3081 0.8169 0.51699
0.125 0.1831 0.42673
0.125 0.5 0.86297
0.0 0.1835 0.10279
0.6919 0.5 0.67932
0.75 0.0 0.42547
0.1915 0.8165 0.27448
0.6835 0.3085 0.22552
0.5 0.3165 0.60279
0.8081 0.6915 0.12255
0.375 0.0 0.48048
0.8085 0.3081 0.37745
0.3081 0.1831 0.51699
0.8085 0.1835 0.27448
0.3169 0.8081 0.98301
0.5 0.25 0.07454
0.5 0.875 0.01953
0.0 0.8081 0.82068
0.25 0.5 0.92547
0.1835 0.8085 0.72552
0.0 0.875 0.75196
0.6915 0.3165 0.77448
0.3085 0.1919 0.87745
0.1919 0.6831 0.01699
0.0 0.0 0.86492
0.875 0.5 0.86297
0.1831 0.3081 0.48301
0.3085 0.8081 0.87745
0.125 0.5 0.15358
0.375 0.3169 0.92673
0.8165 0.1915 0.72552
0.0 0.6915 0.2877
0.0 0.75 0.57454
0.6835 0.5 0.39721
0.5 0.875 0.84643
0.3169 0.1919 0.98301
0.5 0.3081 0.32068
0.3169 0.8165 0.16806
0.6919 0.8169 0.51699
0.75 0.5 0.92547
0.8085 0.6919 0.37745
0.3081 0.5 0.46475
0.6831 0.1919 0.98301
0.3165 0.8169 0.33194
0.8169 0.6835 0.66806
0.3081 0.5 0.67932
0.6915 0.6835 0.77448
0.0 0.3085 0.2877
0.1919 0.0 0.96475
0.1831 0.875 0.57327
0.625 0.0 0.65358
0.875 0.8169 0.42673
0.5 0.1915 0.7877
0.3169 0.625 0.07327
0.1835 0.6831 0.83194
0.6919 0.8085 0.62255
0.8081 0.3169 0.01699
0.0 0.375 0.34643
0.5 0.5 0.63508
0.3085 0.0 0.7123
0.5 0.875 0.13704
0.8085 0.8165 0.27448
0.8169 0.6919 0.48301
0.625 0.0 0.36297
0.3165 0.3085 0.22552
0.3165 0.1831 0.33194
0.1919 0.3169 0.01699
0.375 0.5 0.74805
0.0 0.8165 0.10279
0.8165 0.3169 0.83194
0.3169 0.1835 0.16806
0.0 0.625 0.34643
0.3081 0.1915 0.62255
0.375 0.6831 0.92673
0.0 0.1919 0.03525
0.1915 0.1835 0.27448
0.6919 0.5 0.46475
0.5 0.125 0.01953
0.6831 0.1835 0.16806
0.3165 0.5 0.39721
0.8169 0.3081 0.48301
0.8169 0.125 0.57327
0.5 0.6919 0.32068
0.1919 0.3085 0.12255
0.625 0.0 0.48048
0.0 0.0 0.13508
0.8085 0.5 0.2123
0.0 0.375 0.51953
0.8081 0.3085 0.12255
0.5 0.375 0.25196
0.875 0.1831 0.42673
0.5 0.125 0.84643
0.0 0.625 0.51953
0.6831 0.8081 0.98301
0.1831 0.6835 0.66806
0.8165 0.0 0.89721
0.1919 0.6915 0.12255
0.5 0.3081 0.53525
0.0 0.125 0.75196
0.3165 0.6915 0.22552
0.1915 0.5 0.2123
0.6915 0.8081 0.87745
0.1831 0.3165 0.66806
0.0 0.25 0.57454
0.125 0.5 0.98048
0.1915 0.6919 0.37745
0.1919 0.0 0.17932
0.125 0.8169 0.42673
0.3081 0.8085 0.62255
0.5 0.5 0.5
0.1831 0.6919 0.48301
0.3169 0.375 0.07327
0.8081 0.0 0.17932
0.5 0.8085 0.7877
0.6831 0.375 0.07327
0.6919 0.1915 0.62255
0.8081 0.6831 0.01699
0.0 0.8081 0.03525
0.3085 0.6835 0.77448
0.5 0.625 0.25196
0.0 0.5 0.25
0.1915 0.3081 0.37745
0.5 0.75 0.07454
0.6831 0.8165 0.16806
0.6835 0.1831 0.33194
0.0 0.375 0.63704
0.8165 0.8085 0.72552
0.3085 0.3165 0.77448
0.6915 0.1919 0.87745
0.1831 0.125 0.57327
0.8165 0.6831 0.83194
0.375 0.0 0.65358
0.625 0.3169 0.92673
0.0 0.0 0.0
0.875 0.0 0.24805
0.8169 0.875 0.57327
0.1835 0.0 0.89721
0.5 0.6919 0.53525
0.6919 0.1831 0.51699
0.5 0.5 0.36492
0.1835 0.1915 0.72552
0.5 0.125 0.13704
0.375 0.0 0.36297
0.1835 0.3169 0.83194
0.5 0.0 0.75
0.625 0.5 0.74805
0.0 0.1919 0.82068
0.625 0.6831 0.92673
"""

coord= "relative"

cages="""
14 0.5 0.76761 0.42697
16 0.0 -0.5 -0.25
12 1.0 0.5 0.43204
12 0.5 0.26599 0.69713
14 0.5 0.5 1.0
15 0.5 0.5 0.84792
14 -0.26761 0.0 0.07303
16 0.5 0.0 0.25
14 0.0 0.26761 -0.07303
14 0.0 0.0 0.5
12 0.5 0.0 -0.06796
12 0.5 0.73401 0.69713
12 0.0 -0.23401 0.19713
12 0.0 0.5 0.06796
12 -0.23401 0.0 -0.19713
14 0.5 0.23239 0.42697
14 0.76761 0.5 0.57303
12 0.0 0.23401 0.19713
12 0.5 1.0 0.56796
15 0.0 0.0 0.34792
12 0.73401 0.5 0.30287
14 0.0 -0.26761 -0.07303
14 0.26761 0.0 0.07303
12 0.26599 0.5 0.30287
15 0.5 0.5 0.15208
15 0.0 0.0 -0.34792
12 0.23401 0.0 -0.19713
14 0.23239 0.5 0.57303
"""

bondlen = 3


cell = """
13.144879859028674 13.144879859028674 44.58305335060767
"""

density = 0.6208242688729755



from genice.cell import cellvectors
cell = cellvectors(a=13.144879859028674,
                   b=13.144879859028674,
                   c=44.58305335060767)
