#!/usr/bin/env python3

#FAU Decoration of a 4-network
#読みこんだAR3Rの座標を、FAU構造における多面体vertexの位置とみなし、
#それらを連結するネットワークを六角柱で修飾して大きなネットワークを作る。

from math import acos, pi, sin, cos
from collections import defaultdict
import numpy as np
import logging
import re

# Aeroiceの超格子の接点多面体で、きちんとorderするように設計する。
# そのためには、超格子のもととなるdiamond latticeを白黒二部グラフとし、
# 黒から白へ向けていつも多角柱を作るようにする。
# 黒、白の接点多面体の六員環はすべてhomodromicとするが、どっちむきになるかは角柱の長さによって変わる。角柱が奇数段であれば、白黒とも同じ向きになるが、偶数段だと反転する。tune_anglesはてきとうに角柱を回転してつじつまをあわしているが、これを廃止する必要があるな。まずは全部決定論的に作る。
# ちょっとまじめに考えないといけない感じ。模型を睨む。

def tune_angles(sixvecs, pivot):
    """
    Find the best origin of angles to make sum cos(3 th) largest
    """
    sixangles = []
    for i in range(len(sixvecs)):
        vec = sixvecs[i]
        cosine = sixvecs[0] @ vec
        if cosine > 1.0:
            cosine = 1.0
        angle = acos(cosine)
        sine   = np.cross(sixvecs[0], vec)
        if sine @ pivot < 0:
            angle = -angle
        sixangles.append(angle)
    offset = 0
    while True:
        sum = 0.0
        dsum = 0.0
        for a in sixangles:
            sum += cos((a+offset)*6)
            dsum += -sin((a+offset)*6)
        doffset = dsum / 20.0
        if abs(doffset) < 1e-6:
            return offset
        offset += doffset



class decorate():
    def __init__(self, atoms, cell, pairs, Ncyl):
        """
        Ncyl is the number of cylinders to be inserted (>0)
        """
        #make netghbor list
        nei = defaultdict(set)
        for i,j in pairs:
            nei[i].add(j)
            nei[j].add(i)
        self.nei = nei
        self.atoms = atoms
        self.cell  = cell
        self.Ncyl  = Ncyl
        self.vertices = []
        self.fixedEdges = []
        for pair in pairs:
            self.one(pair)

    def one(self, pair):
        logger = logging.getLogger()
        i,j = pair
        dij = self.atoms[j] - self.atoms[i]
        dij -= np.floor(dij + 0.5)
        dij = dij @ self.cell
        scale = np.linalg.norm(dij)
        dij /= scale
        rests = self.nei[i].copy()
        rests.remove(j)
        logger.debug("Rests: {0}".format(rests))
        #Regularize the dihedral angles
        #to point them 6-fold directions.
        #by adding an offset
        vecs = []
        for k in rests:
            vec = self.atoms[k] - self.atoms[i]
            vec -= np.floor(vec + 0.5)
            vec = vec @ self.cell
            #orthogonalize
            shadow = dij @ vec
            vec -= shadow*dij
            vec /= np.linalg.norm(vec)
            #print(np.dot(vec,dij))
            vecs.append(vec)
        # 向きを同じにする。
        if np.linalg.det(np.vstack([dij,vecs[0],vecs[1]])) < 0:
            vecs[0], vecs[1] = vecs[1], vecs[0]
        offset = pi/6 #30 degree
        x = vecs[0]
        z = dij
        y = np.cross(z,x)
        sixvecs = np.zeros((6,3))
        for j in range(6):
            a = j*pi*2/6 + offset
            sixvecs[j] = x*cos(a) + y*sin(a)
        #determine r
        #assume edge length is 1
        #the radius of the outer sphere of the polyhed is sqrt(3/2)
        L = (3/2)**0.5 * 2 + self.Ncyl
        r = 1/L     #edge len = radius of cyl
        rp = (3/2)**0.5 / L  # = radius of polyhed
        #
        icell = np.linalg.inv(self.cell)
        a = self.atoms[i] @ self.cell
        s = ""
        for j in range(0, self.Ncyl+1):
            vec0 = dij*(rp + j*r)*scale + a
            for vec in sixvecs:
                rpos = vec0 + vec*r*scale
                pos = rpos @ icell
                self.vertices.append(pos)
            first = len(self.vertices)-6
            if j % 2 == 0:
                for k in range(5):
                    self.fixedEdges.append((first+k, first+k+1))
                self.fixedEdges.append((first+5,first))
            else:
                for k in range(5):
                    self.fixedEdges.append((first+k+1, first+k))
                self.fixedEdges.append((first,first+5))
            if j > 0:
                for k in range(6):
                    if k % 2 == 0:
                        self.fixedEdges.append((first+k, first+k-6))
                    else:
                        self.fixedEdges.append((first+k-6, first+k))


import genice2.lattices
from genice2.lattices import ice1c # base topology

class Lattice(genice2.lattices.Lattice):
    def __init__(self):
        logger = logging.getLogger()
        self.cell1c = ice1c.self.cell
        self.waters1c = np.fromstring(ice1c.self.waters, sep=" ")
        self.waters1c = self.waters1c.reshape((self.waters1c.shape[0]//3,3))
        self.pairs1c = np.fromstring(ice1c.self.pairs, sep=" ", dtype=int)
        self.pairs1c = self.pairs1c.reshape((self.pairs1c.shape[0]//2,2))
        #
        #0..3を黒、4..7を白とする。もともと二部グラフになっているようだ。
        #


        def argparser(arg):
            assert re.match("^[0-9]+$", arg) is not None, "Argument must be an integer."
            Ncyl = int(arg)
            logger.info("Superlattice {0}xFAU".format(Ncyl))
            dec = decorate(self.waters1c, self.cell1c, self.pairs1c, Ncyl)
            self.coord='relative'
            self.cell = "{0} {1} {2}".format(dec.self.cell[0,0],dec.self.cell[1,1],dec.self.cell[2,2])
            self.waters = dec.vertices
            self.fixed = dec.self.fixedEdges

        # default.
        argparser("1")