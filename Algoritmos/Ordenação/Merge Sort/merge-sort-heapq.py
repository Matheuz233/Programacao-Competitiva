import heapq


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return list(heapq.merge(left, right))


print(merge_sort([2, 3, 4, 90, 32, 432, 3434, 2344, 34]))
