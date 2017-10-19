#!python3


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))


class LinkedList(object):
    # Worst case: linear time, O(n)
    # Best case: constant time, O(1)
    def __init__(self, iterable=None):
        """Initialize this linked list; append the given items, if any"""
        self.head = None           # O(1)
        self.tail = None           # O(1)
        self.num_nodes = 0         # O(1)
        if iterable:               # O(1)
            for item in iterable:  # O(n)
                self.append(item)  # O(1)

    # In all cases, constant time O(1)
    def __repr__(self):
        """Return a string representation of this linked list"""
        return 'LinkedList({})'.format(self.items())

    # Worst case: linear time, O(n)
    # Best case: constant time, O(1)
    def items(self):
        """Return a list of all items in this linked list"""
        result = []                      # O(1)
        current = self.head              # O(1)
        while current is not None:       # O(n)
            result.append(current.data)  # O(1)
            current = current.next       # O(1)
        return result                    # O(1)

    # In all cases: constant time, O(1)
    def is_empty(self):
        """Return True if this linked list is empty, or False"""
        return self.num_nodes == 0  # O(1 + 1)

    # In all cases: constant time, O(1)
    def length(self):
        """Return the length of this linked list by returning number of nodes"""
        return self.num_nodes  # O(1)

    # In all cases: constant time, O(1)
    def append(self, item):
        """Insert the given item at the tail of this linked list"""
        node = Node(item)              # O(1)

        if self.num_nodes == 0:        # O(1)
            self.head = node           # O(1)
        else:
            self.tail.next = node      # O(1)
            node.previous = self.tail  # O(1)

        self.tail = node               # O(1)
        self.num_nodes += 1            # O(1)

    # In all cases: constant time, O(1)
    def prepend(self, item):
        """Insert the given item at the head of this linked list"""
        node = Node(item)              # O(1)
        if self.num_nodes:             # O(1)
            self.tail = node           # O(1)
        else:
            node.next = self.head      # O(1)
            self.head.previous = node  # O(1)
        self.head = node               # O(1)

    # Worst case: linear time, O(n)
    # Best case: constant time, O(1)
    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError"""
        current_node = self._find_node(item)                         # Best: O(1), Worst: O(n)
        if current_node is None:                                     # O(1)
            raise ValueError('{0} does not contain {1}'.format(self.__class__.__name__, item))

        if current_node == self.head and current_node == self.tail:  # O(1 + 1)
            self.head = None                                         # O(1)
            self.tail = None                                         # O(1)
        elif current_node == self.head:                              # O(1)
            self.head = current_node.next                            # O(1)
            self.head.previous = None                                # O(1)
        elif current_node == self.tail:                              # O(1)
            previous_node = current_node.previous                    # O(1)
            previous_node.next = None                                # O(1)
            self.tail = previous_node                                # O(1)
        else:
            previous_node = current_node.previous                    # O(1)
            previous_node.next = current_node.next                   # O(1)

    # In all cases: Quadratic time, O(n^2)
    def find(self, quality):
        """Return an item from this linked list satisfying the given quality"""
        for item in self.items():  # O(n * n)
            if quality(item):      # O(1)
                return item        # O(1)

    # Worst case: linear time, O(n)
    # Best case: constant time, O(1)
    def replace(self, item, new_item):
        node = self._find_node(item)  # Best: O(1), Worst: O(n)
        node.data = new_item          # O(1)

    # Worst case: linear time, O(n)
    # Best case: constant time, O(1)
    def _find_node(self, item):
        """Returns the first node it encounters where data is equal to item"""
        current_node = self.head              # O(1)
        while current_node is not None:       # O(n)
            if current_node.data == item:     # O(1)
                return current_node           # O(1)
            current_node = current_node.next  # O(1)
