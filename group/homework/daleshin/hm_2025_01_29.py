test_nums: list[int]  = [12, 32, 0, -4, 4, 564564, 63, 5976]
# test_nums.sort()

for i in range(len(test_nums) - 1):
    for k in range(len(test_nums) - 1): # отнимаю 1, чтобы ограничить длину списка, так как у меня дальше есть выражение k+1 , при последжних итерациях выдает ошибку IndexError: list index out of range , потому что ссылается на несуществующий элемент списка
        if test_nums[k] > test_nums[k + 1]:
            test_nums[k], test_nums[k + 1] = test_nums[k + 1], test_nums[k] # меняю местами в списке значения

print(test_nums)