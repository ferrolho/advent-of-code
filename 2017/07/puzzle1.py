#!/usr/bin/python3

import sys


class Node:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.children = []
        self.parent = None

    def __str__(self):
        return self.name + ' ' + str(self.weight) + ': ' + ', '.join(self.children)


def main():
    # A map of all the nodes indexed by their names.
    nameToNode = {}

    for line in sys.stdin:
        tokens = line.strip().split('->')

        name, weightRaw = tokens[0].split()
        weight = int(weightRaw[weightRaw.index('(') + 1:weightRaw.rindex(')')])

        nameToNode[name] = Node(name, weight)

        if len(tokens) == 2:
            children = [x.strip() for x in tokens[1].split(',')]
            nameToNode[name].children = children

    # At this point we have a map with all the existing nodes,
    # but the only existing relationship is from parent to child.

    # This loop assigns a parent to every node but the root.
    for name in nameToNode:
        for child in nameToNode[name].children:
            nameToNode[child].parent = name

    root = ''

    # Find the node with no parent, i.e. the root.
    for name in nameToNode:
        if nameToNode[name].parent is None:
            root = name
            break

    print(root)


if __name__ == '__main__':
    main()
