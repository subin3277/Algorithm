def cocktailshakerSort(a, n):
    left = 0
    right = n
    while(left<right):
        for i in range(left+1,right):
            if(a[i]>a[i+1]):
                temp = a[i]
                a[i]=a[i+1]
                a[i+1]=temp
        left+=1    
        for i in range (right-1,left-1,-1):
            if(a[i]>a[i+1]):
                temp = a[i]
                a[i]=a[i+1]
                a[i+1]=temp
        right-=1
    return a

def checkSort(a, n):

    isSorted = True
    for i in range(1, n):
        if a[i] > a[i+1]:
            isSorted = False
        if not isSorted:
            break
    if isSorted:
        print("정렬 완료")
    else:
        print("정렬 오류 발생")


import random, time


N = 5000
a = []
a.append(None)

for i in range(N):
    a.append(random.randint(1, N))
start_time = time.time()
cocktailshakerSort(a, N)
end_time = time.time() - start_time
print("칵테일 쉐이커 정렬의 실행 시간 (N=%d) : %0.3f"%(N, end_time))
checkSort(a, N)
