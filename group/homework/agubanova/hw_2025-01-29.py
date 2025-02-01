# Написать пузырьковую сортровку

spisok_num: list = [12, 32, 0, -4, 4, 564564]
for pass_num in range(len(spisok_num) - 1):
    for compare_index in range(len(spisok_num) - pass_num - 1):
        if spisok_num[compare_index] > spisok_num[compare_index + 1]:
            spisok_num[compare_index], spisok_num[compare_index + 1] = spisok_num[compare_index + 1], spisok_num[compare_index]
print(spisok_num)