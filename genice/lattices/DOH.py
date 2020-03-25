# coding: utf-8

desc={"ref": {},
      "usage": "No options available.",
      "brief": "Clathrate type H."
      }

cages="""
12         0.5000 0.5000 0.5000
12         0.4167 0.0000 0.5000
12_1       0.7500 0.3333 0.7500
12         0.5000 0.5000 0.0000
12_1       0.6667 0.3333 0.2500
12_1       0.3333 0.6667 0.2500
12         0.0000 0.5833 0.5000
20         1.0000 0.0000 0.2000
20         0.0000 0.0000 0.7500
12_1       0.3333 0.6667 0.7500
12         1.0000 0.5000 0.0000
12         0.5000 0.0000 0.0000
"""

bondlen=3.0000000000030558
coord='relative'


density=0.755632278461

waters="""
    0.3333    0.6667    0.4301
    0.6667    0.3333    0.4301
    0.6667    0.3333    0.0699
    0.3333    0.6667    0.0699
    0.1305    0.2609    0.0000
    0.1304    0.8695    0.0000
    0.7391    0.8696    0.0000
    0.8695    0.7391    0.0000
    0.8696    0.1305    0.0000
    0.2609    0.1304    0.0000
    0.6119    0.6119    0.3186
    1.0000    0.3881    0.3186
    0.3881    0.0000    0.3186
    0.3881    0.3881    0.3186
    0.0000    0.6119    0.3186
    0.6119    0.0000    0.3186
    0.3881    0.3881    0.1815
    0.0000    0.6119    0.1815
    0.6119    0.0000    0.1815
    0.6119    0.6119    0.1815
    1.0000    0.3881    0.1815
    0.3881    0.0000    0.1815
    0.7914    0.5827    0.3877
    0.7913    0.2086    0.3877
    0.4173    0.2087    0.3877
    0.2086    0.4173    0.3877
    0.2087    0.7914    0.3877
    0.5827    0.7913    0.3877
    0.2086    0.4173    0.1123
    0.2087    0.7914    0.1123
    0.5827    0.7913    0.1123
    0.7914    0.5827    0.1123
    0.7913    0.2086    0.1123
    0.4173    0.2087    0.1123
    0.3333    0.6667    0.9301
    0.6667    0.3333    0.9301
    0.6667    0.3333    0.5699
    0.3333    0.6667    0.5699
    0.1305    0.2609    0.5000
    0.1304    0.8695    0.5000
    0.7391    0.8696    0.5000
    0.8695    0.7391    0.5000
    0.8696    0.1305    0.5000
    0.2609    0.1304    0.5000
    0.6119    0.6119    0.8186
    1.0000    0.3881    0.8186
    0.3881    0.0000    0.8186
    0.3881    0.3881    0.8186
    0.0000    0.6119    0.8186
    0.6119    0.0000    0.8186
    0.3881    0.3881    0.6815
    0.0000    0.6119    0.6815
    0.6119    0.0000    0.6815
    0.6119    0.6119    0.6815
    1.0000    0.3881    0.6815
    0.3881    0.0000    0.6815
    0.7914    0.5827    0.8877
    0.7913    0.2086    0.8877
    0.4173    0.2087    0.8877
    0.2086    0.4173    0.8877
    0.2087    0.7914    0.8877
    0.5827    0.7913    0.8877
    0.2086    0.4173    0.6123
    0.2087    0.7914    0.6123
    0.5827    0.7913    0.6123
    0.7914    0.5827    0.6123
    0.7913    0.2086    0.6123
    0.4173    0.2087    0.6123
"""


from genice.cell import cellvectors
cell = cellvectors(a=12.4212113964,
                   b=12.421211396338748,
                   c=10.0656455142*2,
                   C=120.0000000000566)
