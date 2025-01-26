def bubble_sort(sorted_list: list[int]) -> list[int]:
    len_sorted_list = len(sorted_list)
    for i in range(len_sorted_list):
        sorted_flag = False
        for y in range(0, len_sorted_list-1):
            if sorted_list[y] > sorted_list[y+1]:
                sorted_list[y], sorted_list[y +
                                            1] = sorted_list[y+1], sorted_list[y]
                sorted_flag = True
        if not sorted_flag:
            break
        print(sorted_list)
    return sorted_list


var_list = [5, 58, 458, 70, 9]
sort_list = bubble_sort(var_list)
