import csv
from classes.avl.avl_node import Node


class AvlDataFactory(object):

    @staticmethod
    def get_tree_data():
        node_array = []
        with open('assets/imports/avl-tree.csv', 'rb') as csv_file:
            tree_reader = csv.reader(csv_file, delimiter=';', quotechar='"', skipinitialspace=True, strict=True)
            for row in tree_reader:
                node_array.append(Node(row[0].decode('utf-8'), row[1].decode('utf-8'), row[2].decode('utf-8')))
            return node_array

    @staticmethod
    def export_tree(nodes):
        with open('assets/exports/avl-tree.csv', 'w') as csv_file:
            tree_writer = csv.writer(csv_file, delimiter=';', quotechar='"', skipinitialspace=True, strict=True)
            for node in nodes:
                tree_writer.writerow([node.name.encode("utf-8"), node.age.encode("utf-8"), node.course.encode("utf-8"), ''])
            print '.csv exportado!'