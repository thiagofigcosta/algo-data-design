from matplotlib import pyplot as plt

import algo_data_design.utils.list as u_list
import algo_data_design.utils.plot as u_plot
import algo_data_design.utils.random as u_number
from algo_data_design.algorithms import searching
from algo_data_design.utils import time as u_time


def searching_benchmark():
    benchmark_start_time = u_time.time()
    tests_per_array = 30
    step = 7
    array_sizes = (100, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 2000000)
    deltas = {}
    for algorithm in ('linear', 'binary', 'jump', 'interpolation'):
        deltas[algorithm] = ([], [])
    for size in array_sizes:
        int_list = u_list.sequential_stepped_int_list(size, step)
        largest_number = max(int_list)
        numbers_to_find = []
        for _ in range(tests_per_array):
            numbers_to_find.append(u_number.random_int(0, largest_number))

        partial_results = ([], [])
        for to_find in numbers_to_find:
            before = u_time.time()
            _, hits = searching.linear_search_with_hits(int_list, to_find)
            delta = u_time.delta(before)
            partial_results[0].append(delta)
            partial_results[1].append(hits)
        deltas['linear'][0].append(sum(partial_results[0]))
        deltas['linear'][1].append(sum(partial_results[1]) / tests_per_array)

        partial_results = ([], [])
        for to_find in numbers_to_find:
            before = u_time.time()
            _, hits = searching.jump_search_with_hits(int_list, to_find)
            delta = u_time.delta(before)
            partial_results[0].append(delta)
            partial_results[1].append(hits)
        deltas['jump'][0].append(sum(partial_results[0]))
        deltas['jump'][1].append(sum(partial_results[1]) / tests_per_array)

        partial_results = ([], [])
        for to_find in numbers_to_find:
            before = u_time.time()
            _, hits = searching.interpolation_search_with_hits(int_list, to_find)
            delta = u_time.delta(before)
            partial_results[0].append(delta)
            partial_results[1].append(hits)
        deltas['interpolation'][0].append(sum(partial_results[0]))
        deltas['interpolation'][1].append(sum(partial_results[1]) / tests_per_array)

        partial_results = ([], [])
        for to_find in numbers_to_find:
            before = u_time.time()
            _, hits = searching.binary_search_with_hits(int_list, to_find)
            delta = u_time.delta(before)
            partial_results[0].append(delta)
            partial_results[1].append(hits)
        deltas['binary'][0].append(sum(partial_results[0]))
        deltas['binary'][1].append(sum(partial_results[1]) / tests_per_array)

    delta_experiment = u_time.delta(benchmark_start_time)
    print('Experiments took:', u_time.timestamp_to_human_readable_str(delta_experiment))

    for i, (algorithm, results) in enumerate(deltas.items()):
        plt.plot(array_sizes, results[0], 'o-', color=u_plot.get_plot_colour_by_index(i), label=algorithm)
    title = 'Searching algorithms benchmark'
    plt.title(title)
    mng = plt.get_current_fig_manager()
    mng.resize(2000, 1200)  # TODO magic
    mng.canvas.manager.set_window_title(title)
    plt.xlabel("Array sizes")
    plt.ylabel("Time (s)")
    plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
    plt.tight_layout(rect=[0, 0, 1, 1])  # plt.savefig("output.png", bbox_inches="tight")
    plt.show(block=False)

    plt.figure()  # clear for next figure

    for i, (algorithm, results) in enumerate(deltas.items()):
        plt.plot(array_sizes, results[1], 'o-', color=u_plot.get_plot_colour_by_index(i), label=algorithm)
    title = 'Searching algorithms benchmark'
    plt.title(title)
    mng = plt.get_current_fig_manager()
    mng.resize(2000, 1200)  # TODO magic
    mng.canvas.manager.set_window_title(title)
    plt.xlabel("Array sizes")
    plt.ylabel("Hits")
    plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
    plt.tight_layout(rect=[0, 0, 1, 1])  # plt.savefig("output.png", bbox_inches="tight")
    plt.show()


def main():
    searching_benchmark()


if __name__ == "__main__":
    main()
