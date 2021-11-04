def bruteForce(p,t,k):
    M = len(p)
    N = len(t)
    i=k
    j=0
    while j < M and i<N:
        if(t[i]!=p[j]):
            i -= j
            j = -1
        i+=1
        j+=1
    if (j == M):
        return i-M
    else :
        return i

t = "ababacabcbababcacacbcaababca"
p = "ababca"
k=0
sum = 0
while True:
    position = bruteForce(p,t,k)
    k = position + len(p)
    if k<len(t):
        sum +=1
        print("위치 : ",position)
    else :
         break
if(sum == 0):
    print(t,end='\0')

