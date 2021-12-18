def countft(a):
    for x in range(27):
        count.append(0)
    for i in range(len(a)):
        word = ord(a[i])
        if (word!=32):
            loca = ord(a[i]) - 64
        else :
            loca = 0
        count[loca] = count[loca]+1

def newcountft():
    min1=100
    min2=100
    min1id=-1
    min2id=-1
    while(True):
        for i in range(len(count)):
            if cp[i]<min1 and cp[i]>0:
                min1 = count[i]
                min1id=i
            elif cp[i]<min2 and cp[i]>0:
                min2 = count[i]
                min2id = i
        if min1id==-1 or min2id==-1:
            break
        sum = min1+min2
        dad[min1id]=len(count)
        dad[min2id]=len(count)*(-1)
        count.append(sum)
        cp.append(sum)
        dad.append(0)
        cp[min1id]=0
        cp[min2id]=0
        min1=100
        min2=100
        min1id=-1
        min2id=-1    
    
def makeft():
    for k in range(27):
        i=x=0
        j=1
        if(count[k]):
            q=dad[k]
            while q:
                if q<0:
                    x+=j
                    q=-q
                q=dad[q]
                j+=j
                i+=1
        code[k]=x
        length[k]=i
        
A='A SIMPLE STRING TO BE ENCODED USING A MINIMAL NUMBER OF BITS'
count = []
cp=[]
dad = []
code = []
length=[]
countft(A)
cp=count.copy()
for i in range(len(count)):
    print(count[i],end=' ')
print('\n')
for i in range(len(count)):
    dad.append(0)
    code.append(0)
    length.append(0)
newcountft()
for i in range(len(count)):
    print(count[i],end=' ')
print('\n')
for i in range(len(dad)):
    print(dad[i],end=' ')
print('\n')    
makeft()
for i in range(len(code)):
    print(code[i],end=' ')
print('\n')
for i in range(len(length)):
    print(length[i],end=' ')
