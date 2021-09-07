def isPerfect(a):
    s = 0
    i = 1
    while i<= a/2:
        if a%i ==0:
            s+=i
        i+=1
    if s==a:
        return True
    else :
        return False

A = int(input('a = '))
if isPerfect(A):
    print('완전수')
else :
    print('완전수 아님')
