class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def set_left(self, node):
        self.left = node
        self.left.parent = self

    def set_right(self, node):
        self.right = node
        self.right.parent = self

    def __repr__(self):
        return f"Node({self.value})"


class BinarySearchTree(object):
    def __init__(self, root):
        self.root = root

    def search(self, x):
        curr = self.root
        while curr is not None:
            if curr.value < x.value:
                curr = curr.right
            elif curr.value > x.value:
                curr = curr.left
            elif curr.value == x.value:
                return True
        return False

    def minimum(self, x):
        curr = x
        while curr.left is not None:
            curr = curr.left
        return curr

    def maximum(self, x):
        curr = x
        while curr.right is not None:
            curr = curr.right
        return curr

    def successor(self, x):
        if x.right is not None:
            return self.minimum(x.right)
        while x.parent is not None:
            if x.parent.left == x:
                break
            x = x.parent
        return x.parent

    def predecessor(self, x):
        if x.left is not None:
            return self.maximum(x.left)
        while x.parent is not None:
            if x.parent.right == x:
                break
            x = x.parent
        return x.parent

    def insertion(self, x):
        curr = self.root
        while curr is not None:
            curr_parent = curr
            if curr.value < x.value:
                curr = curr.right
            elif curr.value >= x.value:
                curr = curr.left

        if curr_parent.value < x.value:
            curr_parent.right = x
        elif curr_parent.value >= x.value:
            curr_parent.left = x


def make_tree():
    tree = Node(15)

    tree.set_left(Node(6))
    tree.left.set_left(Node(3))
    tree.left.set_right(Node(7))
    tree.left.left.set_left(Node(2))
    tree.left.left.set_right(Node(4))
    tree.left.right.set_right(Node(13))
    tree.left.right.right.set_left(Node(9))

    tree.set_right(Node(18))
    tree.right.set_left(Node(17))
    tree.right.set_right(Node(20))
    return tree


def test_search():
    tree = make_tree()
    bst = BinarySearchTree(tree)
    assert bst.search(Node(3))
    assert bst.search(Node(5)) is False


def test_minimum():
    tree = make_tree()
    bst = BinarySearchTree(tree)
    assert bst.minimum(tree).value == 2


def test_maximum():
    tree = make_tree()
    bst = BinarySearchTree(tree)
    assert bst.maximum(tree).value == 20


def test_successor():
    tree = make_tree()
    bst = BinarySearchTree(tree)
    assert bst.successor(tree.left.left).value == 4
    assert bst.successor(tree.left).value == 7
    assert bst.successor(tree.right.right) is None
    assert bst.successor(tree.left.right.right).value == 15


def test_predecessor():
    tree = make_tree()
    bst = BinarySearchTree(tree)
    assert bst.predecessor(tree.left.left).value == 2
    assert bst.predecessor(tree.left).value == 4
    assert bst.predecessor(tree.right.right).value == 18
    assert bst.predecessor(tree.left.right.right).value == 9


def test_insertion():
    tree = make_tree()
    bst = BinarySearchTree(tree)
    bst.insertion(Node(1))
    bst.insertion(Node(14))
    assert tree.left.left.left.left.value == 1
    assert tree.left.right.right.right.value == 14


if __name__ == "__main__":
    test_search()
    test_minimum()
    test_maximum()
    test_successor()
    test_predecessor()
    test_insertion()
