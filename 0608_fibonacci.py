# def fibonacci_recur(n):
#     if n == 0: 
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci_recur(n-2) + fibonacci_recur(n-1)

#분기문 아직 잘 모르겠다 ㅠ
def fibonacci_iter(n):
    if n >= 0: # 양의 정수일때
        answer = 0
        temp1 = 1
        temp2 = 1
        for i in range(2, n-2):
            answer = n-2 + n-1
            temp1 = n-1
            temp2 = answer
        return answer    

#n = int(input()) 
print(fibonacci_iter(10))

