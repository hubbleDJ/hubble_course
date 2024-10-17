# написать функцию, которая выполняет пузырьковую сортировку у списка
def bubble_sort(no_sort_list: list[int | float]) -> list[int | float]:
    """Сортирует список с помощью пузырьковой сортировки"""

    sort_list: list[int | float] = []
    elem: int | float = 0
    for i in range(0, len(no_sort_list) - 1):
        for i in range(0, len(no_sort_list) - 1):
            if no_sort_list[i] > no_sort_list[i + 1]:
                elem = no_sort_list[i]
                no_sort_list[i] = no_sort_list[i + 1]
                no_sort_list[i + 1] = elem
    sort_list: list[int | float] = no_sort_list
    return sort_list

print(bubble_sort([1, 5, -8, 1.3, 0]))

# написать функцию которая принимает строку(любой текст и любой длины) 
# и возвращает словарь, ключами которого являются символы данно текста, значением их количества в тексте ada
def num_of_characters_line(line: str) -> dict[str, int]:
    """Подсчитывает количество каждого символа в строке"""

    symbol_dict: dict[str, int] = {}
    symbol: str = None
    for i in range(0, len(line)):
        count: int = 0
        symbol: str = line[i]
        for i in range(0, len(line)):
            if line[i] == symbol:
                count += 1
                symbol_dict[line[i]] = count
    return symbol_dict

print(num_of_characters_line('python cool language'))
   
