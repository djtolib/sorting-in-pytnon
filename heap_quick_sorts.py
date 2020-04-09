""" binary_search(x, array, start=None, end=None) -> int
insertion_sort(array) -> NoneType
merge_sort(array, start=None, end=None) -> list (is not array)"""


# Quic sort begin

def quicksort(a, start=None, end=None):
    if len(a) <= 1:
        return
    if start == None:
        start = 0;
        end = len(a) - 1
    if start < end:
        q = partition(a, start, end)
        quicksort(a, start, q - 1)
        quicksort(a, q + 1, end)


def partition(a, start, end):
    x = a[end]
    i = start - 1
    for j in range(start, end):
        if a[j] <= x:
            i += 1
            temp = a[i];
            a[i] = a[j];
            a[j] = temp
    temp = a[i + 1];
    a[i + 1] = a[end];
    a[end] = temp
    return i + 1
# Quick sort end

# Heap sort begin

def down_sift(a, k, n):
    new_elem = a[k]
    while k <= n // 2:
        child = 2 * k
        if child < n and a[child] < a[child + 1]:
            child = child + 1
        if new_elem >= a[child]:
            break
        a[k] = a[child]
        k = child
    a[k] = new_elem


def heap_sort(a):
    size = len(a)
    if size <= 1:
        return
    for i in range(size // 2, -1, -1):
        down_sift(a, i, size - 1)
    for i in range(size - 1, 0, -1):
        temp = a[i];
        a[i] = a[0]
        a[0] = temp
        down_sift(a, 0, i - 1)

# Heap sort end

