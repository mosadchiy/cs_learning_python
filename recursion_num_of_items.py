def num_of_items(arr):
    if len(arr) == 0:
        return 0
    return 1 + num_of_items(arr[1:])


print(num_of_items([2, 4, 6, 5]))
