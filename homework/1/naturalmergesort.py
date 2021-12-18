def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a)//2
    left, right = merge_sort(a[:mid]), merge_sort(a[mid:])
    return merge(left, right, a.copy())


def merge(left, right, merged):
    left2, right2 = 0, 0
    while left2 < len(left) and right2 < len(right):
        if left[left2] <= right[right2]:
            merged[left2+right2]=left[left2]
            left2 += 1
        else:
            merged[left2 + right2] = right[right2]
            right2 += 1
    for i in range(left2, len(left)):
        merged[i + right2] = left[i]
    for j in range(right2, len(right)):
        merged[left2 + j] = right[j]
    return merged

def checkSort(a, n):
    isSorted = True
    for i in range(0, n-1):
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

for i in range(N):
    a.append(random.randint(1, N))
start_time = time.time()
a = merge_sort(a)
end_time = time.time() - start_time
print("자연 합병정렬의 실행 시간 (N=%d) : %0.3f"%(N, end_time))
checkSort(a, N)
