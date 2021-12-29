import unittest

import algo_data_design.problems

test = unittest.TestCase()


def info():
    if algo_data_design.problems.NO_INFO:
        return
    print("Two sum")
    print("Given an array of ints and a target return the two indexes of the array")
    print("corresponding to elements that summed are equal to the target")
    print("The same index cannot be used twice and there is always a solution")
    print("Examples:")
    print('\t[2,7,11,15], 9 -> [0,1]')
    print('\t[3,2,4], 6 -> [1,2]')
    print('\t[3,3], 6 -> [0,1]')


def run(numbers, target):
    # Time complexity: O(n)
    # Space complexity: O(m), where m is the amount of different numbers in the list

    solutions = {}
    for i, number in enumerate(numbers):
        solutions[target - number] = i

    for j, number in enumerate(numbers):
        if number in solutions and solutions[number] != j:
            return [j, solutions[number]]


def main():
    info()
    test.assertEqual([0, 1], run([2, 7, 11, 15], 9))
    test.assertEqual([1, 2], run([3, 2, 4], 6))
    test.assertEqual([0, 1], run([3, 3], 6))
    if not algo_data_design.problems.NO_INFO:
        print('All tests passed')


if __name__ == "__main__":
    main()
