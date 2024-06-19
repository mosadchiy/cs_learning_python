def binary_search(arr, item_to_find):
    if len(arr) == 1:
        if arr[0] == item_to_find:
            print("item found: ", item_to_find)
            return
        return
    mid_index = int((0 + len(arr) - 1) / 2)
    binary_search(arr[0:mid_index + 1], item_to_find)
    binary_search(arr[mid_index + 1:], item_to_find)


my_list = [1, 2, 3, 4, 5]
item = 3
print("input array: ", my_list)
print("item to find: ", item)
binary_search(my_list, item)
