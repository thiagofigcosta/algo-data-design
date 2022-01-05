import unittest

import algo_data_design.problems
from algo_data_design.data_structures import Stack

test = unittest.TestCase()


def info():
    if algo_data_design.problems.NO_INFO:
        return
    print("Matching parenthesis")
    print("For a given string input containing the chars `(` and `)` return:")
    print("\t True - If there is a closing parenthesis after every open parenthesis")
    print("\t False - Otherwise")
    print("Examples:")
    print("\t`)())` -> False")
    print("\t`(()()(((())())))` -> True")


def run(parenthesis_sequence):
    # Time complexity: O(n)
    # Space complexity: O(n)
    stack = Stack()
    for char in parenthesis_sequence:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                return False
        else:
            raise ValueError('Bad input')
    return len(stack) == 0


def main():
    info()
    test.assertFalse(run(')())'))
    test.assertTrue(run('(()()(((())())))'))
    if not algo_data_design.problems.NO_INFO:
        print('All tests passed')


if __name__ == "__main__":
    main()
