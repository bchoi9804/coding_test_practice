def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

n = int(input())
print(factorial(10))

# def factorial(n):
#     result = 1
#     if n > 0 : # 양의 정수이면
#         result = n * factorial(n-1) # 재귀적 순환 알고리즘 사용
#     return result  


#문제: 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
#입력: 첫째 줄에 정수 N(0<=N<=12)이 주어진다.
#출력: 첫째 줄에 N!을 출력한다.