def insertionSort(a, n):
    for i in range(2,n+1):
        print(i)
        v= a[i]
        j=i
        while(a[j-1] > v):
            a[j]=a[j-1]
            j-=1
        a[j]=v

a=[3,2,5,1,4]
insertionSort(a, len(a))
for i in range(len(a)):
    print(a[i],end =' ')
            
