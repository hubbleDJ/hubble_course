# Нписать любую сортировку,
# в которой есть рекурсия(быстрая, сортировка делением)

def merge_sort(my_array: list[float|int]) -> list[float|int]:
    """sorting nums in ascending order by merging"""
    
    if len(my_array) <= 1:
        #if the length of an array is 1, it's already sorted
        return my_array
    
    middle = len(my_array) // 2
        #dividing an array into 2 parts: left and right
    left = my_array[:middle]
    right = my_array[middle:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)

def merge (left: list[float|int], right: list[float|int]) -> list[float|int]:
    """merging 2 arrays into one"""
    
    sorted_array = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_array.append(left[left_index])
            left_index = left_index + 1
        else: 
            sorted_array.append(right[right_index])
            right_index = right_index + 1
    #adding the remaining numbers if one of the arrays is empty
    sorted_array = sorted_array + left[left_index:]
    sorted_array = sorted_array + right[right_index:]
    
    return sorted_array

my_array = [423, -3209, 22.71, -1453, -320, -13.34, 1225, -497, -2251, 1769]
sorted_array = merge_sort(my_array)
print(sorted_array)