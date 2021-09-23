def heapSort(a, n):
    for i in range(n//2,0,-1):
        heapify(a,i,n)
    for i in range(n-1,0,-1):
        temp = a[1]
        a[1]=a[i+1]
        a[i+1]=temp
        heapify(a,1,i)
    return a

def heapify(a, h, m):
    v=a[h]
    j=2*h
    while(j<=m):
        if(j<m and a[j]<a[j+1]):
            j+=1
        if(v>= a[j]):
            break
        else:
            a[j//2]=a[j]
        j=2*j
    a[j//2]=v
    return a

a=[0,6,2,8,1,3,9,4,5,10,7]
a= heapSort(a,len(a)-1)
for i in range(1,len(a)):
    print(a[i], end =' ')
