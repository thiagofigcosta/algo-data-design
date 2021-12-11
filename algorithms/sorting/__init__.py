from enum import Enum, auto as enum_auto


class QuickSortPivotMethod(Enum):
    MEDIAN = enum_auto()
    FIRST = enum_auto()
    LAST = enum_auto()
    MIDDLE = enum_auto()

    @staticmethod
    def get_all_methods():
        return list(map(lambda c: c, QuickSortPivotMethod))

    def __str__(self):
        return self.name


class BubbleSortMethod(Enum):
    OPTIMUM = enum_auto()
    REGULAR = enum_auto()

    @staticmethod
    def get_all_methods():
        return list(map(lambda c: c, BubbleSortMethod))

    def __str__(self):
        return self.name


from .intro import sort as sort
from .intro import sort as intro_sort
from .quick import sort as quick_sort
from .quick_insertion import sort as quick_insertion_sort
from .bubble import sort as bubble_sort
from .swap import sort as swap_sort
from .counting import sort as counting_sort
from .heap import sort as heap_sort
from .insertion import sort as insertion_sort
from .insertion import insert as insert_sorted
from .shell import sort as shell_sort
from .merge import sort as merge_sort
from .radix import sort as radix_sort
from .selection import sort as selection_sort
from .bucket import sort as bucket_sort
from .bogo import sort as bogo_sort
from .bogo import sort as stou_com_sort
