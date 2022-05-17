def findMinimum(arr):
    min = arr[0]
    min_index = 0
    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]
            min_index = i
    return min_index

def sort(arr):
    sortArr = []
    for i in range(len(arr)):
        min = findMinimum(arr)
        sortArr.append(arr.pop(min))
    return sortArr


print(sort([56, 43, 77, 564, 87, 11, 22]))