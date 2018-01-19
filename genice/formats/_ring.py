# coding: utf-8
"""
Test suite: ring direction statistics
"""

# A directed cycle is expressed as an array of True and False.
# For example,
# --> --> --> : [True, True, False]
# --> <-- --> : [Frue, False, True]
#They are isomorphic if they can be identical by rotations and inversions.

# 


import itertools as it
from countrings import countrings_nx as cr
import sys
from collections import defaultdict
import networkx as nx
from math import log

def isomorphs(a):
    """
    return the symmetry number of cycle a
    """
    iso = set()
    aa = a + a
    for i in range(len(a)):
        part = tuple(aa[i:i+len(a)])
        iso.add(part)
    e = [not x for x in a]
    ee = e + e
    for i in range(len(a)):
        part = tuple(ee[i:i+len(a)])
        iso.add(part)
    return iso


def code(ori):
    """
    from an array of True/False to an integer.
    """
    s = 0
    for i in range(len(ori)):
        if ori[i]:
            s += 1<<i
    return s


def encode(ori):
    m = 9999
    for i in isomorphs(ori):
        c = code(i)
        if c < m:
            m = c
    return m

    
def symmetry(a):
    return len(isomorphs(a))


def freedom(a):
    """
    return possible number of molecular placements
    """
    n = 1
    for i in range(len(a)):
        if a[i-1] is a[i]:
            n *= 2
    return n


def pauling_probability(a):
    N = len(a)
    return symmetry(a) * freedom(a) / (3**N+1)  #I do not understand why + 1


def pauling_combination(a):
    N = len(a)
    return symmetry(a) * freedom(a)


def test():
    uniq = set()
    for a in it.product((False, True), repeat=6):
        iso = isomorphs(a)
        if len(iso & uniq) == 0:
            uniq.add(a)
            print(a)
            print(symmetry(a))
            print(freedom(a))
            print(pauling_probability(a))



def contains(a,b):
    """
    return True if one of the isomorphs of b is included in the set a.
    """
    return len(a & isomorphs(b)) > 0
    

def probabilities(N):
    prob = dict()
    for a in it.product((False, True), repeat=N):
        c = encode(a)
        if c not in prob:
            prob[c] = pauling_probability(a)
    return prob


def combinations(N):
    comb = dict()
    for a in it.product((False, True), repeat=N):
        c = encode(a)
        if c not in comb:
            comb[c] = pauling_combination(a)
    return comb


def orientations(members, digraph):
    return [digraph.has_edge(members[i-1], members[i]) for i in range(len(members))]


def hook4(lattice):
    lattice.logger.info("Hook4: Ring test.")
    graph = nx.Graph(lattice.spacegraph) #undirected
    stat = dict()
    prob = defaultdict(int)
    for n in 3,4,5,6,7,8:
        prob[n] = probabilities(n)
        stat[n] = defaultdict(int)
        # lattice.logger.info("  sum of Pauling comb.:{0} / {1}".format(sum(combinations(n).values()), 3**n))
    for ring in cr.rings_iter(graph, 8):
        ori = orientations(ring, lattice.spacegraph)
        c   = encode(ori)
        n   = len(ring)
        stat[n][c] += 1
    #size code code(binary) Approx. Stat.
    for n in 3,4,5,6,7,8:
        fmtstr = "{{0}} {{1}} {{1:0{0}b}} {{2:.5f}} {{3:.5f}}".format(n)
        denom = 0
        for c in stat[n]:
            denom += stat[n][c]
        if denom > 0:
            dKL = 0.0
            for c in prob[n]:
                print(fmtstr.format(n,c,prob[n][c], stat[n][c]/denom))
                q = stat[n][c]/denom
                p = prob[n][c]
                if q > 0.0:
                    dKL += q*(log(q) - log(p))
            dKL /= log(2.0)  #bit
            print("{1} {0} dKL[{0}-ring]".format(n,dKL))
            lattice.logger.info("  dKL[{0}-ring]={1}".format(n,dKL))
    #print(score)
    lattice.logger.info("Hook4: end.")


hooks = {4:hook4}
