def count_list(arr):
    if arr == []: return 0
    else: return 1 + count_list(arr[1:])
    
print(count_list([1, 2, 3, 5, 6]))