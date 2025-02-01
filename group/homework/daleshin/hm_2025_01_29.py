test_nums: list[int]  = [12, 32, 0, -4, 4, 564564, 63, 5976]
# test_nums.sort()

for _ in range(len(test_nums) - 1):
    for element_index in range(len(test_nums) - 1): # отнимаю 1, чтобы не ссылаться на неусуществующий индеск 
            if test_nums[element_index] > test_nums[element_index + 1]:
                test_nums[element_index], test_nums[element_index + 1] = test_nums[element_index + 1], test_nums[element_index] # меняю местами в списке значения

print(test_nums)