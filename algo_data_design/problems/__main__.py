import sys

import algo_data_design
from algo_data_design.problems import *
from algo_data_design.utils import input as u_input


def print_problem_title(i, name):
    print('\t{} - {}'.format(i, name))
    return i + 1


def problems_info():
    print('Problems')
    i = print_problem_title(1, 'Matching Parenthesis')
    i = print_problem_title(i, 'Nth Fibonacci')
    i = print_problem_title(i, 'Replace words')
    i = print_problem_title(i, 'Word len')
    i = print_problem_title(i, 'Two sum')
    print()
    return i - 1


def main():
    amount_of_problems = problems_info()
    if algo_data_design.problems.NO_PROMPT:
        problems = list(range(1, amount_of_problems))
    else:
        print('Choose a problem to run [1 - {}]: '.format(amount_of_problems))
        problems = u_input.input_number(greater_or_eq=1, lower_or_eq=amount_of_problems)
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
        else:
            print('Unknown problem `{}`'.format(problem))
            sys.exit(1)


if __name__ == "__main__":
    main()
