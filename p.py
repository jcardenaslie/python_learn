class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key  # int or string
        self.val = val  # int or string
        self.left = left  # TreeNode
        self.right = right  # TreeNode
        self.parent = parent  # TreeNode

    def hasLeft(self):
        return self.left

    def hasRight(self):
        return self.right

    def isLeft(self):
        return self.parent and self.parent.left == self

    def isRight(self):
        return self.parent and self.parent.right == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.right or self.left)

    def hasAnyChildren(self):
        return self.right or self.left

    def hasBothChildren(self):
        return self.right and self.left

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.val = value
        self.left = lc
        self.right = rc
        if self.hasLeft():
            self.left.parent = self
        if self.hasRight():
            self.right.parent = self


class SplayTree:
    def __init__(self):
        self.root = None

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeft():
                self._put(key, val, currentNode.left)
            else:
                currentNode.left = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRight():
                self._put(key, val, currentNode.right)
            else:
                currentNode.right = TreeNode(key, val, parent=currentNode)

    def __setitem__(self, key, val):
        self.put(key, val)

    def root(self):
        return self.root

    def preorder(self, node):
        if node is not None:
            print(node.key)
            self.preorder(node.left)
            self.preorder(node.right)

    def search(self, root, key):
        return self.splay(root, key)

    def splay(self, root, key):
        if root == None or root.key == key: return root
        if root.key > key:
            if root.left == None: return root
            if root.left.key > key:
                root.left.left = self.splay(root.left.left, key)
                root = self.right_rotation(root)
            elif root.left.key < key:
                root.left.right = self.splay(root.left.right, key)
                if root.left.right != None:
                    root.left = self.left_rotation(root.left)
            if root.left:
            	return self.right_rotation(root)
            return root
        else:
            if root.right == None: return root
            if root.right.key > key:
                root.right.left = self.splay(root.right.left, key)
                if root.right.left != None:
                    root.right = self.right_rotation(root.right)
            elif root.right.key < key:
                root.right.right = self.splay(root.right.right, key)
                root = self.left_rotation(root)
            if root.right:
            	return self.left_rotation(root)
            return root

    def right_rotation(self, x):
        y = x.left
        x.left = y.right
        y.right = x
        return y

    def left_rotation(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        return y


mytree = SplayTree()
mytree[6] = 1
mytree[7] = 7
mytree[3] = 3
mytree[5] = 5
mytree[4] = 4
mytree[1] = 4



mytree.preorder(mytree.root)
print("\n")

val = mytree.search(mytree.root, 5).val
print("val: {}".format(val))

mytree.preorder(mytree.root)

