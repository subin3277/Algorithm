def CountingSort(a, n, m):
    for j in range (1,m+1):
        count[j]=0
    for i in range (1,n+1):
        count[a[i]]=count[a[i]]+1
    for j in range (2,m+1):
        count[j]=count[j-1]+count[j]
    for i in range (n,0,-1):
        b[count[a[i]]]=a[i]
        count[a[i]]=count[a[i]]-1
    for i in range (1,n+1):
        a[i]=b[i]
    return a


a=[0,1,2,2,1,3,4,4,1]
b=[0,0,0,0,0,0,0,0,0]
count = [0,0,0,0,0]
A=CountingSort(a,8,4)
for i in range (1,9):
    print(a[i],end=' ')
