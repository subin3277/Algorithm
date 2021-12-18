import sys
sys.setrecursionlimit(10000)
import random, time

def mergeSort(a,l,r):
    if(r > l):
        m = (r+l)//2
        mergeSort(a,l,m)
        mergeSort(a,m+1,r)
        merge(a,l,m,r)

def merge(a,l, m, r):
    i=l
    j=m+1
    k=l
    b=a.copy()
    while((i<=m)and(j<=r)):
        if(a[i]<a[j]):
            b[k]=a[i]
            k+=1
            i+=1
        else:
            b[k]=a[j]
            k+=1
            j+=1
    if(i>m):
        for p in range (j, r+1):
            b[k]=a[p]
            k+=1
    else :
        for p in range (i,m+1):
            b[k]=a[p]
            k+=1
    for p in range (l,r+1):
        a[p]=b[p]

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


N = 5000
a = []
a.append(None)
for i in range(N):
    a.append(random.randint(1, N))
start_time = time.time()
mergeSort(a,1,N)
end_time = time.time() - start_time
print("합병 정렬의 실행 시간 (N=%d) : %0.3f"%(N, end_time))
checkSort(a, N)
