import math

INF = int(2e9)


class SegmentTreeNode:
    def __init__(self, l, r, v=INF):
        self.left = l
        self.right = r
        self.value = v

    def merge(self, left, right):
        if left is not None and right is not None:
            self.value = min(left.value, right.value)
        elif left is None and right is None:
            self.value = INF
        elif left is None:
            self.value = right.value
        else:
            self.value = left.value


class SegmentTree:
    def __init__(self, a):
        n = len(a)
        power = math.ceil(math.log(n, 2))
        total = 2 ** (power + 1)
        self.__tree = [None] * int(total)
        self.__leaf_length = int(total/2)-1
        self.__build(1, 0, self.__leaf_length, a)

    def __build(self, node, l, r, a):
        if l == r:
            self.__tree[node] = SegmentTreeNode(l, r)
            try:
                self.__tree[node].value = a[l]
            except IndexError:
                self.__tree[node].value = INF
            return
        leftchild = 2 * node
        rightchild = leftchild + 1
        mid = (l + r) // 2
        self.__build(leftchild, l, mid, a)
        self.__build(rightchild, mid + 1, r, a)
        self.__tree[node] = SegmentTreeNode(l, r)
        l = self.__tree[leftchild]
        r = self.__tree[rightchild]
        self.__tree[node].merge(l, r)

    def __query(self, node, l, r, i, j):
        if l >= i and r <= j:
            return self.__tree[node]
        elif j < l or i > r:
            return None
        else:
            leftchild = 2 * node
            rightchild = leftchild + 1
            mid = (l + r) // 2
            l = self.__query(leftchild, l, mid, i, j)
            r = self.__query(rightchild, mid + 1, r, i, j)
            if l is not None and r is not None:
                return SegmentTreeNode(-1, -1, min(l.value, r.value))
            elif l is None and r is None:
                return SegmentTreeNode(-1, -1, INF)
            elif l is None:
                return SegmentTreeNode(-1, -1, r.value)
            else:
                return SegmentTreeNode(-1, -1, l.value)

    def query(self, i, j): 
        return self.__query(1, 0, self.__leaf_length, i, j)

    def __update(self, node, l, r, i, v):
        if l == i and r == i:
            self.__tree[node].value = v
        elif i < l or i > r:
            return None
        else:
            leftchild = 2 * node
            rightchild = leftchild + 1
            mid = (l + r) // 2
            self.__update(leftchild, l, mid, i, v)
            self.__update(rightchild, mid + 1, r, i, v)
            l = self.__tree[leftchild]
            r = self.__tree[rightchild]
            self.__tree[node].merge(l, r)

    def update(self, i, value):
        self.__update(1, 0, self.__leaf_length, i, value)

a = [7, 2, 3, 0, 5, 10, 3, 12, 18]
# a = [18, 17, 13, 19, 15, 11, 20]

queries = [[0, 4], [4, 7], [7, 8]]
segment_tree = SegmentTree(a)

for q in queries:
    print(segment_tree.query(q[0], q[1]).value)