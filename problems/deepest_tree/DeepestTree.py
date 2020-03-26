"""
problem formalization:

you are given a tree with N nodes and N-1 edges. Nodes are numbered from 0 (source) to N-1.
You are allowed to 'rotate' the tree by defining any of it's nodes as the root. Find the depth of the deepest tree that
can be achieved with such rotation.

Create an EFFICIENT algorithm to perform the given task.

-----------------------------------------------------------------------------------------------------------------------

Example:

input: shown in tree.jpg
output: 5

(the process of rotation/root changing is shown in rotated_tree.jpg)

-----------------------------------------------------------------------------------------------------------------------

Limitations:

time - 2.5 seconds
space - no limitation

-----------------------------------------------------------------------------------------------------------------------

Testing:

After implementing your solution, test it with out given input by 'CheckSolution' file.
You have a total of 7 test:
- tests 1-4 are visible to you, and you can access it's input using 'get_input' method from utils.Test.
- tests 5-7 are not visible to you, and need to pass them without knowing the input.
It is assured to you that all input is legal and fits the solution signature.

-----------------------------------------------------------------------------------------------------------------------

Documentation:

After passing all tests, write a doc in Confluence describing your solution.
In the doc, analyze the runtime of the algorithm you used.

"""

import networkx as nx


def deepest_tree_solution(path_to_tree: str) -> int:
    """ Find the depth of the deepest tree that can be achieved by rotations

    :param path_to_tree: path to the pickle file with the tree input
    :return: depth of the deepest tree that can be achieved by rotations
    """
    t = nx.read_gpickle(path_to_tree)
    pass
