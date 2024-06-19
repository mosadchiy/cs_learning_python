def max_number(arr):
    if len(arr) == 0:
        return 0
    cur_max = arr[0]
    new_max = max_number(arr[1:])
    return cur_max if cur_max >= new_max else new_max


print(max_number([2, 4, 6, 5]))
