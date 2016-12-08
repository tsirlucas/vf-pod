from classes.red_black.red_black_node import Node


class RedBlackTree(object):

    def __init__(self, create_node=Node):
        self.nil = create_node(name=None)
        self.root = self.nil
        self.create_node = create_node

    def minimum(self, x=None):
        if x is None:
            x = self.root
        while x.left != self.nil:
            x = x.left
        return x

    def maximum(self, x=None):
        if x is None:
            x = self.root
        while x.right != self.nil:
            x = x.right
        return x

    def insert_key(self, name):
        self.insert_node(self.create_node(name=name))

    def insert_node(self, z):
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.name < x.name:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == self.nil:
            self.root = z
        elif z.name < y.name:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        z.red = True
        self.insert_fixup(z)

    def insert_fixup(self, z):
        while z.p.red:
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.red:
                    z.p.red = False
                    y.red = False
                    z.p.p.red = True
                    z = z.p.p
                else:
                    if z == z.p.right:
                        z = z.p
                        self.left_rotate(z)
                    z.p.red = False
                    z.p.p.red = True
                    self.right_rotate(z.p.p)
            else:
                y = z.p.p.left
                if y.red:
                    z.p.red = False
                    y.red = False
                    z.p.p.red = True
                    z = z.p.p
                else:
                    if z == z.p.left:
                        z = z.p
                        self.right_rotate(z)
                    z.p.red = False
                    z.p.p.red = True
                    self.left_rotate(z.p.p)
        self.root.red = False

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.p = x
        y.p = x.p
        if x.p == self.nil:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.nil:
            x.right.p = y
        x.p = y.p
        if y.p == self.nil:
            self.root = x
        elif y == y.p.right:
            y.p.right = x
        else:
            y.p.left = x
        x.right = y
        y.p = x

    def check_invariants(self):
        def is_red_black_node(node):
            if (node.left and not node.right) or (node.right and not node.left):
                return 0, False

            if not node.left and not node.right and node.red:
                return 0, False

            if node.red and node.left and node.right:
                if node.left.red or node.right.red:
                    return 0, False

            if node.left and node.right:

                if self.nil != node.left and node != node.left.p:
                    return 0, False
                if self.nil != node.right and node != node.right.p:
                    return 0, False

                left_counts, left_ok = is_red_black_node(node.left)
                if not left_ok:
                    return 0, False
                right_counts, right_ok = is_red_black_node(node.right)
                if not right_ok:
                    return 0, False

                # check children's counts are ok
                if left_counts != right_counts:
                    return 0, False
                return left_counts, True
            else:
                return 0, True

        num_black, is_ok = is_red_black_node(self.root)
        return is_ok and not self.root.red


def write_tree_as_dot(t, f, show_nil=False):
    def node_id(node):
        return 'N%d' % id(node)

    def node_color(node):
        if node.red:
            return "red"
        else:
            return "black"

    def visit_node(node):
        print >> f, "  %s [label=\"%s\", color=\"%s\"];" % (node_id(node), node, node_color(node))
        if node.left:
            if node.left != t.nil or show_nil:
                visit_node(node.left)
                print >> f, "  %s -> %s ;" % (node_id(node), node_id(node.left))
        if node.right:
            if node.right != t.nil or show_nil:
                visit_node(node.right)
                print >> f, "  %s -> %s ;" % (node_id(node), node_id(node.right))

    print >> f, "// Created by rbtree.write_dot()"
    print >> f, "digraph red_black_tree {"
    visit_node(t.root)
    print >> f, "}"


def test_tree(t, keys):
    assert t.check_invariants()
    for i, key in enumerate(keys):
        for key2 in keys[:i]:
            assert t.nil != t.search(key2)
        for key2 in keys[i:]:
            assert (t.nil == t.search(key2)) ^ (key2 in keys[:i])
        t.insert_key(key)
        assert t.check_invariants()


if '__main__' == __name__:
    import os, sys, numpy.random as R


    def write_tree(t, filename):
        f = open('%s.dot' % filename, 'w')
        write_tree_as_dot(t, f)
        f.close()
        os.system('dot %s.dot -Tsvg -o %s.svg' % (filename, filename))


    R.seed(2)
    size = 50
    keys = R.randint(-50, 50, size=size)
    t = RedBlackTree()
    test_tree(t, keys)
    write_tree(t, 'tree')

