def isPrime(a):
    i = 2
    while i<=a/2 :
        if a%i == 0 :
            return False
        i+=1
    return True

A = int(input("a = "))
if isPrime(A):
    print('소수')
else:
    print('소수 아님')
