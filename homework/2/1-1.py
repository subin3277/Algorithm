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
    

A='A SIMPLE STRING TO BE ENCODED USING A MINIMAL NUMBER OF BITS'
count = []
B = countft(A)
for i in range(len(count)):
    print(count[i],end = ' ')
