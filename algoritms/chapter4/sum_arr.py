def sum_arr(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sum_arr(arr[1:])

print(sum_arr([2, 4, 6]))