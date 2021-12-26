import unittest

import algo_data_design.problems
from algo_data_design.utils import input as u_input

test = unittest.TestCase()


def info():
    print("Climbing stairs")
    print("If you have to climb n steps of a stair, and you could climb one or two steps at the time,")
    print("in how many ways you could climb it?")
    print('\t1 -> 1')
    print('\t2 -> 2')
    print('\t3 -> 3')
    print('\t5 -> 8')


def run_sub_optimal(n):  # exactly like nth fibonacci
    # Time complexity: O(2^n)
    # Space complexity: O(n)
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    return run_sub_optimal(n - 1) + run_sub_optimal(n - 2)


def run_optimal(n):  # exactly like nth fibonacci
    # Time complexity: O(n)
    # Space complexity: O(n)
    stairs = [0, 1, 2]
    for i in range(3, n + 1, 1):
        stairs.append(stairs[i - 1] + stairs[i - 2])
    return stairs[n]


def main():
    if algo_data_design.problems.NO_PROMPT:
        optimal = True
    else:
        print('Run optimal solution? {y,n}')
        optimal = u_input.input_boolean()
    if optimal:
        run = run_optimal
    else:
        run = run_sub_optimal
    info()
    test.assertEqual(1, run(1))
    test.assertEqual(2, run(2))
    test.assertEqual(3, run(3))
    test.assertEqual(8, run(5))
    test.assertEqual(1836311903, run(45))
    print('All tests passed')


if __name__ == "__main__":
    main()
