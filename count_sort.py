import random
import timeit


def count_sort(a):
    if len(a) <= 1:
        return a
    a_max = a_min = a[0]
    for x in a:
        if x < a_min:
            a_min = x
        elif x > a_max:
            a_max = x
    res = []
    for i in range(a_max - a_min + 2):
        res.append(0)
    for x in a:
        res[x - a_min] += 1
    a = []
    for i, x in enumerate(res):
        if x:
            for j in range(x):
                a.append(i + a_min)
    return a


inp = list(range(10**6))
random.shuffle(inp)
time = timeit.default_timer()
a = count_sort(inp)
res = timeit.default_timer() - time
print("Generated array:\n")
print(inp)
print("Sorted array:\n", a)
print(f"Sorting time: {res}")
