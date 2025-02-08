# Написать пузырьковую сортировку
# [12, 32, 0, -4, 4, 56564]

def bubble_sort(nums: list[int]) -> list[int]:
    """sorting numbers in ascending order """

    length_nums  = len(nums)
    for ordinal_num  in range(0, length_nums - 1):
        for current_ord_num  in range(0, length_nums - 1):
            if nums[current_ord_num] > nums[current_ord_num + 1]:
                nums[current_ord_num], nums[current_ord_num + 1] = \
                        nums[current_ord_num  + 1], nums[current_ord_num]

    return nums

list1: list[int] = [-500, -501, 5, 12, 32, 0, -4, 4, 56564, -432]
bubble_sort(list1)

print("Отсортированный список 1: ", list1)
print("Отсортированный список 1: ", bubble_sort([-1, -5]))
