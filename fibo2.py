def solution(x):
    a = 1
    b = 1
    if x == 1 or x == 2:
        return 1
    elif x == 0:
        return 0
    else:
        for i in range(1,x):
            a, b = b, b+a # 이전값+전전값을 더하는 방식
        return a

print(solution(20))                                        