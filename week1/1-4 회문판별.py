def isPalindrome(s):
    i = 0
    j = len(s)-1
    while i<j:
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True

s = input('s = ')
if isPalindrome(s):
    print('회문')
else :
    print('회문아님')
