from matplotlib import pyplot as plt

import sorting
import utils.list as u_list
import utils.plot as u_plot
import utils.time as u_time


def sorting_benchmark():
    benchmark_start_time = u_time.time()
    array_sizes = (5, 10, 100, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000)
    max_size_for_on2_algs = 10000
    last_size_for_all_algs = 50000
    deltas = {}
    for algorithm in (
            'bogo', 'bubble_opt', 'bubble_reg', 'bucket', 'counting', 'heap', 'insertion', 'intro', 'merge',
            'quick_median',
            'quick_mid', 'quick_first', 'quick_last', 'quick_insertion', 'radix', 'selection', 'shell', 'swap'):
        deltas[algorithm] = []
    for size in array_sizes:
        int_list = u_list.random_int_list(size)
        int_list_short_range = u_list.random_int_list(size, -500, 500)
        float_list = u_list.random_float_list(size)
        if size <= sorting.bogo.MAXIMUM_FAST_SORTING_SIZE:
            to_sort = int_list.copy()
            before = u_time.time()
            sorting.bogo.sort(to_sort)
            delta = u_time.delta(before)
            deltas['bogo'].append(delta)

        if size <= max_size_for_on2_algs:
            to_sort = int_list.copy()
            before = u_time.time()
            sorting.bubble.sort(to_sort, method=sorting.BubbleSortMethod.OPTIMUM)
            delta = u_time.delta(before)
            deltas['bubble_opt'].append(delta)

            to_sort = int_list.copy()
            before = u_time.time()
            sorting.bubble.sort(to_sort, method=sorting.BubbleSortMethod.REGULAR)
            delta = u_time.delta(before)
            deltas['bubble_reg'].append(delta)

        to_sort = float_list.copy()
        before = u_time.time()
        sorting.bucket.sort(to_sort)
        delta = u_time.delta(before)
        deltas['bucket'].append(delta)

        to_sort = int_list.copy()
        before = u_time.time()
        sorting.counting.sort(to_sort)
        delta = u_time.delta(before)
        deltas['counting'].append(delta)

        to_sort = int_list.copy()
        before = u_time.time()
        sorting.heap.sort(to_sort)
        delta = u_time.delta(before)
        deltas['heap'].append(delta)

        if size <= max_size_for_on2_algs:
            to_sort = int_list.copy()
            before = u_time.time()
            sorting.insertion.sort(to_sort)
            delta = u_time.delta(before)
            deltas['insertion'].append(delta)

        to_sort = int_list.copy()
        before = u_time.time()
        sorting.intro.sort(to_sort)
        delta = u_time.delta(before)
        deltas['intro'].append(delta)

        to_sort = int_list.copy()
        before = u_time.time()
        sorting.merge.sort(to_sort)
        delta = u_time.delta(before)
        deltas['merge'].append(delta)

        to_sort = int_list.copy()
        before = u_time.time()
        sorting.quick.sort(to_sort, pivot_method=sorting.QuickSortPivotMethod.MEDIAN)
        delta = u_time.delta(before)
        deltas['quick_median'].append(delta)

        to_sort = int_list.copy()
        before = u_time.time()
        sorting.quick.sort(to_sort, pivot_method=sorting.QuickSortPivotMethod.MIDDLE)
        delta = u_time.delta(before)
        deltas['quick_mid'].append(delta)

        to_sort = int_list.copy()
        before = u_time.time()
        sorting.quick.sort(to_sort, pivot_method=sorting.QuickSortPivotMethod.FIRST)
        delta = u_time.delta(before)
        deltas['quick_first'].append(delta)

        to_sort = int_list.copy()
        before = u_time.time()
        sorting.quick.sort(to_sort, pivot_method=sorting.QuickSortPivotMethod.LAST)
        delta = u_time.delta(before)
        deltas['quick_last'].append(delta)

        to_sort = int_list.copy()
        before = u_time.time()
        sorting.quick_insertion.sort(to_sort)
        delta = u_time.delta(before)
        deltas['quick_insertion'].append(delta)

        to_sort = int_list_short_range.copy()
        before = u_time.time()
        sorting.radix.sort(to_sort)
        delta = u_time.delta(before)
        deltas['radix'].append(delta)

        if size <= max_size_for_on2_algs:
            to_sort = int_list.copy()
            before = u_time.time()
            sorting.selection.sort(to_sort)
            delta = u_time.delta(before)
            deltas['selection'].append(delta)

            to_sort = int_list.copy()
            before = u_time.time()
            sorting.shell.sort(to_sort)
            delta = u_time.delta(before)
            deltas['shell'].append(delta)

            to_sort = int_list.copy()
            before = u_time.time()
            sorting.swap.sort(to_sort)
            delta = u_time.delta(before)
            deltas['swap'].append(delta)

    largest_value = 0
    largest_size = 0
    for _, results in deltas.items():
        largest_value = max(results + [largest_value])
        largest_size = max([len(results)] + [largest_size])

    for i, (algorithm, results) in enumerate(deltas.items()):
        results_small = results[:array_sizes.index(last_size_for_all_algs)]
        array_sizes_small = array_sizes[:array_sizes.index(last_size_for_all_algs)]
        infinite_array = [largest_value * 1.11] * (len(array_sizes_small) - len(results_small))
        plt.plot(array_sizes_small, results_small + infinite_array, 'o-', color=u_plot.get_plot_colour_by_index(i),
                 label=algorithm)
    title = 'Sorting algorithms benchmark'
    plt.ylim([0, largest_value * 1.03])
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
        if len(results) == largest_size:
            plt.plot(array_sizes, results, 'o-', color=u_plot.get_plot_colour_by_index(i), label=algorithm)
    title = 'Fast sorting algorithms benchmark'
    plt.title(title)
    mng = plt.get_current_fig_manager()
    mng.resize(2000, 1200)  # TODO magic
    mng.canvas.manager.set_window_title(title)
    plt.xlabel("Array sizes")
    plt.ylabel("Time (s)")
    plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
    plt.tight_layout(rect=[0, 0, 1, 1])  # plt.savefig("output.png", bbox_inches="tight")
    plt.show()

    print(u_time.timestamp_to_human_readable_str(u_time.delta(benchmark_start_time)))


def main():
    sorting_benchmark()


if __name__ == "__main__":
    main()
