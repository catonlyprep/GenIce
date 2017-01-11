#!/usr/bin/env python3
#coding: utf-8
#input: coordinate of the nodes, the digraph obeying the ice rule.
#output: the digraph with zero net dipole.

import sys
import math
import networkx
import random
import numpy as np
import logging




#convert numpy array to a plain string
def plaintext(a):
    s = ""
    for x in a:
        s += "{0} ".format(x)
    return s



def Line(v0,v1):
    return "l " + plaintext(v0) + plaintext(v1) + "\n"


def Arrow(v0,v1):
    return "s " + plaintext(v0) + plaintext(v1) + "\n"



def Polygon(vertices):
    s = "p {0} ".format(len(vertices))
    for v in vertices:
        s += plaintext(v)
    return s + "\n"



def Color(x):
    return "@ {0}\n".format(int(x))



def Layer(x):
    return "y {0}\n".format(int(x))


def NewPage():
    return "\n"


class YaplotDraw(networkx.DiGraph):
    def __init__(self, coord, cell, data=None):
        super().__init__(data)
        self.coord = coord
        self.cell  = cell

    def draw_edge(self,i,j):
        ci = self.coord[i]  #0..1
        cj = self.coord[j]
        d = cj - ci
        d -= np.floor( d + 0.5 )
        xi = np.dot(ci,self.cell)
        xj = np.dot(ci+d,self.cell)
        if self.has_edge(i,j):
            return Color(4) + "a 2\n" + Arrow(xi, xj)
        elif self.has_edge(j,i):
            return Color(5) + "a 2\n" + Arrow(xj, xi)
        else:
            return Color(0) + Line(xi, xj)
            

    def draw_cell(self):
        s = Color(2)
        ex = np.array([1.,0.,0.])
        ey = np.array([0.,1.,0.])
        ez = np.array([0.,0.,1.])
        x = np.dot(ex,self.cell)
        y = np.dot(ey,self.cell)
        z = np.dot(ez,self.cell)
        zero = np.zeros_like(x)
        for vx in (zero, x):
            for vy in (zero, y):
                s += Line(vx+vy,vx+vy+z)
        for vx in (zero, x):
            for vz in (zero, z):
                s += Line(vx+vz,vx+y+vz)
        for vz in (zero, z):
            for vy in (zero, y):
                s += Line(vy+vz,x+vy+vz)
        return s

    def draw_path(self,path):
        s = Color(3)
        for i in range(len(path)-1):
            j,k = path[i],path[i+1]
            s += self.draw_edge(j,k)
        return s
    

    


class IceGraph(networkx.DiGraph):
    #def __init__(data=None):
    #    super(IceGraph, self).__init__(data)

    def register_pairs(self,pairs):
        self.clear()
        for pair in pairs:
            x,y = pair[0:2]
            self.add_edge(x,y)

            
    def _goahead(self,node,marked,order):
        while not marked[node]:
            marked[node] = True
            order.append(node)
            nei = self.neighbors(node)
            next = random.randint(0,1)
            if len(nei) != 2:
                logging.getLogger().error("Dangling bond: {0} {1}".format(node,nei))
            node = nei[next]
        #a cyclic path is found.
        #trim the uncyclic part
        while order[0] != node:
            order.pop(0)
        #add the node at the last again
        order.append(node)
        return order


    def homodromiccycle(self):
        """
        Randomly select a homodromic cycle
        """
        marked = [False] * self.number_of_nodes()
        order = []
        node = random.randint(0,self.number_of_nodes()-1)
        return self._goahead(node,marked,order)


    def isZ4(self):
        """
        Reply whether all the vertices have four neighbors or not.
        """
        good = True
        undir = self.to_undirected()
        for node in range(undir.number_of_nodes()):
            if len(undir.neighbors(node)) != 4:
                good = False
        return good


    def purgedefects(self, defects):
        d = defects[0]
        if self.in_degree(d) == 2 and self.out_degree(d) == 2:
            defects.pop(0)
            return
        if self.in_degree(d) > 2:
            nodes = self.predecessors(d)
            i = random.randint(0,len(nodes)-1)
            node = nodes[i]
            self.remove_edge(node,d)
            self.add_edge(d,node)
            defects.append(node)
        if self.out_degree(d) > 2:
            nodes = self.successors(d)
            i = random.randint(0,len(nodes)-1)
            node = nodes[i]
            self.remove_edge(d,node)
            self.add_edge(node,d)
            defects.append(node)

            
    def defects(self):
        """
        Reply the list of defective vertices.
        """
        defects = []
        for i in range(self.number_of_nodes()):
            if self.in_degree(i) != 2 or self.out_degree(i) != 2:
                defects.append(i)
            if self.degree(i) != 4:
                logger = logging.getLogger()
                logger.error("Non Z4 vertex: {0} {1} {2} {3}".format(i,self.degree(i),self.successors(i),self.predecessors(i)))
        return defects

    def purge_ice_defects(self):
        logger = logging.getLogger()
        if not self.isZ4():
            logger.error("Some water molecules do not have four HBs.")
            sys.exit(1)
        defects = self.defects()
        while len(defects)>0:
            self.purgedefects(defects)
        if len(self.defects()) != 0:
            logger.error("Some water molecules do not obey the ice rule.")
            sys.exit(1)

    def all_shortest_cycles(self, vertex):
        """
        Return the shortest cycles including the given vertex.
        """
        logger = logging.getLogger()
        generators = []
        pathlen = 999999999999999999999999
        paths = []
        for v in self.neighbors(vertex):
            #get the first item
            #Results of this generator is very biased.
            #First resulsts are far from the random walk path.
            #
            generator = networkx.all_shortest_paths(self, source=v, target=vertex)
            logger.debug(type(generator))
            path = next(generator)
            logger.debug("path len: {0}".format(len(path)))
            if len(path) < pathlen:
                generators = [generator,]
                paths = [path,]
                pathlen = len(path)
            elif len(path) == pathlen:
                generators.append(generator)
                paths.append(path)
        for path in paths:
            yield [vertex,] + path
        for generator in generators:
            for path in generator:
                yield [vertex,] + path

    def is_homodromic(self, path):
        for i in range(len(path)-1):
            if not self.has_edge(path[i], path[i+1]):
                return False
        return True
            
    def Homodromize(self, path):
        """
        Make a given unhomodromic cyclic path homodromic.
        (By bypassing the contacting homodromic cycles.)
        """
        pass

            


class SpaceIceGraph(IceGraph):
    """
    Digraph with geometrical info
    """
    XAXIS=1
    YAXIS=2
    ZAXIS=3
    def __init__(self, data=None, coord=None, pbc=True):
        super(SpaceIceGraph, self).__init__(data)
        if coord is not None:
            self.add_vectors(coord, pbc)
            
    def add_vectors(self, coord, pbc=True):
        """
        add vector attributes to each edge
        """
        for i,j,k in self.edges_iter(data=True):
            vec = coord[j] - coord[i]
            if pbc:
                vec -= np.floor(vec + 0.5)
            k["vector"] = vec  #each edge has "vector" attribute
        
    def dipole_of_a_cycle(self, order):
        """
        normally zero.
        Non-zero when it goes across the cell.

        the first element of the order must be the same as the last one.
        """
        delta = np.zeros(3)
        for i in range(len(order)-1):
            delta += self.get_edge_data(order[i],order[i+1])["vector"]
        return delta
            
    def invert_edge(self,from_,to_):
        """
        also invert the attribute vector
        """
        v = self.get_edge_data(from_,to_)["vector"]
        self.remove_edge(from_,to_)
        self.add_edge(to_,from_,vector=-v)


    def invert_path(self, path):
        for i in range(len(path)-1):
            f = path[i]
            t = path[i+1]
            self.invert_edge(f,t) #also invert the attribute vector
        
    def net_polarization(self):
        dipole = np.zeros(3)
        for i,j,k in self.edges_iter(data=True):
            dipole += k["vector"]
        return dipole


    #This is too slow for a big system.  Improve it.
    def depolarize(self):
        """
        It assumes vector attribute is set
        """
        logger = logging.getLogger()
        dipole = self.net_polarization()
        logger.debug("Initial dipole: {0}".format(dipole))
        s0 = np.dot(dipole, dipole)
        #In the following calculations, there must be error allowances.
        while s0 > 0.1:
            path = self.homodromiccycle()
            pathdipole = self.dipole_of_a_cycle(path)
            newdipole = dipole - 2.0 * pathdipole
            logger.debug("Updated dipole: {0}".format(newdipole))
            #logger.debug("Debugged dipole: {0}".format(self.polarization()))
            s1 = np.dot(newdipole, newdipole)
            if s1 < s0:
                self.invert_path(path)
                s0 = s1
                dipole -= 2.0 * pathdipole
                logger.debug("Score: {0}".format(s0))


    def polarize(self, axis):
        """
        make a graph in which all the edges direct along the Z axis.
        """
        original = SpaceIceGraph(self)  #make a copy
        if axis > 0:#+1..+3
            for i,j,k in original.edges_iter(data=True):
                v = k["vector"]
                if v[axis-1] < 0:
                    self.invert_edge(i,j)
        else:
            axis = -axis #-1..-3
            for i,j,k in original.edges_iter(data=True):
                v = k["vector"]
                if v[axis-1] > 0:
                    self.invert_edge(i,j)


    def all_untraversed_shortest_cycles(self, vertex, axis, MaxTrials=None):
        """
        pickup the shortest cycles that do not traverse the axis except the given one.
        """
        logger = logging.getLogger()
        trial = 0
        for path in self.all_shortest_cycles(vertex):
            dipole = self.dipole_of_a_cycle(path)
            logger.debug("{0}".format(dipole))
            if axis > 0:
                dipole[axis-1] -= 1.0  #the dipole along to the axis should be 1.
            else:
                dipole[-axis-1] += 1.0  #the dipole along to the axis should be 1.
            if np.dot(dipole, dipole) < 0.1:  #the dipole is almost zero,
                yield path
                trial = 0
            else:
                logger.debug("Rejected.")
                trial += 1
                if MaxTrials is not None:
                    if MaxTrials < trial:
                        #terminate
                        yield None
                        return




def all_backward_paths(directedgraph,cycle):
    """
    a generator that yields the backward chains in the cycle one by one.
    """
    logger = logging.getLogger()
    ###for debug:
    dir = [directedgraph.has_edge(cycle[head], cycle[head+1]) for head in range(len(cycle)-1)]
    logger.debug("Directions: {0}".format(dir))
        
    head = 0
    #firstly, find the one forward edge
    while not directedgraph.has_edge(cycle[head], cycle[head+1]):
        head += 1
        if head == len(cycle)-1:
            #all the edges are backward
            #yield the backward chain and the intervening forward vertices.
            logger.debug("All the edges are backward.")
            yield cycle, []
            return
    #for convenience, double the cycle
    double = cycle + cycle[1:] + cycle[1:]
    #origin: the first vertex
    origin = cycle[head]
    logger.debug("The first forward edge is at {0}".format(head))
    #and find the first backward edge
    while directedgraph.has_edge(double[head], double[head+1]):
        head += 1
        if double[head] == origin:
            #all the edges are forward
            logger.debug("All the edges are forward.")
            yield [], cycle[1:]
            return
    #reset origin to the first backward edge
    origin = cycle[head]
    while True:
        first = head
        logger.debug("The first backward edge is at {0}".format(head))
        while not directedgraph.has_edge(double[head], double[head+1]):
            head += 1
        last = head
        logger.debug("The last backward edge is at {0}".format(head))
        while directedgraph.has_edge(double[head], double[head+1]):
            head += 1
        forward = head
        logger.debug("Backward path: {0}".format(double[first:last+1]))
        logger.debug("Intervening forward vertices: {0}".format(double[last+1:forward]))
        yield double[first:last+1],double[last+1:forward]
        if double[forward] == origin:
            break
    
    
def are_cycles_same(directedgraph, a,b):
    aa = a.copy()
    bb = b.copy()
    if aa[-1] == aa[0]:
        aa = aa[:-1]
    if bb[-1] == bb[0]:
        bb = bb[:-1]
    bb = tuple(bb)
    NA = len(aa)
    NB = len(bb)
    if NA != NB:
        return False
    N = NA
    aa = aa + aa
    for i in range(N):
        if tuple(aa[i:i+N]) == bb:
            return True
    return False
    

def test_all_backward_paths(directedgraph,cycle):
    logger = logging.getLogger()
    edges = set([(cycle[i], cycle[i+1]) for i in range(len(cycle)-1)])
    vertices = []
    for backpath,interv in all_backward_paths(directedgraph,cycle):
        vertices += backpath + interv
        for edge in [(backpath[i],backpath[i+1]) for i in range(len(backpath)-1)]:
            if not directedgraph.has_edge(edge[0],edge[1]):
                edges.remove(edge)
            else:
                logger.error("The barckard edge not found: {0}".format(edge))
                sys.exit(1)
    for edge in edges:
        if not directedgraph.has_edge(edge[0],edge[1]):
            logger.error("This must be forward edge: {0}".format(edge))
            sys.exit(1)
    if not are_cycles_same(directedgraph, cycle, vertices):
        logger.error("Mismatch: original {0} vs processed {1}".format(cycle, vertices))
        sys.exit(1)
        
    logger.debug("test_add_backard_paths: Done")


def traversed_homodromic_cycle(spaceicegraph, polarized, vertex, axis, debug=False, draw=None):
    """
    set True to debug when you want to "make test"
    """
    logger = logging.getLogger()
    if axis not in (1,2,3,-1,-2,-3):
        logger.error("Illegal axis: {0}".format(axis))
        sys.exit(1)
    logger.debug("isZ4: {0}".format(polarized.isZ4()))
    logger.debug("defects: {0}".format(polarized.defects()))
    #Make a "string" connecting between the ceiling and the floor.
    untraversed = polarized.all_untraversed_shortest_cycles(vertex, axis, MaxTrials=10)
    #make it homodromic.
    cycle = next(untraversed)
    if cycle is None:
        logger.debug("No candids.")
        return None
    logger.debug("One short cycle: {0}".format(cycle))
    if draw is not None:
        print("r 0.02")
        print(draw.draw_cell(), end="")
        print(draw.draw_path(cycle), end="")
    #test
    if debug:
        test_all_backward_paths(spaceicegraph,cycle)
    detours = []
    for backpath, interv in all_backward_paths(spaceicegraph,cycle):
        if len(backpath) == 0:
            #No backward edges
            detours.append(([],[],interv))
            continue
        first = backpath[0]
        last  = backpath[-1]
        rev   = list(reversed(backpath))
        #find a bypass
        bestbypass = None
        for bypass in networkx.all_shortest_paths(spaceicegraph,source=first,target=last):
            logger.debug("A homodromic path from {0} to {1}: {2}".format(first,last,bypass))
            cyc = bypass[0:len(bypass)-1] + rev
            dip = spaceicegraph.dipole_of_a_cycle(cyc)
            logger.debug("A homodromic cycle: {0}; dipole {1}".format(cyc, dip))
            # we do not want the alternative path spans the cell, so dip should be zero.
            if np.dot(dip,dip) < 0.1:
                bestbypass = bypass
                break
        if bestbypass is None:
            #no harvest
            logger.info("No harvest.".format(detours))
            return None
        detours.append((backpath, bestbypass, interv))
    logger.debug("Found detours to make the cycle homodromic: {0}".format(detours))
    #Harvest check
    #rebuild the cycles
    original = []
    homodromized = []
    for from_,to_,interv in detours:
        original += from_ + interv
        homodromized += to_ + interv
    if not are_cycles_same(spaceicegraph, cycle, original):
        logger.error("Wrong division of the cycle: {0} vs {1}".format(cycle,origina))
        sys.exit(1)
    if homodromized[-1] != homodromized[0]:
        homodromized.append(homodromized[0])
    if not spaceicegraph.is_homodromic(homodromized):
        logger.error("The homodromized path is not homodromic: {0}".format(homodromized))
        sys.exit(1)
    #if the cycle contains two identical edges:
    edges = [(homodromized[i], homodromized[i+1]) for i in range(len(homodromized)-1)]
    if len(edges) != len(set(edges)):
        logger.debug("The cycle is entangled.")
        #no harvest
        logger.info("No harvest.".format(detours))
        return None
    logger.info("Dipole of the harvest: {0}".format(spaceicegraph.dipole_of_a_cycle(homodromized)))
    print(draw.draw_path(homodromized))
    return homodromized

        
def depolarize(spaceicegraph, debug=False, coord=None, cell=None):
    """
    set True to debug when you want to "make test"
    """
    draw = None
    if coord is not None:
        draw = YaplotDraw(coord,cell,data=spaceicegraph)
    logger = logging.getLogger()
    polarized = dict()
    for axis in (+spaceicegraph.XAXIS, +spaceicegraph.YAXIS, +spaceicegraph.ZAXIS,
                 -spaceicegraph.XAXIS, -spaceicegraph.YAXIS, -spaceicegraph.ZAXIS):
        polarized[axis] = SpaceIceGraph(spaceicegraph)
        polarized[axis].polarize(axis)
    while True:
        net_polar = spaceicegraph.net_polarization()
        logger.info("Net polarization: {0}".format(net_polar))
        if np.dot(net_polar, net_polar) < 0.1:
            break
        if net_polar[0] > 0.5:
            logger.debug("Depolarize +X")
            axis = spaceicegraph.XAXIS
        elif net_polar[0] < -0.5:
            logger.debug("Depolarize -X")
            axis = -spaceicegraph.XAXIS
        elif net_polar[1] > 0.5:
            logger.debug("Depolarize +Y")
            axis = spaceicegraph.YAXIS
        elif net_polar[1] < -0.5:
            logger.debug("Depolarize -Y")
            axis = -spaceicegraph.YAXIS
        elif net_polar[2] > 0.5:
            logger.debug("Depolarize +Z")
            axis = spaceicegraph.ZAXIS
        elif net_polar[2] < -0.5:
            logger.debug("Depolarize -Z")
            axis = -spaceicegraph.ZAXIS
        vertex = random.randint(0,spaceicegraph.number_of_nodes()-1)
        logger.debug("Axis: {0} {1}".format(axis,polarized[axis]))
        cycle = traversed_homodromic_cycle(spaceicegraph, polarized[axis], vertex, axis, debug, draw=draw)
        logger.debug("----------------------")
        if cycle is not None:
            logger.debug("The cycle: {0}".format(cycle))
            spaceicegraph.invert_path(cycle)
