def mergeSort(a,l,r):
    if(r > l):
        m = (r+l)/2
        mergeSort(a,l,m)
        mergeSort(a,m+1,r)
        merge(a,l,m,r)

def merge(a,low, mid, high):
    temp = []
    l, h = low, mid
    while l < mid and h < high:
        if a[l] < a[h]:
            temp.append(a[l])
            l += 1
        else:
            temp.append(a[h])
            h += 1

    while l < mid:
        temp.append(a[l])
        l += 1
    while h < high:
        temp.append(a[h])
        h += 1

    for i in range(low, high):
        a[i] = temp[i - low]
    return a

a= [6,2,8,1,3,9,4,5,10,7]
mergeSort(a,0,9)
for i in range(10):
    print(a[i], end=' ')
