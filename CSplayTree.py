class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key  # int or string
        self.value = val  # int or string
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

        self.root=None

    def root(self):
        return self.root

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

    def find(self,key):

        self.root=self.splaying(self.root,key)

        if self.root.key==key:
            return self.root.value

        return None

    def remove(self,key):

        if not self.root:
            print("empty tree")
            return

        self.root=self.splaying(self.root,key)

        if self.root.key!=key:
            return

        else:  # then we should delete the root

            # the traditional BST deletion is to swap with its inorder predecessor and delete recursively.

            if self.root.left==None:
                self.root=self.root.right

            else: # since now, every thing in the left subtree is smaller than key, everything right subtree larger.
                righttree=self.root.right
                # splaying up the largest element (closest to key) in the left subtree
                self.root=self.splaying(self.root.left,key)  # its right must be empty
                self.root.right=righttree

    def splaying(self,node,key):
        if not node:
            return None
        if key == node.key:
            return node
        if key < node.key:
            if node.left == None:
                return node
            if key < node.left.key:
                node.left.left = self.splaying(node.left.left,key) # this is a grand parent situation now
                node = self.rotateRight(node)
            elif key > node.left.key:
                node.left.right=self.splaying(node.left.right,key)
                if node.left.right:
                    node.left=self.rotateLeft(node.left)
            if node.left:
                return self.rotateRight(node)
            return node
        elif key>node.key:
            if node.right==None:
                return node
            if key<node.right.key:
                node.right.left = self.splaying(node.right.left,key)
                if node.right.left:
                    node.right = self.rotateRight(node.right)
            elif key>node.right.key:
                node.right.right = self.splaying(node.right.right,key)
                node = self.rotateLeft(node)
            if node.right:
                return self.rotateLeft(node)
            return node


    def rotateLeft(self,x):
        y = x.right
        x.right = y.left
        y.left = x
        return y

    def rotateRight(self,x):
        y = x.left
        x.left = y.right
        y.right = x
        return y

    def preorder(self, node):
        if node is not None:
            print(node.key)
            self.preorder(node.left)
            self.preorder(node.right)


# splayTree=SplayTree()

# splayTree[12] = 12
# splayTree[10] = 10
# splayTree[1] = 1
# splayTree[3] = 3
# splayTree[5] = 5
# splayTree[100] = 100

# splayTree.preorder(splayTree.root)
# print("\n")

# print(splayTree.find(100))
# print("\n")

# splayTree.preorder(splayTree.root)
# print("\n")
# for x in splayTree.keys():
#     print(x)