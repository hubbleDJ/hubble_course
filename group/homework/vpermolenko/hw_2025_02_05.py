"""Module homework 2025-02-05 functions"""

TEST_LIST: list[int | float] = [6, 4, 5, 3, 1.5, 2]
print(TEST_LIST)


def bubble_sort(list_to_sort: list[int | float]) -> list[int | float]:
    """base bubble sort for list of nums, returns new list"""

    sorting_list: list[int | float] = list[int | float](list_to_sort)
    was_sorted_flag: bool = True
    less_sort_counter: int = 1
    
    if len(sorting_list) == 2 and sorting_list[0] > sorting_list[1]:
        sorting_list[0], sorting_list[1] =\
            sorting_list[1], sorting_list[0]
    elif len(sorting_list) > 2:
        while was_sorted_flag:
            was_sorted_flag = False
            for index in range(len(sorting_list) - less_sort_counter):
                if sorting_list[index] > sorting_list[index + 1]:
                    sorting_list[index], sorting_list[index + 1] =\
                        sorting_list[index + 1], sorting_list[index]
                    was_sorted_flag = True
            less_sort_counter += 1

    return sorting_list


print(bubble_sort(TEST_LIST))
print(bubble_sort([2, 1]))
print(bubble_sort([1, 2]))
print(bubble_sort([2]))
print(bubble_sort([]))


def min_from_list(processing_list: list[int | float]) -> int | float | None:
    """finds and returns minimal element"""

    min_elem: int | float
    
    if len(processing_list) == 0:
        return
    else:
        min_elem = processing_list[0]
        if len(processing_list) == 2 and processing_list[0] > processing_list[1]:
            min_elem = processing_list[1]
        elif len(processing_list) > 2:
            for index in range(1, len(processing_list)):
                if processing_list[index] < min_elem:
                    min_elem = processing_list[index]
    
    return min_elem

print(min_from_list(TEST_LIST))
print(min_from_list([2, 1]))
print(min_from_list([1, 2]))
print(min_from_list([2]))
print(min_from_list([]))


def max_from_list(processing_list: list[int | float]) -> int | float | None:
    """finds and returns maximum element"""

    max_elem: int | float
    
    if len(processing_list) == 0:
        return
    else:
        max_elem = processing_list[0]
        if len(processing_list) == 2 and processing_list[0] < processing_list[1]:
            max_elem = processing_list[1]
        elif len(processing_list) > 2:
            for index in range(1, len(processing_list)):
                if processing_list[index] > max_elem:
                    max_elem = processing_list[index]
    
    return max_elem

print(max_from_list(TEST_LIST))
print(max_from_list([2, 1]))
print(max_from_list([1, 2]))
print(max_from_list([2]))
print(max_from_list([]))


def even_from_list(processing_list: list[int | float]) -> list[int | float]:
    """returns new list with only even nums from original list"""
    
    result_list: list[int|float] = []
    
    for elem in processing_list:
        if elem % 2 == 0:
            result_list.append(elem)
    
    return result_list

print(even_from_list(TEST_LIST))
print(even_from_list([2, 1]))
print(even_from_list([1, 2]))
print(even_from_list([2]))
print(even_from_list([]))
