def bubbleSort(a, n):
    for i in range(n, 2, -1):
        for j in range(1, i):
            if(a[j]>a[j+1]):
                temp = a[j]
                a[j]=a[j+1]
                a[j+1]=temp
    return a

A = [3,2,5,1,4]
res = bubbleSort(A, len(A)-1)
for i in range(len(A)):
    print(res[i],end=' ')
