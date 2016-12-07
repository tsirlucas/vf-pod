from classes.avl.avl_node import Node


output_debug = False


def debug(msg):
    if output_debug:
        print msg


class BinaryTree:
    def __init__(self, *args):
        self.node = None
        self.height = -1

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
            self.node.left = BinaryTree()
            self.node.right = BinaryTree()
            debug("Inserted name [" + str(node.name) + "]")

        elif node.name < tree.name:
            self.node.left.insert(node)

        elif node.name > tree.name:
            self.node.right.insert(node)

        else:
            debug("name [" + str(node.name) + "] already in tree.")

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
        return self.set_ordered_nodes(nodes)

    def display(self, level=0, pref=''):
        '''
        Display the whole tree. Uses recursive def.
        '''
        self.update_heights()  # Must update heights before print
        if self.node is not None:
            print '-' * level * 3, pref, self.node.name, "[" + str(self.height) + "]", \
                'L' if self.is_leaf() else ' '
            if self.node.left is not None:
                self.node.left.display(level + 1, '<')
            if self.node.left is not None:
                self.node.right.display(level + 1, '>')
