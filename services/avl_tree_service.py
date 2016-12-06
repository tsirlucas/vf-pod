from factories.avl_data_factory import AvlDataFactory
from classes.avl.avl_tree import AVLTree


class AvlTreeService(object):

    @staticmethod
    def __build__(nodes):
        tree = AVLTree(nodes)
        return tree

    @staticmethod
    def __print_tree__(tree):
        tree.display()

    @staticmethod
    def generate_and_print():
        nodes = AvlDataFactory.get_tree_data()
        tree = AvlTreeService.__build__(nodes)
        AvlTreeService.__print_tree__(tree)
