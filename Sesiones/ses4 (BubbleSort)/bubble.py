arr = [2, 1, 3, 4, 5, 3, 9]
arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 20, 11, 52]

for i in range(len(arr)):
    for j in range(len(arr) - i - 1):
        if (arr[j] > arr[j+1]):
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)
            