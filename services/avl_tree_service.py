from factories.avl_data_factory import AvlDataFactory
from classes.avl.avl_tree import AvlTree


class AvlTreeService(object):

    @staticmethod
    def build(nodes):
        tree = AvlTree(nodes)
        return tree

    @staticmethod
    def print_tree(tree):
        tree.display()

    @staticmethod
    def generate_and_print():
        nodes = AvlDataFactory.get_tree_data()
        tree = AvlTreeService.build(nodes)
        AvlTreeService.print_tree(tree)
