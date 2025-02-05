# Оптимизировать пузырьковую сортировку
# Засунуть сортировку в функцию

sorting_list: list[float|int] = [1, 3, 4, 5, 7, -1, 90, -11]
len_sorting_list: int = len(sorting_list)

for passage_list in range(len_sorting_list):
    for index_value in range(len_sorting_list - 1):
        if sorting_list[index_value] > sorting_list[index_value + 1]:
            buffer = sorting_list[index_value + 1]
            sorting_list[index_value + 1] = sorting_list[index_value]
            sorting_list[index_value] = buffer
            
print(sorting_list)