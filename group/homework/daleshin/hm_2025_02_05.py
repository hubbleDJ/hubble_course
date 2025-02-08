# sorting_list: list[float|int] = [1, 2, 3, 4, 5, 6]
sorting_list: list[float|int] = [12, 32, 0, -4, 4, 564564, 63, 5976]

# Написать функцию, которая возвращает максимальное значение в списке

def FindMax(num_list: list[float|int]) -> list[float|int]:
    """Функция ищет максимальное число"""
    
    num_max: float|int = num_list[0]
    for num in num_list:
        if num > num_max:
            num_max = num

    return num_max

# Написать функцию, которая возвращает минимальное значение в списке

def FindMin(num_list: list[float|int]) -> list[float|int]:
    """Функция ищет минимальное число"""
    
    num_min: float|int = num_list[0]
    for num in num_list:
        if num < num_min:
            num_min = num

    return num_min

# Написать функцию, которая возвращает все четные элементы списка в виде новго списка

def EvenNums(num_list: list[float|int]) -> list[float|int]:
    """Функция ищет четные числа и складывает в новый список"""
    
    nums_sorted:list[float|int] = []
    for num in num_list:
        if num % 2 == 0 and num != 0:
            nums_sorted.append(num)

    return nums_sorted

# Оптимизировать пузырьковую сортировку
 # Прекратить сортировку если сортировать уже не надо
    
# Засунуть сортировку в функцию

def BubbleSort(num_list: list[float|int]) -> list[float|int]:
    """Функция сортирует список пузырьком """
    
    already_sorted: bool = False

    for passage_list in range(len(num_list) - 1):
        if already_sorted == False:
            already_sorted = True
            for index_value in range(len(num_list) - 1 - passage_list):
                if num_list[index_value] > num_list[index_value + 1]:
                    num_list[index_value], num_list[index_value + 1] = num_list[index_value + 1], num_list[index_value]
                    already_sorted = False

        elif already_sorted == True:
            break

    return num_list

print(FindMax(sorting_list))
print(FindMin(sorting_list))
print(EvenNums(sorting_list))
print(BubbleSort(sorting_list))