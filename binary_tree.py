from tree import Tree
# abstract base class representing a binary structure
class BinaryTree(Tree):

    def left(self, p):
        # returns a position representing p's left side
        raise NotImplementedError("Must be implemented by sub-class")

    def right(self, p):
        # return a position rep p's right side
        raise NotImplementedError("Must be implemented by sub-class")

    def sibling(self, p):
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        elif self.right(p) is not None:
            yield self.right(p)

