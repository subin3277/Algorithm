def quickSort(a, l ,r):
    if(r>l):
        i = partition(a,l,r)
        quickSort(a,l,i-1)
        quickSort(a,i+1,r)
    return a

def partition(a, l ,r):
    v = a[r]
    i = l-1
    j = r
    while (True):
        i +=1
        while a[i]<v:
            i+=1
        j -=1
        while a[j]>v:
            j -=1
        if(i>=j) :
            break
        temp = a[i]
        a[i] = a[j]
        a[j] = temp
    temp2 = a[i]
    a[i] = a[r]
    a[r] = temp2
    return i

a= [-1,6,2,8,1,3,9,4,5,10,7]
quickSort(a, 1,10)
for i in range(1,11):
    print(a[i], end=' ')
