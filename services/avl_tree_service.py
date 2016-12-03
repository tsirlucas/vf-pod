import factories.avl_data_factory as AvlTreeFactory
from classes.avl.avl_tree import AVLTree


def build(nodes):
    tree = AVLTree(nodes)
    return tree


def print_tree(tree):
    tree.display()


def generate_and_print():
    nodes = AvlTreeFactory.get_tree_data()
    tree = build(nodes)
    print_tree(tree)
