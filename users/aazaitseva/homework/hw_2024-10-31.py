#Написать пузырьковую сортировку

#def bubble_sort(sorted_list: list[int]) -> list[int]:
    #"""сротирует список пузырьковой сортировкой"""

    #return 

#принцип пузырьковой сортировки

def bubble_sort(sorted_list: list[int]) -> list[int]:
    n = len(sorted_list)
    for i in range(n):
        for y in range(0, n-1):
            if sorted_list[y] > sorted_list[y+1]:
                sorted_list[y], sorted_list[y+1] = sorted_list[y+1], sorted_list[y]
    return sorted_list
var_list = [58, 5, 458, 70, 9]
sort_list = bubble_sort(var_list)
print(sort_list)