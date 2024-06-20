def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


my_list = [10, 5, 2, 3]
print("input array: ", my_list)
print("sorted array: ", quick_sort([10, 5, 2, 3]))
