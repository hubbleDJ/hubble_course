# Написать функцию, которая возвращает максимальное значение в списке

def number_max(number_list: list[float|int]) -> float|int:
    """Находит максимальное значение"""
    
    num_max: float|int = number_list[0]
    for num in number_list:
        if num > num_max:
            num_max = num

    return num_max

# Написать функцию, которая возвращает минимальное значение в списке

def number_min(number_list: list[float|int]) -> float|int:
    """Находит минимальное значение"""
    
    num_min: float|int = number_list[0]
    for num in number_list:
        if num < num_min:
            num_min = num

    return num_min

# Написать функцию, которая возвращает все четные элементы списка в виде новго списка

def even_nums(number_list: list[float|int]) -> list[float|int]:
    """Поиск четного и добавление в новый список"""
    
    even_numbers_list: list[float|int] = []
    for num in number_list:
        if num % 2 == 0:
            even_numbers_list.append(num)

    return even_numbers_list

# Написать пузырьковую сортровку
spisok_num: list = [12, 32, 0, -4, 4, 564564]

def buble_sort(number_list: list[float|int]) -> list[float|int]:
    """Сортирует пузырьковым методом(последовательно сравнивать значения соседних элементов и меняет 
    числа местами, если предыдущее оказывается больше последующего. 
    Таким образом элементы с большими значениями оказываются в конце списка, 
    а с  меньшими остаются в начале)"""

    sorted_done: bool = False
    for pass_num in range(len(number_list) - 1):
        sorted_done = True
        for compare_index in range(len(number_list) - pass_num - 1):
            if number_list[compare_index] > number_list[compare_index + 1]:
                number_list[compare_index], number_list[compare_index + 1] = \
                number_list[compare_index + 1], number_list[compare_index]
                sorted_done = False
        if sorted_done == True:
            break 
    
    return number_list

print(number_max(spisok_num), number_min(spisok_num), even_nums(spisok_num), buble_sort(spisok_num), sep='\n')