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

    def __eq__(self, other):
        # https://bugs.python.org/issue30545
        if not isinstance(other, Enum):
            return False
        self_dict = self.__dict__
        other_dict = other.__dict__
        return self_dict['_value_'] == other_dict['_value_'] and str(self_dict['__objclass__']) == str(
            other_dict['__objclass__'])


class BubbleSortMethod(Enum):
    OPTIMUM = enum_auto()
    REGULAR = enum_auto()

    @staticmethod
    def get_all_methods():
        return list(map(lambda c: c, BubbleSortMethod))

    def __str__(self):
        return self.name

    def __eq__(self, other):
        # https://bugs.python.org/issue30545
        if not isinstance(other, Enum):
            return False
        self_dict = self.__dict__
        other_dict = other.__dict__
        return self_dict['_value_'] == other_dict['_value_'] and str(self_dict['__objclass__']) == str(
            other_dict['__objclass__'])


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
from .merge import sort_linked_list as merge_sort_linked_list
from .radix import sort as radix_sort
from .selection import sort as selection_sort
from .bucket import sort as bucket_sort
from .bogo import sort as bogo_sort
from .bogo import sort as stou_com_sort
