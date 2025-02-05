# Написать функцию, которая возвращает максимальное значение в списке
# Написать функцию, которая возвращает минимальное значение в списке
# Написать функцию, которая возвращает все четные элементы списка в виде новго списка

# Оптимизировать пузырьковую сортировку
    # Прекратить сортировку если сортировать уже не надо
    
# Засунуть сортировку в функцию

sorting_list: list[float|int] = [1, 2, 3, 4, 5, 6]
len_sorting_list: int = len(sorting_list)

for passage_list in range(len_sorting_list):
    print(sorting_list)
    for index_value in range(len_sorting_list - 1):
        print(sorting_list[index_value], sorting_list[index_value + 1])
        if sorting_list[index_value] > sorting_list[index_value + 1]:
            sorting_list[index_value], sorting_list[index_value + 1] =\
                sorting_list[index_value + 1], sorting_list[index_value]
            
print(sorting_list)