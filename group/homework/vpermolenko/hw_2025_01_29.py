"""Module homework 2025-01-29 Bubble sort"""

arr_to_sort: list[int|float] = [6, 4, 5, 2, 1.5, 3]
print(arr_to_sort)

was_sorted_flag: bool = True
less_check_counter: int = 1

while was_sorted_flag :
    was_sorted_flag = False
    for index in range(len(arr_to_sort) - less_check_counter) :
        if arr_to_sort[index] > arr_to_sort[index + 1]:
            temp = arr_to_sort[index]
            arr_to_sort[index] = arr_to_sort[index + 1]
            arr_to_sort[index + 1] = temp
            was_sorted_flag = True
    less_check_counter += 1

print(arr_to_sort)
