def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer

def soluion(left, right):
    return sum([-n if int(n**0.5)==n**0.5 else n for n in range(left, right+1)])
