class Tree:
    # abstract base class representing a tree structure
    class Position: # nested position class
        # an abstraction respresenting a location of a single element
        def element(self):
            # returns the element stored at the position
            raise NotImplementedError("Must be implemented by sub-class")

        def __eq__(self, other):
            # returns true if other position represents the same location
            raise NotImplementedError("Must be implemented by sub-class")

        def __ne__(self, other):
            # returns true if other position doesnot represents the same location
            return not (self == other)

    # abstract methods that concretes subclasses must support
    def root(self):
        # returns position respresenting the tree's root or none if it empty
        raise NotImplementedError("Must be implemented by sub-class")

    def parent(self, p):
        # returns position respresenting the position's parent or none if it empty
        raise NotImplementedError("Must be implemented by sub-class")

    def num_children(self, p):
        # returns the number of children the position p has or none if it empty
        raise NotImplementedError("Must be implemented by sub-class")

    def children(self, p):
        # generates the iteration of children of that position
        raise NotImplementedError("Must be implemented by sub-class")

    def __len__(self):
        # return the total number of elements in the tree
        raise NotImplementedError("Must be implemented by sub-class")

    # concrete methods implemented in this class
    def is_root(self, p):
        # returns true if position p represents the root of the tree
        return self.root() == p

    def is_leaf(self, p):
        # returns true if the position p doesnot have any children
        return self.num_children(p) == 0

    def is_empty(self):
        # returns true if the tree is empty
        return self.__len__() == 0







    def _depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1+self._depth(self.parent(p))

    def _height(self, p):
        if self.is_leaf(p):
            return 0
        else:
            return 1+max(self._height(i) for i in self.children(p))









