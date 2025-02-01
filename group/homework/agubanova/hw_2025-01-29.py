# Написать пузырьковую сортровку

# [12, 32, 0, -4, 4, 564564]
# [12, 0, 32, -4, 4, 564564]
# [12, 0, -4, 32, 4, 564564]
# [12, 0, -4, 4, 32, 564564]
# [12, 0, -4, 4, 32, 564564]

spisok_num: list = [12, 32, 0, -4, 4, 564564]
for i in range(len(spisok_num) - 1):
    for k in range(len(spisok_num) - i - 1):
        if spisok_num[k] > spisok_num[k + 1]:
            spisok_num[k], spisok_num[k + 1] = spisok_num[k + 1], spisok_num[k]
print(spisok_num)