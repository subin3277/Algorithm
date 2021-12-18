class PQ:
    def __init__(self):
        self.heap = [0]*100
        self.info = [0]*100
        self.n = 0

    def insert(self, v, x):
        self.n += 1
        i = self.n
        while True:
            if i == 1: break
            if v >= self.heap[int(i/2)]: break
            self.heap[i] = self.heap[int(i/2)]
            self.info[i] = self.info[int(i/2)]
            i = int(i/2)
        self.heap[i] = v
        self.info[i] = x

    def remove(self):
        x = self.info[1]
        temp_v = self.heap[self.n]
        temp_x = self.info[self.n]
        self.n -= 1
        i = 1
        j = 2
        while j <= self.n:
            if (j < self.n) and (self.heap[j] > self.heap[j+1]):
                j += 1
            if temp_v <= self.heap[j]: break
            self.heap[i] = self.heap[j]
            self.info[i] = self.info[j]
            i = j
            j *= 2
        self.heap[i] = temp_v
        self.info[i] = temp_x
        return x

    def isEmpty(self):
        if self.n == 0: return True
        else: return False

def index(c):
    if ord(c) == 32: return 0
    else: return (ord(c)-64)

def makeHuffman(t, m):
    for i in range(m):
        count[index(t[i])] += 1
    for i in range(27):
        if count[i]:
            pq.insert(count[i], i)
    i = 27
    while not pq.isEmpty():
        t1 = pq.remove()
        t2 = pq.remove()
        dad[i] = 0
        dad[t1] = i
        dad[t2] = -i
        count[i] = count[t1] + count[t2]
        if not pq.isEmpty():
            pq.insert(count[i], i)
        i += 1
    for k in range(27):
        i = x = 0
        j = 1
        if count[k]:
            q = dad[k]
            while q:
                if q < 0:
                    x += j
                    q = -q
                q = dad[q]
                j += j
                i += 1
        code[k] = x
        length[k] = i


def encode(t, m):
    huffman_code = ''
    for j in range(m):
        i = length[index(t[j])]
        while i > 0:
            huffman_code += str((code[index(t[j])] >> i - 1) & 1)
            i -= 1
    return huffman_code

def decode(t):
    string = ''
    i=0
    while(i<len(t)):
        j=i+6
        state = True
        while(j-i>2):
            binary = t[i:j]
            intbinary = int(binary,2)
            for k in range(27):
                if ((j-i)==length[k]) and (intbinary==code[k]):
                    if(chr(k+64)=='@'):
                        string += ' '
                    else :
                        string += chr(k+64)
                    i+=j-i-1
                    state == False
                    break
            if state == False:
                break
            j-=1
        i+=1
    return string
    

text = 'A SIMPLE STRING TO BE ENCODED USING A MINIMAL NUMBER OF BITS'
count = [0]*100
dad = [0]*100
length = [0]*27
code = [0]*27
M = len(text)
pq = PQ()
makeHuffman(text, M)
en = encode(text, M)
print('인코딩 결과 : ')
print(en)
print()
print('count[k] : ')
for i in range (27):
    print(count[i],end=' ')
print('\n')
print('dad[k] : ')
for i in range (len(dad)):
    print(dad[i],end=' ')
print('\n')
print('length[k] : ')
for i in range (len(length)):
    print(length[i],end=' ')
print('\n')
print('code[k] : ')
for i in range (len(code)):
    print(code[i],end=' ')
print('\n')
print('디코딩 결과 : ')  
print(decode(en))
