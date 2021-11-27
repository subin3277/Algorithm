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

def dadft(a):
    min=100
    minid = -1
    min2=100
    min2id = -1
    while(True):
        for i in range(27):
            if((count[i]<=min2)and(count[i]>0)):
                if(count[i]<=min):
                    min2 = min
                    min2id = minid
                    min = count[i]
                    minid = i
                else :
                    min2 = count[i]
                    min2id = i
        if(min2 == 100):
            break;
        count.append(min+min2)
        count[minid]=0
        count[min2id]=0
        min=100
        minid = -1
        min2=100
        min2id = -1
    
    

A='A SIMPLE STRING TO BE ENCODED USING A MINIMAL NUMBER OF BITS'
count = [] 
dad = []
for i in range(len(count)):
    dad.append(0)
    print(count[i])
