s = [5,7,9,4,6]

for j in range(len(s)):
    for i in range(len(s)-1):
        temp = 0
        if s[i] < s[i+1]:
            temp = s[i]
            s[i] = s[i+1]
            s[i+1] = temp
print(s)         

def solution(s):
    if len(s) > 1:
        for i in range(len(s)):
            for j in range(len(s)-1):
                temp = 0
                if s[j] < s[j+1]:
                    temp = s[j]
                    s[j] = s[j+1]
                    s[j+1] = temp
        return s[:-1]
    else:
        return [-1]  