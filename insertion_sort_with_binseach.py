from random import *

def insertion(A):
    res = []
    for x in A:
        i = len(res)
        if i == 0:
            res.append(x)
        elif res[i - 1] < x:  # Добавим в конец.
            res.append(x)
        elif res[0] > x:  # Когда хотим сдвинуть массив, нужно добавить хоть чего небудь
            res.append(10000)  # иначе будет out of range.
            while i > 0:  # В этом случае нужно добавить перед первым.
                res[i] = res[i - 1]
                i -= 1
            res[0] = x
        else:
            res.append(20000)  # В этом случае нужно добавить между двумя элементами.
            i = len(res) - 1
            while not (res[i] >= x >= res[i - 1]):
                res[i] = res[i - 1]
                i -= 1
            else:
                res[i] = x
    return res


def search(A, x):
    A = insertion(A)
    l = 0;
    r = len(A) - 1
    if A[0] > x or A[len(A) - 1] < x:  # Здесь очевидно что если искомый x больше последнего
        return -1  # или меньше первого элемента, то его точно нет в массиве.
    while True:
        m = (l + r) // 2
        if x < A[m]:
            r = m - 1
        elif x > A[m]:
            l = m + 1
        else:
            return m
        if l > r:
            return -1


try:
    n = int(input('Введите длину массива: '))
except:
    print('Некоррекное число!')
in_arr = []

for i in range(n):
    in_arr.append(randint(-100, 100))
print('Сгенерировали:\n', in_arr)
print('Отсортировали:\n', insertion(in_arr))
try:
    x = int(input('Чего хотим искать? '))
except:
    print('Некоррекное число!')

if in_arr:
    res = search(in_arr, x)
    if res == -1:
        print('Искали, искали, но ненашли! :(')
    else:
        print('Вот, вот он!!! A[', res, ']', sep='')
