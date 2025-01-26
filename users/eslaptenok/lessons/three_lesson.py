x, y = 1, 2

def factorial(num: int) -> int:
    """ """

    answer: int = 1
    for i in range(1, num + 1):
        answer *= i
    return answer

print(factorial(5))

def search_number(search_list: list[int], num: int) -> int:
    """ """

    if len(search_list) == 1 and num == search_list[0]:
        return num
    elif len(search_list) == 1 and num != search_list[0]:
        return None

    half_list: int = int(len(search_list)/2)
    left_list: list[int] = search_list[:half_list] # 1, 2
    right_list: list[int] = search_list[half_list:] # 4, 5

    if num < left_list[0] or num > right_list[-1]:
        return None
    elif num <= left_list[-1]:
        return search_number(left_list, num)
    elif num >= right_list[0]:
        return search_number(right_list, num)
    return

print(search_number([1, 2, 3, 4, 5], 2))
print(search_number([1, 2, 4, 5], 3))
print(search_number([3], 3))
print(search_number([2], 3))
print(search_number([1, 2, 3, 4, 5], 6))
print(search_number([1, 2, 3, 4, 5], -1))
