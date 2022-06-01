#s = [5,7,9,4,6]
#s.sort(reverse=True)
#print(s[:-1])

s = [4,3,2,1]
#print(min(s))
s.remove(min(s))
#print(s)

def solution(s):
    if len(s) > 1:
        return s
    else:
        return [-1]    
