# написать функцию, которая выполняет пузырьковую сортировку у списка
def bubble_sort(no_sotr_list: list[int | float]) -> list[int | float]:
    """Сортирует список с помощью пузырьковой сортировки"""

    sort_list: list[int | float] = []
    return sort_list

print(bubble_sort([1, 5, -8, 1.3, 0]))
elem: int = 0
sort_list: list[int] = [1, 5, -8, 1.3, 0]
for i in range(0, len(sort_list) - 1):
    if sort_list[i] > sort_list[i + 1]:
        sort_list[i] = sort_list[i + 1]

        

# написать функцию которая принимает строку(любой текст и любой длины) 
# и возвращает словарь, ключами которого являются символы данно текста, значением их количества в тексте

{
    'п': 1,
    'р': 1,
    ',': 2
}
   
