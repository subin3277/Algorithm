def initNext(p):
    m =len(p)
    next[0] = -1
    i=0
    j=-1
    while i<m:
        next[i] = j
        while j>=0 and (p[i]!=p[j]):
            j = next[j]
        i+=1
        j+=1

next=[0]*50
p1 = "ababca"
p2 = "abababca"
p3 = "abcbabcbabc"
p4 = "abracadabra"
initNext(p4)
for i in range(1,len(p4)):
    print(next[i],end = ' ')
