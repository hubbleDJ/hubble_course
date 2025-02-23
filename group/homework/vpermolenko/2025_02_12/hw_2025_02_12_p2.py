"""Module homework 2025-02-12 Recursive quick sort"""

from random import randint

TEST_LIST: list[int | float] = [randint(0, 100) for x in range(10)]
print(TEST_LIST)

def quick_sort(list_to_sort: list[int | float]) -> list[int | float]:
    """
        Быстрая сортировка, возвращает новый отсортированный массив
    """

    sorted_list: list[int | float] = []
    less_list: list[int | float] = []
    greater_equal_list: list[int | float] = []

    if len(list_to_sort) <= 1:
        return list(list_to_sort)
    for index in range(len(list_to_sort) - 1):
        if list_to_sort[index] < list_to_sort[len(list_to_sort) - 1]:
            less_list.append(list_to_sort[index])
        else:
            greater_equal_list.append(list_to_sort[index])

    if len(less_list) >= 1:
        less_list = quick_sort(less_list)
    if len(greater_equal_list) >= 1:
        greater_equal_list = quick_sort(greater_equal_list)

    sorted_list.extend(less_list)
    sorted_list.append(list_to_sort[len(list_to_sort) - 1])
    sorted_list.extend(greater_equal_list)

    return sorted_list

print(quick_sort(TEST_LIST))
