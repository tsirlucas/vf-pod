# -*- coding: utf-8 -*-
from factories.red_black_data_factory import RedBlackDataFactory
from classes.red_black.red_black_tree import RedBlackTree


class RedBlackTreeService(object):
    @staticmethod
    def build(nodes):
        tree = RedBlackTree(nodes)
        return tree

    @staticmethod
    def print_tree(tree):
        tree.display(tree.root)
        #criar display na classe red_black_tree.

    @staticmethod
    def generate_and_print():
        nodes = RedBlackDataFactory.get_tree_data()
        tree = RedBlackTreeService.build(nodes)
        RedBlackTreeService.print_tree(tree)
        RedBlackTreeService.export_tree(tree)

    @staticmethod
    def export_tree(tree):
        nodes = tree.get_ordered_nodes(tree)
        RedBlackDataFactory.export_tree(nodes)
        #criar o get_ordered_nodes, criar a funcao na arvore, para retornar o no ordenado.
