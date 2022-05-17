def max (arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    max_sub = max(arr[1:])    
    return arr[0] if arr[0] > max_sub else max_sub

print(max([23, 45, 21, 43, 54]))