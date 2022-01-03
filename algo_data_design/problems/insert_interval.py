import unittest

import algo_data_design.problems

test = unittest.TestCase()


def info():
    if algo_data_design.problems.NO_INFO:
        return
    print("Insert Interval")
    print("An interval is a sorted array of integers, containing two numbers. For a given sorted array of intervals")
    print("and a new interval, insert the new interval on the intervals list. The new list must not have overlaps!")
    print("Examples:")
    print('\t[[1,3],[6,9]], [4,5] -> [[1,3],[4,5],[6,9]]')
    print('\t[[1,3],[6,9]], [2,5] -> [[1,5],[6,9]]')
    print('\t[[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8] -> [[1,2],[3,10],[12,16]]')


def run(intervals, new_interval):
    # Time complexity: O(n)
    # Space complexity: O(n)
    new_intervals = []
    overlap_list = []
    overlap_index = None
    for i, interval in enumerate(intervals):
        # check for overlapping intervals or full overlaps
        partial_overlap_1 = interval[0] <= new_interval[0] <= interval[1]
        partial_overlap_2 = interval[0] <= new_interval[1] <= interval[1]
        full_overlap_1 = new_interval[0] <= interval[0] and interval[1] <= new_interval[1]
        full_overlap_2 = interval[0] <= new_interval[0] and new_interval[1] <= interval[1]
        if any([partial_overlap_1, partial_overlap_2, full_overlap_1, full_overlap_2]):
            overlap_list.append(interval)
            if overlap_index is None:
                overlap_index = i
        else:
            new_intervals.append(interval)
    if overlap_index is None:
        # if there is no overlap insert the new interval in order
        for i, interval in enumerate(new_intervals):
            if interval[0] > new_interval[0]:
                new_intervals.insert(i, new_interval)
                return new_intervals
        new_intervals.append(new_interval)
        return new_intervals
    else:
        # if there is overlaps, find the interval that defines the union
        overlap_list.append(new_interval)
        all_numbers = []
        for interval in overlap_list:
            all_numbers += interval
        new_interval_min = min(all_numbers)
        new_interval_max = max(all_numbers)
        new_intervals.insert(overlap_index, [new_interval_min, new_interval_max])
        return new_intervals


def main():
    info()
    test.assertEqual([[0, 0], [1, 5]], run([[1, 5]], [0, 0]))
    test.assertEqual([[1, 3], [4, 5], [6, 9]], run([[1, 3], [6, 9]], [4, 5]))
    test.assertEqual([[1, 5], [6, 9]], run([[1, 3], [6, 9]], [2, 5]))
    test.assertEqual([[1, 2], [3, 10], [12, 16]], run([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
    if not algo_data_design.problems.NO_INFO:
        print('All tests passed')


if __name__ == "__main__":
    main()
