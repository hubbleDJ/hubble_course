arr = [12, 32, 0, -4, 4, 564564]
n = len(arr)

for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            
            arr[j], arr[j+1] = arr[j+1], arr[j]

print("Отсортированный массив:", arr)