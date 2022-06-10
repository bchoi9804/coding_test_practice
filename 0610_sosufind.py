# def sosu(x): # 어떤 자연수가 소수인지 판별하는 함수
#     for i in range(2, x): # 2부터 x-1까지의 모든 수를 확인하여
#         if x % i == 0: # 나누어 떨어지면 소수가 아님
#             return False
#     return True

# def solution(n):
#     num = set(range(2, n+1)) # 입력받은 자연수 n을 2부터 n까지 집합으로 만들어서 num변수에 저장
#     print(num) # num 확인

#     for i in range(2, n+1): # 2부터 n까지 모든 수를 확인
#         if i in num: # i가 집합의 원소라면
#             num -= set(range(2*i, n+1, i)) # 집합의 차를 num 변수에 저장
    
#     print(num)
#     return len(num)

# print(solution(10))
# print(solution(5))    

#에라토스테네스의 체(Sieve of Eratosthenes)라는 방법이 사용된 코드 
# n까지의 모든 소수를 구한다고 하면 
# 2를 제외한 모든 2의 배수를 num에서 제거.
# 3을 제외한 모든 3의 배수를 num에서 제거.
# 4는 아까 2에서 제거.
# 5를 제외한 모든 5의 배수를 num에서 제거.
# 이렇게 반복해서 num에 남아 있는 수들이 소수이다.
# 대량의 소수를 한꺼번에 판별하고자 할 때 사용한다.   

#어떠한 자연수가 소수인지 아닌지 판별할 때 약수의 특징을 이용한다.
# 모든 수를 탐색하는 것이 아닌 그 수의 제곱근까지만 확인해서 소수를 판별할 수 있다.

import math

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

print(is_prime_number(123565422))   
print(is_prime_number(571))              