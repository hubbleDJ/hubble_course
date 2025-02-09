# Написать функцию, которая возвращает максимальное значение в списке

def NumberMax(number_list: list[float|int]) -> float|int:
    """Находит максимальное значение"""
    
    num_max: float|int = number_list[0]
    for num in number_list:
        if num > num_max:
            num_max = num

    return num_max

# Написать функцию, которая возвращает минимальное значение в списке

def NumberMin(number_list: list[float|int]) -> float|int:
    """Находит минимальное значение"""
    
    num_min: float|int = number_list[0]
    for num in number_list:
        if num < num_min:
            num_min = num

    return num_min

# Написать функцию, которая возвращает все четные элементы списка в виде новго списка

def EvenNums(number_list: list[float|int]) -> list[float|int]:
    """Поиск четного и добавление в новый список"""
    
    number_sorted:list[float|int] = []
    for num in number_list:
        if num % 2 == 0 and num != 0:
            number_sorted.append(num)

    return number_sorted

# Оптимизировать пузырьковую сортировку
# Прекратить сортировку если сортировать уже не надо
# Засунуть сортировку в функцию

def BubbleSort(number_list: list[float|int]) -> list[float|int]:
    """Пузырьковая сортировка списка """
    
    sorted_done: bool = False

    for passage_list in range(len(number_list) - 1):
        sorted_done = True
        for index_value in range(len(number_list) - 1 - passage_list):
            if number_list[index_value] > number_list[index_value + 1]:
                number_list[index_value], number_list[index_value + 1] = number_list[index_value + 1], number_list[index_value]
                sorted_done = False
        if sorted_done == True:
            break

    return number_list

number_list: list[float|int] = [1, 2, 3, 4, 5, 6]

print(NumberMax(number_list))
print(NumberMin(number_list))
print(EvenNums(number_list))
print(BubbleSort(number_list))