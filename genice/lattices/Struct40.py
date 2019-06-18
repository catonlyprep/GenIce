# coding: utf-8
"""
Data source: Dutour Sikirić, Mathieu, Olaf Delgado-Friedrichs, and Michel Deza. “Space Fullerenes: a Computer Search for New Frank-Kasper Structures” Acta Crystallographica Section A Foundations of Crystallography 66.Pt 5 (2010): 602–615.

Cage composition:
 (12,14,15,16) = (12,12,8,0,)
"""

pairs="""
169 65
12 73
81 159
181 146
7 164
162 109
77 156
151 180
32 61
33 61
110 111
163 174
123 75
126 44
29 69
3 56
16 120
40 51
13 63
84 95
32 1
128 115
78 43
105 85
46 74
161 70
0 27
132 140
121 24
138 121
10 172
151 89
47 128
73 163
92 48
132 45
7 181
171 57
160 54
143 122
144 177
22 0
85 4
113 74
151 58
146 110
60 46
172 155
104 123
92 25
102 148
83 23
126 105
152 106
97 67
42 112
55 180
14 2
174 87
117 153
126 7
8 127
90 66
98 141
150 137
114 11
99 37
170 9
77 129
123 114
15 137
136 87
32 51
108 38
34 165
34 166
43 135
105 45
107 182
2 63
42 62
83 135
155 24
13 133
123 60
59 94
148 54
99 119
158 79
78 88
133 23
99 118
1 65
72 101
85 146
105 167
35 136
128 79
108 76
5 40
44 26
176 122
124 18
129 88
50 154
42 69
130 88
130 89
179 26
125 128
12 63
116 122
91 37
76 167
47 75
162 72
82 59
141 131
169 17
16 104
67 147
165 96
124 160
96 80
114 18
72 56
102 57
93 132
74 75
159 160
152 150
90 103
144 176
182 87
8 152
27 143
164 26
104 124
16 54
36 147
115 183
78 58
64 31
38 103
71 109
168 19
177 116
12 145
150 72
178 111
15 106
76 66
45 139
52 156
145 58
77 138
23 95
175 56
130 172
81 11
62 71
171 116
6 57
2 64
142 95
157 143
10 44
10 45
118 48
125 59
113 176
83 180
137 36
86 175
107 147
4 111
88 141
33 66
8 107
2 9
156 58
35 127
28 75
62 101
64 147
106 9
160 47
44 110
133 96
73 142
86 182
35 71
142 173
154 112
15 67
100 170
41 80
183 69
39 17
151 138
43 55
124 74
6 33
30 115
12 49
111 118
167 65
177 148
82 154
89 24
20 51
157 40
4 164
100 31
170 53
140 119
168 103
56 70
145 166
125 161
126 168
0 68
159 94
172 131
27 103
60 148
21 5
20 6
173 174
69 70
161 162
15 14
55 156
20 68
91 24
175 50
11 70
81 60
127 36
13 170
107 9
155 118
86 35
108 19
125 114
97 49
13 142
10 178
19 17
173 53
127 101
4 139
21 143
77 34
85 169
49 64
149 89
149 25
166 80
90 169
98 121
81 183
84 134
109 117
84 180
97 41
30 158
3 117
158 11
98 25
63 80
22 167
165 135
22 168
26 131
83 145
137 53
86 150
61 171
8 50
182 53
28 40
14 173
153 112
101 154
181 76
146 19
18 94
100 36
5 120
27 33
57 120
55 149
100 136
139 155
92 178
91 179
93 179
71 29
21 38
20 39
98 43
22 39
97 163
16 28
102 113
31 133
138 134
37 149
3 158
108 61
51 116
14 41
28 177
163 96
37 129
46 144
47 144
113 157
174 31
134 135
93 99
152 109
119 131
84 52
121 48
41 95
52 73
179 139
178 140
46 115
79 153
175 29
32 17
68 120
68 122
30 18
7 90
67 87
25 119
176 54
129 48
78 34
136 106
92 130
30 42
93 110
3 62
82 162
38 65
39 66
102 104
164 140
161 153
91 141
94 112
52 165
82 29
49 23
6 157
0 1
50 117
1 5
59 183
159 79
166 134
181 132
21 171
"""

waters="""
0.625 0.625 0.3914
0.375 0.75 0.39046
0.875 0.75 0.89046
0.65989 0.34011 0.08018
0.125 0.875 0.53962
0.29321 0.91821 0.3499
0.70679 0.08179 0.3499
0.75 0.25 0.5
0.75 0.75 0.0
0.78489 0.59011 0.93397
0.71511 0.71511 0.56508
0.41821 0.20679 0.15011
0.625 0.625 0.82348
0.66821 0.33179 0.867
0.125 0.875 0.8914
0.21511 0.78489 0.93492
0.45679 0.79321 0.27866
0.09011 0.71511 0.43397
0.625 0.0 0.17557
0.125 0.5 0.46133
0.83179 0.83179 0.367
0.16821 0.16821 0.367
0.71511 0.71511 0.43492
0.625 0.0 0.82443
0.29321 0.91821 0.65011
0.70679 0.08179 0.65011
0.90989 0.28489 0.56603
0.75 0.375 0.39046
0.20679 0.79321 0.27866
0.21511 0.40989 0.06603
0.79321 0.20679 0.14916
0.875 0.125 0.8914
0.25 0.625 0.39046
0.625 0.25 0.39046
0.0 0.5 0.75
0.0 0.25 0.0
0.625 0.0 0.96133
0.29321 0.29321 0.64916
0.15989 0.15989 0.41982
0.84011 0.84011 0.41982
0.125 0.875 0.32348
0.20679 0.79321 0.85084
0.875 0.125 0.1086
0.79321 0.20679 0.72134
0.875 0.5 0.53867
0.5 0.875 0.53867
0.04321 0.29321 0.22134
0.95679 0.70679 0.22134
0.08179 0.70679 0.65011
0.58179 0.79321 0.8499
0.625 0.625 0.03962
0.08179 0.70679 0.3499
0.29321 0.29321 0.77866
0.40989 0.21511 0.93397
0.58179 0.58179 0.25931
0.54321 0.20679 0.72134
0.40989 0.21511 0.06603
0.5 0.125 0.32443
0.58179 0.58179 0.74069
0.33179 0.66821 0.133
0.29321 0.29321 0.22134
0.375 0.375 0.3914
0.78489 0.21511 0.06508
0.79321 0.58179 0.8499
0.75 0.875 0.89046
0.28489 0.90989 0.43397
0.71511 0.09011 0.43397
0.34011 0.65989 0.91982
0.70679 0.70679 0.35084
0.125 0.25 0.10955
0.25 0.125 0.10955
0.0 0.375 0.03867
0.375 0.0 0.03867
0.375 0.375 0.82348
0.91821 0.08179 0.24069
0.08179 0.91821 0.24069
0.5 0.125 0.46133
0.20679 0.54321 0.72134
0.79321 0.45679 0.72134
0.79321 0.58179 0.15011
0.0 0.625 0.82443
0.375 0.375 0.17652
0.34011 0.65989 0.08018
0.70679 0.95679 0.77866
0.29321 0.04321 0.77866
0.25 0.75 0.5
0.25 0.25 0.0
0.21511 0.40989 0.93397
0.875 0.5 0.67557
0.5 0.875 0.67557
0.875 0.125 0.46038
0.16821 0.16821 0.633
0.83179 0.83179 0.633
0.28489 0.28489 0.56508
0.58179 0.79321 0.15011
0.375 0.0 0.82443
0.0 0.375 0.82443
0.33179 0.66821 0.867
0.875 0.125 0.67652
0.375 0.375 0.6086
0.78489 0.21511 0.93492
0.625 0.0 0.03867
0.54321 0.20679 0.27866
0.90989 0.28489 0.43397
0.5 0.0 0.25
0.5 0.75 0.5
0.0 0.625 0.96133
0.625 0.625 0.96038
0.28489 0.28489 0.43492
0.0 0.625 0.03867
0.125 0.5 0.53867
0.09011 0.71511 0.56603
0.75 0.875 0.10955
0.79321 0.20679 0.27866
0.375 0.0 0.17557
0.0 0.375 0.17557
0.125 0.5 0.32443
0.78489 0.59011 0.06603
0.25 0.625 0.60955
0.625 0.25 0.60955
0.5 0.875 0.32443
0.125 0.875 0.67652
0.875 0.5 0.32443
0.29321 0.04321 0.22134
0.70679 0.95679 0.22134
0.20679 0.79321 0.14916
0.75 0.5 0.5
0.75 0.0 0.0
0.0 0.625 0.17557
0.125 0.5 0.67557
0.70679 0.70679 0.64916
0.75 0.375 0.60955
0.5 0.125 0.53867
0.79321 0.20679 0.85084
0.08179 0.91821 0.75931
0.91821 0.08179 0.75931
0.0 0.375 0.96133
0.375 0.0 0.96133
0.20679 0.79321 0.72134
0.28489 0.90989 0.56603
0.71511 0.09011 0.56603
0.91821 0.29321 0.65011
0.41821 0.20679 0.8499
0.91821 0.29321 0.3499
0.0 0.5 0.25
0.70679 0.70679 0.77866
0.25 0.5 0.5
0.59011 0.78489 0.93397
0.41821 0.41821 0.25931
0.5 0.125 0.67557
0.25 0.0 0.0
0.45679 0.79321 0.72134
0.0 0.75 0.0
0.875 0.75 0.10955
0.59011 0.78489 0.06603
0.375 0.75 0.60955
0.41821 0.41821 0.74069
0.875 0.125 0.32348
0.66821 0.33179 0.133
0.625 0.625 0.17652
0.70679 0.70679 0.22134
0.125 0.875 0.1086
0.21511 0.78489 0.06508
0.20679 0.41821 0.8499
0.875 0.125 0.53962
0.04321 0.29321 0.77866
0.95679 0.70679 0.77866
0.5 0.875 0.46133
0.875 0.5 0.46133
0.125 0.875 0.46038
0.65989 0.34011 0.91982
0.29321 0.29321 0.35084
0.625 0.625 0.6086
0.25 0.125 0.89046
0.125 0.25 0.89046
0.375 0.375 0.03962
0.79321 0.45679 0.27866
0.20679 0.54321 0.27866
0.84011 0.84011 0.58018
0.15989 0.15989 0.58018
0.5 0.0 0.75
0.5 0.25 0.5
0.375 0.375 0.96038
0.20679 0.41821 0.15011
"""

coord= "relative"

cages="""
12 0.0 0.0 0.39057
12 0.5 0.5 0.89057
12 0.5 0.5 0.10943
12 0.0 0.0 0.60943
14 0.17284 0.17284 0.28871
14 0.82716 0.82716 0.28871
14 0.32716 0.67284 0.78871
14 0.32716 0.67284 0.21129
14 0.82716 0.82716 0.71129
14 0.67284 0.32716 0.78871
14 0.67284 0.32716 0.21129
14 0.17284 0.17284 0.71129
15 0.0 0.0 0.17406
15 0.5 0.5 0.67406
15 0.5 0.5 0.32594
15 0.0 0.0 0.82594
12 0.0 0.5 0.10564
12 0.0 0.5 0.60564
12 0.5 0.0 0.39436
12 0.0 0.5 0.89436
12 0.5 0.0 0.89436
12 0.0 0.5 0.39436
12 0.5 0.0 0.60564
12 0.5 0.0 0.10564
15 0.13956 0.13956 0.5
15 0.86044 0.86044 0.5
15 0.36044 0.63956 0.0
15 0.63956 0.36044 0.0
14 0.0 0.0 0.04905
14 0.5 0.5 0.54905
14 0.5 0.5 0.45095
14 0.0 0.0 0.95095
"""

bondlen = 3


cell = """
15.612917728598969 15.612917728598969 93.43202863446575
"""

density = 0.24148249589841608



from genice.cell import cellvectors
cell = cellvectors(a=15.612917728598969,
                   b=15.612917728598969,
                   c=93.43202863446575)
