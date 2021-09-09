def binarySearch(a,key,left,right) :
    
    if left<=right :
        mid = int((left+right)//2)
        if (key == a[mid]) :
            print('key = ',key,end=' ')
            print(', mid = ',mid)
            return mid
        elif key < a[mid] :
            print('key = ',key,end=' ')
            print(', mid = ',mid,end=' ')
            print(', left = ',left,end=' ')
            print(', right = ',mid-1)
            return binarySearch(a,key,left,mid-1)
        else :
            print('key = ',key,end=' ')
            print(', mid = ',mid,end=' ')
            print(', left = ',mid+1,end=' ')
            print(', right = ',right)
            return binarySearch(a,key,mid+1,right)
    else :
        return -1

A = list(range(0,100))
key = int(input('key = '))
print(binarySearch(A,key,1,100))
