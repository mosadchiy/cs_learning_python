def sum_func(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sum_func(arr[1:])


print(sum_func([2, 4, 6, 5]))
