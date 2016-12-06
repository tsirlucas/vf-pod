from factories.binary_data_factory import BinaryDataFactory
from classes.binary.binary_tree import BinaryTree


class BinaryTreeService(object):

    @staticmethod
    def build(nodes):
        tree = BinaryTree(nodes)
        return tree

    @staticmethod
    def print_tree(tree):
        tree.display()

    @staticmethod
    def generate_and_print():
        nodes = BinaryDataFactory.get_tree_data()
        tree = BinaryTreeService.build(nodes)
        BinaryTreeService.print_tree(tree)
