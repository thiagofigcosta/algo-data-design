import algo_data_design
from algo_data_design.problems import *
from algo_data_design.utils import input as u_input


def print_problem_title(i, name):
    if not algo_data_design.problems.NO_INFO:
        print('\t{} - {}'.format(i, name))
    return i + 1


def problems_info():
    if not algo_data_design.problems.NO_INFO:
        print('Problems')
    i = print_problem_title(1, 'Matching Parenthesis')
    i = print_problem_title(i, 'Nth Fibonacci')
    i = print_problem_title(i, 'Replace words')
    i = print_problem_title(i, 'Word len')
    i = print_problem_title(i, 'Two sum')
    i = print_problem_title(i, 'Sum of two integers')
    i = print_problem_title(i, 'Climbing Stairs')
    i = print_problem_title(i, 'Coin change')
    i = print_problem_title(i, 'Clone graph')
    i = print_problem_title(i, 'Longest Common Subsequence')
    i = print_problem_title(i, 'Insert interval')
    i = print_problem_title(i, 'Reverse Linked List')
    i = print_problem_title(i, 'Set matrix zeroes')
    i = print_problem_title(i, 'Longest Substring Without Repeating Characters')
    i = print_problem_title(i, 'Maximum Depth of Binary Tree')
    i = print_problem_title(i, 'Merge k Sorted Lists')
    if not algo_data_design.problems.NO_INFO:
        print()
    return i - 1


def main():
    amount_of_problems = problems_info()
    if algo_data_design.problems.NO_PROMPT:
        problems = list(range(1, amount_of_problems + 1))
    else:
        print('Choose a problem to run [1 - {}]: '.format(amount_of_problems))
        problems = [u_input.input_number(greater_or_eq=1, lower_or_eq=amount_of_problems)]
    for problem in problems:
        if problem == 1:
            matching_parenthesis.main()
        elif problem == 2:
            nth_fibonacci.main()
        elif problem == 3:
            replace_words.main()
        elif problem == 4:
            word_len.main()
        elif problem == 5:
            two_sum.main()
        elif problem == 6:
            sum_of_two_integers.main()
        elif problem == 7:
            climbing_stairs.main()
        elif problem == 8:
            coin_change.main()
        elif problem == 9:
            clone_graph.main()
        elif problem == 10:
            longest_common_subsequence.main()
        elif problem == 11:
            insert_interval.main()
        elif problem == 12:
            reverse_linked_list.main()
        elif problem == 13:
            set_matrix_zeroes.main()
        elif problem == 14:
            longest_substring_without_repeating_characters.main()
        elif problem == 15:
            maximum_depth_of_binary_tree.main()
        elif problem == 16:
            merge_k_sorted_lists.main()
        else:
            raise NotImplementedError('Unknown problem `{}`'.format(problem))
        if not algo_data_design.problems.NO_INFO:
            print()


if __name__ == "__main__":
    main()
