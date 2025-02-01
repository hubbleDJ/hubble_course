# Написать пузырьковую сортировку
# [12, 32, 0, -4, 4, 56564]

def bubble(bubble_sort: list[int]) -> list[int]:
    """_summary_

    Args:
        bubble_sort (list[int]): _description_

    Returns:
        list[int]: _description_
    """
                             # переименовать bubble_sort, num, i и j +++ дописать докстринг
    num = len(bubble_sort)
    for i in range(0, num - 1):
        for j in range(0, num - 1):
            if bubble_sort[j] > bubble_sort[j + 1]:
                bubble_sort[j], bubble_sort[j + 1] = bubble_sort[j + 1], bubble_sort[j]

    return bubble_sort

list1: list[int] = [-500, -501, 5, 12, 32, 0, -4, 4, 56564, -432]
bubble(list1)

print("Отсортированный список 1: ", list1)
print("Отсортированный список 1: ", bubble([-1, -5]))