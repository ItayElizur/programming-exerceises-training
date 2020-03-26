"""
problem formalization:

You are given 2 arrays:
1. A, N-sized integers array.
2. B, N-sized binary array.
The values of A are constant, but ou are allowed to change the values of B by performing a double_bit_switch (DBS):
In a double_bit_switch, you choose two adjacent bit in B and perform NOT operation on both of them (reminder: NOT(0)
 = 1, NOT(1) = 0).
 You can use the the double_bit_switch operation as many times as you want.

Create an EFFICIENT algorithm to find the maximum value of dot product that can be achieved by performing the DBS
operation over B.

-----------------------------------------------------------------------------------------------------------------------

Example:

input: A = [-8, 12, 27, 4, 13, -8, 6], B = [1, 0, 1, 1, 0, 0, 1]
output: 58

-----------------------------------------------------------------------------------------------------------------------

Limitations:

time - 0.5 seconds
space - no limitation

-----------------------------------------------------------------------------------------------------------------------

Testing:

After implementing your solution, test it with out given input by 'CheckSolution' file.
You have a total of 6 test:
- tests 1-4 are visible to you, and you can access it's input using 'get_input' method from utils.Test.
- test 4-6 is not visible to you, and need to pass it without knowing the input.
It is assured to you that all input is legal and fits the solution signature.

-----------------------------------------------------------------------------------------------------------------------

Documentation:

After passing all tests, write a doc in Confluence describing your solution.
In the doc, analyze the runtime of the algorithm you used.

"""

from typing import List


def double_bit_switch_solution(a: List[int], b: List[bool]) -> int:
    """ Decides which items to take, by maximizing the total value of them

    :param a: list of integers
    :param b: list of booleans
    :return: maximal possible dot-product value that can be obtained by performing DBSs.
    """
    pass
