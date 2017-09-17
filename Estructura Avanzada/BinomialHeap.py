import sys

class BinomialHeapNode:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.degree = 0
        self.child = None
        self.sibling = None

class BinomialHeap:
    def __init__(self):
        self.head = None

def make_heap():
    return BinomialHeap()

def make_node(key):
    return BinomialHeapNode(key)

def minimum(H):
    y = H.head
    if y != None:
        min = y.key
        x = y.sibling
        while x != None:
            if x.key < min:
                min = x.key
                y = x
            x = x.sibling
    return y



def __link(x, y):
    x.sibling = y.child
    x.parent = y
    y.child = x
    y.degree = y.degree + 1

def __merge(Hx, Hy):

    class SiblingWrapper:
        sibling = None
    x = Hx.head
    y = Hy.head
    h = SiblingWrapper() # head
    t = h        # tail
    while x != None and y != None:
        if x.degree <= y.degree:
            t.sibling = x
            t = x
            x = x.sibling
        else:
            t.sibling = y
            t = y
            y = y.sibling
    if x != None:
        t.sibling = x
    else:
        t.sibling = y
    return h.sibling

def __union(H1, H2):
    H = BinomialHeap()
    H.head = __merge(H1, H2)
    if H.head == None:
        return H
    w = None
    x = H.head
    while x.sibling != None:
        if x.degree != x.sibling.degree or (x.sibling.sibling != None and x.sibling.sibling.degree == x.degree):
            w = x
            x = x.sibling
        else:
            if x.key <= x.sibling.key:
                y = x.sibling
                z = y.sibling
                x.sibling = z
                __link(y, x)
            else:
                y = x.sibling
                if w != None:
                    w.sibling = y
                else:
                    H.head = y
                __link(x, y)
                x = y
    return H

def __print_siblings(x):
    while x != None:
        print (x.degree),
        x = x.sibling
    print

def insert(H, x):
    S = BinomialHeap()
    S.head = x
    T = __union(H, S)
    H.head = T.head

def print_heap(x, indent='#', char='#'):
    while x != None:
        print (indent, x.key, x.degree)
        if x.child != None:
            print_heap(x.child, indent+char, char)
        x = x.sibling
'''
#data = [31,40,50,37,45,60,65,73,23,76]
#data = [10,20,30,40,50,60,70,80,90]
data = [30,10,90,80,60,70,20,50,40]
#data = [3,3,2,1,8,3,7]

print ("Input data:", data)

print

min = None
max = None
nodes = []
H = BinomialHeap()
for d in data:
    print ("---------------------------------------- insert (%2d) ---"%(d))
    n = BinomialHeapNode(d)
    if min == None or n.key < min.key:
        min = n
    if max == None or n.key > max.key:
        max = n
    nodes.append(n)
    insert(H, n)
    print_heap(H.head, 'o', '->')

print ("min.key = %d, max.key = %d" % (min.key, max.key))

print
'''