n = 12345
a = list(str(n))

result = []
for i in a:
    result.append(int(i))

result.reverse()
print(result)    

#a.sort(reverse=True) 내림차순이 아니라 뒤집기

