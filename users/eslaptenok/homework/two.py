# написать функцию, которая выполняет пузырьковую сортировку у списка
def bubble_sort(sort_list: list[int | float]) -> list[int | float]:
    """Сортирует список с помощью пузырьковой сортировки"""
    
    lenght_list: int = len(sort_list)
    for i in range(0, lenght_list - 1):
        for i in range(0, lenght_list - 1):
            if sort_list[i] > sort_list[i + 1]:
                elem: int | float = sort_list[i]
                sort_list[i] = sort_list[i + 1]
                sort_list[i + 1] = elem
                indicator: bool = True
            else:
                indicator = False
        lenght_list -= 1
        if indicator == False:
            break
    return sort_list

print(bubble_sort([1, 5, -8, 1.3, 0]))
print(bubble_sort([55, 0, 1, 4, 5]))

# написать функцию которая принимает строку(любой текст и любой длины) 
# и возвращает словарь, ключами которого являются символы данно текста, значением их количества в тексте
def num_of_characters_line(line: str) -> dict[str, int]:
    """Подсчитывает количество каждого символа в строке"""

    symbol_dict: dict[str, int] = {}  
    for symbol in line: 
        if symbol in symbol_dict:
            symbol_dict[symbol] += 1
        else:
            symbol_dict[symbol] = 1
    return symbol_dict

print(num_of_characters_line('python cool language'))