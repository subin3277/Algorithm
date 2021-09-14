def selectionSort(a, n):
    for i in range (0,n):
        minIndex = i
        for j in range (i+1,n):
            if (a[j] < a[minIndex]):
                minIndex = j
        temp = a[i]
        a[i]= a[minIndex]
        a[minIndex] = temp
    return a

a = [3,2,5,1,4]
n = len(a)
res = selectionSort(a,n)
for i in range(n):
    print(res[i], end = ' ')
