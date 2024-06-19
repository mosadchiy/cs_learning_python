def max_number(arr):
    if len(arr) == 0:
        return 0
    cur_max = arr[0]
    new_max = max_number(arr[1:])
    if cur_max >= new_max:
        return cur_max
    else:
        return new_max


print(max_number([2, 4, 6, 5]))
