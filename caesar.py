s = "a B z Z sg se"
n = 4

C = "ABCDEFGHIJKLMNOPQRSTUVWXY" 
c = "abcdefghijklmnopqrstuvwxy"

#print(len(C))

answer = ''
for i in range(len(s)): #믄자열 길이만큼 반복
    if s[i] in C or s[i] in c:
        x = ord(s[i]) + n
        answer += chr(x)
    elif s[i] == ' ':
        answer += ' '
    elif s[i] == 'Z':
        y = ord("A")-1 + n 
        answer += chr(y)
    elif s[i] == 'z':
        z = ord("a")-1 + n
        answer += chr(z)

print(answer)    
