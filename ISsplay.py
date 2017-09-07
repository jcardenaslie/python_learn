class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

def rotate_r(node):
    lnode = node.left
    node.left = lnode.right
    lnode.right = node
    return lnode

def rotate_l(node):
    rnode = node.right
    node.right = rnode.left
    rnode.left = node
    return rnode

wnode = Node(None)

def splay(node, x):
    rnode = wnode   
    lnode = wnode   
    while True:
        if node.data == x: break
        elif x < node.data:

            if node.left is None: break
            if x < node.left.data:

                node = rotate_r(node)
                if node.left is None: break
            rnode.left = node
            rnode = node
            node = node.left
        else:

            if node.right is None: break
            if x > node.right.data:

                node = rotate_l(node)
                if node.right is None: break
            lnode.right = node
            lnode = node
            node = node.right
    rnode.left = node.right
    lnode.right = node.left
    node.left = wnode.right
    node.right = wnode.left
    return node

def insert(node, x):
    if node is None: return Node(x)
    if x == node.data: return node
    new_node = Node(x)
    if x < node.data:
        new_node.right = node
        new_node.left = node.left
        node.left = None
    else:
        new_node.left = node
        new_node.right = node.right
        node.right = None
    return new_node

def search(node, x):
    if node is None: return node, False
    node = splay(node, x)
    return node, node.data == x


class Splaytree:
    def __init__(self):
        self.root = None

    def search(self, x):
        self.root, resultado = search(self.root, x)
        return resultado

    def insert(self, x):
        self.root = insert(self.root, x)