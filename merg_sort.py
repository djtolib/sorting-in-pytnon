def mergesort(A):
    M = len(A) // 2 
    if M == 0:
        return A                                    # Пустой массив. Сортировать нечего!!!
    return merge(mergesort(A[:M]), mergesort(A[M:])) # Для левой и правой части массива вызовим mergsort а затем результат "мерджим" :)
def merge(L, R):
    C = []
    while L or R:                   #Пока хотябы в одном массиве ест елемент...
        if not L:                   #Если в L нет элементов то в R обязательно есть, блгодаря условию цикла
            C.append(R.pop(0)) 
        elif not R:                 #Как в случае с L. Но только это не L a R
            C.append(L.pop(0))
        else:                       #Иначе элементы есть и в L и в R. С помощью if запишем меньшего.
            if L[0]<=R[0]:          
                C.append(L.pop(0))
            else:
                C.append(R.pop(0))                
    return C   
### ~~~ Проверим на примере: ~~~ ###
example_arr = [100, 0, 20, 45, 100, 20, -1]
res = mergesort(example_arr)
print('Input array:\n',example_arr,'\nSorted array:\n',res)
