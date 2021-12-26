import unittest

import algo_data_design.problems

test = unittest.TestCase()
from algo_data_design.utils import input as u_input


def info():
    print("Nth Fibonacci number")
    print("The Fibonacci sequence is given by:")
    print("\t F(0) = 0")
    print("\t F(1) = 1")
    print("\t F(n) = F(n-1) + F(n-2)")
    print('Write a program that returns the nth fibonacci number')
    print("Examples:")
    print("\t1 -> 0")
    print("\t2 -> 1")
    print("\t3 -> 1")
    print("\t4 -> 2")
    print("\t13 -> 144")


def run_sub_optimal(n, first_run=True):
    # Time complexity: O(2^n)
    # Space complexity: O(n)
    if first_run:
        n -= 1  # nth number not position n
    if n < 2:
        return n
    else:
        return run_sub_optimal(n - 1, False) + run_sub_optimal(n - 2, False)


def run_optimal(n):
    # Time complexity: O(n)
    # Space complexity: O(n)
    fibonacci = [0, 1]
    for i in range(2, n, 1):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    return fibonacci[n - 1]  # nth number not position n


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
    test.assertEqual(1, run(2))
    test.assertEqual(2, run(4))
    test.assertEqual(144, run(13))
    test.assertEqual(196418, run(28))
    test.assertEqual(7540113804746346429, run(93))
    print('All tests passed')


if __name__ == "__main__":
    main()
