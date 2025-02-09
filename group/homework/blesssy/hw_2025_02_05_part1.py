# Оптимизировать пузырьковую сортировку
    # Прекратить сортировку если сортировать уже не надо
    
# Засунуть сортировку в функцию


def bubble_sort(nums: list[float|int]) -> list[int]:
    """sorting numbers in ascending order """

    length_nums: int = len(nums) 

    for ordinal_num in range(0, length_nums - 1):
        print(nums)
        nums_are_sorted: bool = True # checking if sorting is needed
        
        for index in range(0, length_nums - ordinal_num - 1):
            print (nums[index], nums[index + 1])
            if nums[index] > nums[index + 1]:
                nums[index], nums[index + 1] = \
                    nums[index  + 1], nums[index]
                nums_are_sorted = False # -> the list isn't sorted yet
        if nums_are_sorted:
            break
                
    return nums

list1: list[int] = [-500, -501, 5, 12, 32, 0, -4, 4, 56564, -432]
sorted_list = bubble_sort(list1[:])

print("Отсортированный список 1: ", sorted_list)
print("Отсортированный список 2: ", bubble_sort([1, 2, 3, 4, 7, 5, 6]))

