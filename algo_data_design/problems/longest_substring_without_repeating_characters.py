import unittest

import algo_data_design.problems

test = unittest.TestCase()


def info():
    if algo_data_design.problems.NO_INFO:
        return
    print("Longest Substring Without Repeating Characters")
    print("Given a string return length of the longest substring without repeating characters")
    print("Examples:")
    print('\t"abcabcbb" -> 3')
    print('\t"bbbbb" -> 1')
    print('\t"pwwkew" -> 3')


def run(string):
    # Time complexity: O(n)
    # Space complexity: O(n)
    if len(string) <= 1:
        return len(string)
    length_of_longest_sub_str = 1
    temp_longest_sub_str = string[0]

    for c in string[1:]:
        try:
            index_of_char = temp_longest_sub_str.index(c)
        except:
            index_of_char = None
        if index_of_char is None:
            temp_longest_sub_str += c
            length_of_longest_sub_str = max(length_of_longest_sub_str, len(temp_longest_sub_str))
        else:
            temp_longest_sub_str = temp_longest_sub_str[index_of_char + 1:] + c
    return length_of_longest_sub_str


def main():
    info()
    test.assertEqual(3, run("abcabcbb"))
    test.assertEqual(1, run("bbbbb"))
    test.assertEqual(3, run("pwwkew"))
    test.assertEqual(0, run(""))
    if not algo_data_design.problems.NO_INFO:
        print('All tests passed')


if __name__ == "__main__":
    main()
