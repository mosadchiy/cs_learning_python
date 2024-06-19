def binary_search(arr, item_to_find):
    if len(arr) == 0:
        return
    low = 0
    high = len(arr) - 1
    mid = int((low + high) / 2)
    guess = arr[mid]
    if guess == item_to_find:
        print("item found: ", item_to_find)
        return
    if guess > item_to_find:
        binary_search(arr[0:mid], item_to_find)
    else:
        binary_search(arr[mid + 1:], item_to_find)


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
item = 3
print("input array: ", my_list)
print("item to find: ", item)
binary_search(my_list, item)
