import unittest

import algo_data_design
from algo_data_design.utils import input as u_input

test = unittest.TestCase()


def info():
    if algo_data_design.problems.NO_INFO:
        return
    print("Replace words")
    print("In English a word can be formed by the union of a root and another word, the new one is called successor")
    print("The root `an` + the word `other` forms the successor `another`")
    print("Given a list of root words and a sentence, replace all successors in the sentence by the root")
    print("If more than one root can replace a successor, replace it with the shortest root")
    print("Examples:")
    print('\t["cat","bat","rat"], "the cattle was rattled by the battery" -> "the cat was rat by the bat"')
    print('\t["a","b","c"], "aadsfasf absbs bbab cadsfafs" -> "a a b c"')


def run_with_set(roots, sentence):
    # considering: `n` as amount of roots, `m` as the amount of words and `a` as word average size
    # Time complexity: # O(n*a+n)
    # Space complexity: O(m*a)
    roots_set = set(roots)
    sentence_array = sentence.split(' ')  # O(n)
    for i in range(len(sentence_array)):  # O(m)
        word = sentence_array[i]
        for j in range(1, len(word), 1):
            if word[:j] in roots_set:
                word = word[:j]
                break
        sentence_array[i] = word
    return ' '.join(sentence_array)


def run_with_ordered_search(roots, sentence):
    # considering: `n` as amount of roots, `m` as the amount of words and `a` as word average size
    # Time complexity: O(n*(log(n)+m+a))
    # Space complexity: O(m*a+n)
    sorted_roots = sorted(roots)  # O(n*log(n))
    sentence_array = sentence.split(' ')  # O(n)
    for i in range(len(sentence_array)):  # O(m)
        word = sentence_array[i]
        matching_roots = []
        for root in sorted_roots:  # O(m*n)
            matches = True
            if len(root) >= len(word):
                # A root must be smaller then the successor
                matches = False
            else:
                for j in range(len(root)):  # O(m*n*a)
                    if word[j] != root[j]:
                        matches = False  # if the first char does not match we don't need to continue searching
                        break
            if matches:
                matching_roots.append(root)
            elif root[0] > word[0]:
                # If the first char of the root is higher than the first of the word
                # no other roots will match, because the roots are sorted
                break
        if len(matching_roots) > 0:  # replace
            matching_roots.sort(key=lambda x: len(x))
            sentence_array[i] = matching_roots[0]
    return ' '.join(sentence_array)


def main():
    if algo_data_design.problems.NO_PROMPT:
        solution = 1
    else:
        print('Choose a solution to run:')
        print('\t1 - Using ordered search')
        print('\t2 - Using hash set')
        solution = u_input.input_number(greater_or_eq=1, lower_or_eq=2)
    if solution == 1:
        run = run_with_ordered_search
    elif solution == 2:
        run = run_with_set
    else:
        raise AttributeError('Unknown solution')
    info()
    test.assertEqual("the cat was rat by the bat", run(["cat", "bat", "rat"], "the cattle was rattled by the battery"))
    test.assertEqual("a a b c", run(["a", "b", "c"], "aadsfasf absbs bbab cadsfafs"))
    if not algo_data_design.problems.NO_INFO:
        print('All tests passed')


if __name__ == "__main__":
    main()
