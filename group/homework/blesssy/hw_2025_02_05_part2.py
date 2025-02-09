# 1 Написать функцию, которая возвращает максимальное значение в списке
def max_num_in_list(nums1: list[float|int]) -> float|int:
    '''returns max num from list'''
    max_num = nums1[0] # take the 0 index as the max num
    
    length_nums1: int = len(nums1)
    for current_num in range(0, length_nums1):
        if nums1[current_num] > max_num:
            max_num = nums1[current_num] # update the max num
    return max_num

list1: list[int|float] = [6, 3, 9, 1, 4567, 976, 93456]
print(f"the max num in the list {list1} is: ", max_num_in_list(list1))

# 2 Написать функцию, которая возвращает минимальное значение в списке
def min_num_in_list(nums2: list[float|int]) -> float|int:
    '''returns min num from list'''
    min_num = nums2[0] # take the 0 index as the min num
    
    length_nums2: int = len(nums2)
    for current_num in range(0, length_nums2):
        if nums2[current_num] < min_num:
            min_num = nums2[current_num] # update the min num
    return min_num

list2: list[int|float] = [6, 3, 9, 1, 4567, -108, 976, 93456]
print(f"the min num in the list {list2} is: ", min_num_in_list(list2))

# 3 Написать функцию, которая возвращает все четные элементы списка в виде новго списка

def find_even_nums(nums3: list[float|int]) -> int:
    '''returns all even nums from list'''
    even_nums: list[int] = [] # empty list for even nums
    
    for current_num in nums3:
        if current_num % 2 == 0:
            even_nums.append(current_num)
            
    return even_nums

list3: list[int|float] = [6, -634, 9, 1, 4567, -108, 976, 93456]
print(f"even nums in the list {list2} are: ", find_even_nums(list3))