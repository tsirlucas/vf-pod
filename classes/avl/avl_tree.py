from classes.avl.avl_node import Node


output_debug = False


def debug(msg):
    if output_debug:
        print msg


class AvlTree:
    def __init__(self, *args):
        self.node = None
        self.height = -1
        self.balance = 0

        if len(args) == 1:
            for i in args[0]:
                self.insert(i)

    def height(self):
        if self.node:
            return self.node.height
        else:
            return 0

    def is_leaf(self):
        return self.height == 0

    def insert(self, node):
        tree = self.node

        new_node = Node(node.name, node.age, node.course)

        if tree is None:
            self.node = new_node
            self.node.left = AvlTree()
            self.node.right = AvlTree()
            debug("Inserted name [" + str(node.name) + "]")

        elif node.name < tree.name:
            self.node.left.insert(node)

        elif node.name > tree.name:
            self.node.right.insert(node)

        else:
            debug("name [" + str(node.name) + "] already in tree.")

        self.rebalance()

    def rebalance(self):
        '''
        Rebalance a particular (sub)tree
        '''
        # name inserted. Let's check if we're balanced
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.lrotate()  # we're in case II
                    self.update_heights()
                    self.update_balances()
                self.rrotate()
                self.update_heights()
                self.update_balances()

            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.rrotate()  # we're in case III
                    self.update_heights()
                    self.update_balances()
                self.lrotate()
                self.update_heights()
                self.update_balances()

    def rrotate(self):
        # Rotate left pivoting on self
        debug('Rotating ' + str(self.node.name) + ' right')
        A = self.node
        B = self.node.left.node
        T = B.right.node

        self.node = B
        B.right.node = A
        A.left.node = T

    def lrotate(self):
        # Rotate left pivoting on self
        debug('Rotating ' + str(self.node.name) + ' left')
        A = self.node
        B = self.node.right.node
        T = B.left.node

        self.node = B
        B.left.node = A
        A.right.node = T

    def update_heights(self, recurse=True):
        if self.node is not None:
            if recurse:
                if self.node.left is not None:
                    self.node.left.update_heights()
                if self.node.right is not None:
                    self.node.right.update_heights()

            self.height = max(self.node.left.height,
                              self.node.right.height) + 1
        else:
            self.height = -1

    def update_balances(self, recurse=True):
        if self.node is not None:
            if recurse:
                if self.node.left is not None:
                    self.node.left.update_balances()
                if self.node.right is not None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def logical_predecessor(self, node):
        '''
        Find the biggest valued node in LEFT child
        '''
        node = node.left.node
        if node is not None:
            while node.right is not None:
                if node.right.node is None:
                    return node
                else:
                    node = node.right.node
        return node

    def logical_successor(self, node):
        '''
        Find the smallese valued node in RIGHT child
        '''
        node = node.right.node
        if node is not None:  # just a sanity check

            while node.left is not None:
                debug("LS: traversing: " + str(node.name))
                if node.left.node is None:
                    return node
                else:
                    node = node.left.node
        return node

    def check_balanced(self):
        if self is None or self.node is None:
            return True

        # We always need to make sure we are balanced 
        self.update_heights()
        self.update_balances()
        return (abs(self.balance) < 2) and self.node.left.check_balanced() and self.node.right.check_balanced()

    def inorder_traverse(self):
        if self.node is None:
            return []

        inlist = []
        l = self.node.left.inorder_traverse()
        for i in l:
            inlist.append(i)

        inlist.append(self.node.name)

        l = self.node.right.inorder_traverse()
        for i in l:
            inlist.append(i)

        return inlist

    def set_ordered_nodes(self, nodes):
        if self.node is not None:
            if self.node.left is not None:
                self.node.left.set_ordered_nodes(nodes)
            nodes.append(self.node)
            if self.node.right is not None:
                self.node.right.set_ordered_nodes(nodes)
        return nodes

    def get_ordered_nodes(self):
        nodes = []
        self.update_heights()
        self.update_balances()
        return self.set_ordered_nodes(nodes)

    def display(self, level=0, pref=''):
        '''
        Display the whole tree. Uses recursive def.
        '''
        self.update_heights()  # Must update heights before balances 
        self.update_balances()
        if self.node is not None:
            print '-' * level * 3, pref, self.node.name, "[" + str(self.height) + ":" + str(
                self.balance) + "]", 'L' if self.is_leaf() else ' '
            if self.node.left is not None:
                self.node.left.display(level + 1, '<')
            if self.node.left is not None:
                self.node.right.display(level + 1, '>')
