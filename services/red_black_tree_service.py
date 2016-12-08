from factories.red_black_data_factory import RedBlackDataFactory
from classes.red_black.red_black_tree import RedBlackTree


class RedBlackTreeService(object):
    @staticmethod
    def build(nodes):
        tree = RedBlackTree(nodes)
        return tree

    @staticmethod
    def print_tree(tree):
        tree.display()

    @staticmethod
    def generate_and_print():
        nodes = RedBlackDataFactory.get_tree_data()
        tree = RedBlackTreeService.build(nodes)
        RedBlackTreeService.print_tree(tree)

    @staticmethod
    def export_tree(tree):
        nodes = tree.get_ordered_nodes()
        RedBlackDataFactory.export_tree(nodes)
