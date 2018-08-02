# coding: utf-8
#Minimal implementation for genice.
#openjscad-like postmodifier style
"""
cell is in nm

openscad2 comes up with OO style
"""

import numpy as np


def pp(x):
    if type(x) is str:
        return x
    if type(x) is list:
        return x.__str__()
    return np.array2string(x, separator=', ')

class OpenJScad():
    def __init__(self, s="", indent=0):
        self.string = s
        self.indent = indent
    def block(self, head="", seq=[], tail=""):
        ss = "  " * self.indent
        s = ss + head + "\n"
        s += ",\n".join([ ss + "  " + x for x in seq ]) + "\n"
        s += ss + tail
        return s
    def encode(self, *codes): #Stored value as a string
        return "".join([code.__str__() for code in codes])
    
#    def use(self, f):
#        return OpenScad("use <{0}>;\n".format(f))

    def defvar(self, name, value):
        return OpenJScad("{0}={1};\n".format(name,value))

    def translate(self, value):
        return OpenJScad("{3}.translate([{0},{1},{2}])".format(*value, self.string))

    def scale(self, value):
        return OpenJScad("{3}.scale([{0},{1},{2}])".format(*value, self.string))

#    def rotate(self, value):
#        return OpenScad("rotate([{0},{1},{2}]){{\n{3}}} //rotate\n".format(*value, self.string))

    def mirror(self, value):
        return OpenJScad("{3}.mirror([{0},{1},{2}])".format(*value, self.string))

    def add(self, *values):
        el = [value.__str__() for value in values]
        if self.__str__() != "":
            el = [self.__str__()] + el
        return OpenJScad(self.block("union(", el, ")"))

    def union(self, *values):
        return self.add(*values)
    
    def subtract(self, *values):
        el = [value.__str__() for value in values]
        if self.__str__() != "":
            el = [self.__str__()] + el
        return OpenJScad(self.block("difference(", el, ")"))

    def intersect(self, *values):
        el = [value.__str__() for value in values]
        if self.__str__() != "":
            el = [self.__str__()] + el
        return OpenJScad(self.block("intersection(", el, ")"))

    #aliases for backward compat
    def difference(self, *values):
        return self.subtract(*values)
    
    def intersection(self, *values):
        return self.intersect(*values)

    #operators
    def __or__(self, value):
        return self.add(value)
                
    def __and__(self, value):
        return self.intersect(value)
                
    def __sub__(self, value):
        return self.subtract(value)

    #primitives
    def rhomb(self, cell):
        origin = np.zeros(3)
        points = [x+y+z for x in (origin,cell[0]) for y in (origin,cell[1]) for z in (origin,cell[2])]
        s = "polyhedron({points:["
        for point in points:
            s += pp(point) + ",\n"
        s += "],\n"
        faces = [[0,1,3,2],[0,4,5,1],[0,2,6,4],[5,4,6,7],[6,2,3,7],[3,1,5,7]]
        s += "triangles:["
        for face in faces:
            s += pp(face) + ",\n"
        s += "]})"
        return OpenJScad(s)

    def bond(self, s1,s2,r=1.0):
        return OpenJScad("cylinder({{start:{0}, end:{1}, r:{2}}})".format(pp(s1),pp(s2),r))

    def sphere(self, r=1):
        return OpenJScad("sphere(r={0})".format(r))

    def __str__(self):
        return self.string

    def eol(self):
        return self.string + ";"
    
    
def test():
    o = OpenJScad()
    print("function main(){")
    print("return "+o.sphere(r=5).translate([1,2,3]).eol())
    print(o.add(o.sphere(r=2), o.sphere(r=3)).eol())
    print(o.sphere(r=2).add(o.sphere(r=3)).add(o.sphere(r=4)).eol()) #another way
    print((o.sphere(r=2) | o.sphere(r=3) | o.sphere(r=4)).eol()) #another way
    print("}")


def argparser(arg):
    global options
    options={'scale':50, 'rnode':0.07, 'rbond':0.06, 'fn':20}
    if arg != "":
        for a in arg.split(","):
            kw,value = a.split("=")
            if kw in ("scale", "rnode", "rbond", 'fn'):
                options[kw] = float(value)


def hook0(lattice):
    lattice.logger.info("Hook0: Preprocess.")
    for d in range(3):
        lattice.rep[d] += 2  #Extend the size,then cut off later.
    lattice.logger.info("Hook0: end.")

def hook2(lattice):
    global options
    scale = options["scale"]
    rnode = options["rnode"]
    rbond = options["rbond"]
    fn    = options["fn"]
    lattice.logger.info("Hook2: Output water molecules in OpenSCAD format revised.")
    cellmat = lattice.repcell.mat
    rep = np.array(lattice.rep)
    trimbox    = lattice.cell.mat *np.array([(rep[i]-2) for i in range(3)])
    trimoffset = lattice.cell.mat[0]+lattice.cell.mat[1]+lattice.cell.mat[2]
    lattice.logger.info(lattice.repcell.mat)
    lattice.logger.info(lattice.cell.mat)

    margin = 0.2 # expansion relative to the cell size
    lower = (1.0 - margin) / rep
    upper = (rep - 1.0 + margin) / rep

    bonds = []
    if rbond > 0.0:
        for i,j in lattice.graph.edges(data=False):
            s1 =lattice.reppositions[i]
            s2 =lattice.reppositions[j]
            d = s2-s1
            d -= np.floor( d + 0.5 )
            lattice.logger.debug("Len {0}-{1}={2}".format(i,j,np.linalg.norm(d)))
            s2 = s1 + d
            if ( (lower[0] < s1[0] < upper[0] and lower[1] < s1[1] < upper[1] and lower[2] < s1[2] < upper[2] ) or
              (lower[0] < s2[0] < upper[0] and lower[1] < s2[1] < upper[1] and lower[2] < s2[2] < upper[2] ) ):
                bonds.append( (np.dot(s1,cellmat), np.dot(s2,cellmat)))

    nodes = []
    if rnode > 0.0:
        for s1 in lattice.reppositions:
            if lower[0] < s1[0] < upper[0] and lower[1] < s1[1] < upper[1] and lower[2] < s1[2] < upper[2]:
                nodes.append( np.dot(s1, cellmat) )

    o = OpenJScad()
    objs = [o.sphere(r="Rnode").translate(node) for node in nodes] + [o.bond(s1,s2,r="Rbond") for s1,s2 in bonds]
    #operations
    ops = [ #bondfunc,
        o.defvar("$fn", fn),
        o.defvar("Rnode", rnode),
        o.defvar("Rbond", rbond),
        o.defvar("ret", ( o.rhomb(trimbox).translate(trimoffset) & o.union(*objs) ).translate(-trimoffset).scale([scale,scale,scale])) ]
    s = "function main(){\n" + o.encode(*ops) + "\n  return ret;\n}\n"
    s = '//' + "\n//".join(lattice.doc) + "\n" + s
    print(s,end="")
    lattice.logger.info("Hook2: end.")

hooks = {0:hook0, 2:hook2}


if __name__ == "__main__":
    test()