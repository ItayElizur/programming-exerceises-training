"""
Here you test your code performances.

We created several inputs to test your solution. Some of them are visible to you for debugging, and some are not.
the given inputs test your solution under time and space limitations - as describes in the problem file.

Good luck!
"""

from utils.Test import test

# Import your solution here
from problems.string_chain.StringChainSolved import string_chain_solution as solution

# Set current problem name (lowercase with spaces)
NAME = 'string chain'

if __name__ == '__main__':
    # Fill relevant details
    test(problem_name=NAME, idx=6, solution=solution)
