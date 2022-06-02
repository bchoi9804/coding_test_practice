n = 121


#if n == pow(x,2):
#    return pow(x + 1, 2)
x = 0
for i in range(1, n+1): # 나누거나 곱할때는 1
    if n % i == 0:
        if i * i == n:
            x = i
print(x)

# 제곱근 계산 : number ** (1/2)
# import math -> math.sqrt()
# import cmath -> cmath.sqrt() -> 복소수에 대한 제곱근도 구할 수 있다.