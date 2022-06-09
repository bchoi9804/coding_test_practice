def solution(n):
    L = list(map(int, str(n)))
    answer = 0
    for i in L:
        answer += i
    return answer   

print(solution(987))