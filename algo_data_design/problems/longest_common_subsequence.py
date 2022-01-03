import unittest

import algo_data_design.problems

test = unittest.TestCase()


def info():
    if algo_data_design.problems.NO_INFO:
        return
    print("Longest Common Subsequence")
    print("Given two strings str_1 and str_2, return the length of the longest common sub sequence (LCSS) of them")
    print("The LSCC is a string that can be formed using characters of both strings in order, but some indexes can")
    print("can be skipped in both strings.")
    print("Examples:")
    print('\t"abcde", "ace" -> 3')
    print('\t"abcdex", "acesx" -> 4')
    print('\t"thithi", "thithi" -> 6')
    print('\t"abc", "xyz" -> 0')


def run(str_1, str_2):
    # Time complexity: O(n*m), where n is the amount of coins and m is the amount sum
    # Space complexity: O(n*m)
    # Bottom up, solves simple problems first and then go the complex one, navigate the tree of choices from
    # the simplest case till the complex one, storing the known solutions to avoid recomputing
    uninitialized_cell = -1
    dp_cache = []
    for _ in range(len(str_1) + 1):  # plus one to store the base case
        row = [uninitialized_cell] * (len(str_2) + 1)  # plus one to store the base case
        dp_cache.append(row)
    # fill up base cases
    for i in range(len(str_1) + 1):  # initialize with base case, for string size 0 there is no sequence
        dp_cache[i][0] = 0
    for j in range(len(str_2) + 1):  # initialize with base case, for string size 0 there is no sequence
        dp_cache[0][j] = 0

    for i in range(1, len(str_1) + 1, 1):  # solving from the simplest case till the original problem
        for j in range(1, len(str_2) + 1, 1):  # starting with strings with just the first char
            char_1 = str_1[i - 1]
            char_2 = str_2[j - 1]
            if char_1 == char_2:
                # if the chars are equal add one to the previous solution that were not using the current chars
                dp_cache[i][j] = dp_cache[i - 1][j - 1] + 1
            else:
                # if they are not the same pick the best solution between not using the current char of str 1 or not
                # using the current char of str 2
                dp_cache[i][j] = max(dp_cache[i - 1][j], dp_cache[i][j - 1])

    return dp_cache[len(str_1)][len(str_2)]


def main():
    info()
    test.assertEqual(3, run("abcde", "ace"))
    test.assertEqual(4, run("abcdex", "acesx"))
    test.assertEqual(6, run("thithi", "thithi"))
    test.assertEqual(0, run("abc", "xyz"))
    if not algo_data_design.problems.NO_INFO:
        print('All tests passed')


if __name__ == "__main__":
    main()
