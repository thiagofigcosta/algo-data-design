import unittest

test = unittest.TestCase()


def info():
    print("Word len")
    print("For a given array of strings return a map containing a key for every word and its length as value")
    print("Examples:")
    print('\t["a", "bb", "a", "bb"] -> {"bb": 2, "a": 1}')
    print('\t["this", "and", "that", "and"] -> {"that": 4, "and": 3, "this": 4}')
    print('\t["code", "code", "code", "bug"] -> {"code": 4, "bug": 3}')


def run(words):
    # Time complexity: # O(n)
    # Space complexity: O(m), where m is the amount of distinguished words
    solution = {}
    for word in words:
        if word not in solution:
            solution[word] = len(word)
    return solution


def main():
    info()
    test.assertEqual({"bb": 2, "a": 1}, run(["a", "bb", "a", "bb"]))
    test.assertEqual({"that": 4, "and": 3, "this": 4}, run(["this", "and", "that", "and"]))
    test.assertEqual({"code": 4, "bug": 3}, run(["code", "code", "code", "bug"]))
    print('All tests passed')


if __name__ == "__main__":
    main()
