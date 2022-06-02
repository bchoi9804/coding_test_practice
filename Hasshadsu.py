x = 21

x = str(x)
print(x)

sum = 0
for i in range(len(x)): #문자열일경우에 len함수를 쓰고 인덱싱으로 요소를 얻자!
    sum += int(x[i])
print(sum)

#x =''.join(x)
#print(x)

if int(x) % sum == 0: # 파이썬 True, False 대문자 잊지말자!
    print("true")
else:
    print("false")    