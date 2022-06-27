def solution(numbers):
    answer = 45
    for i in range(len(numbers)):
        if 1 <= numbers[i] <= 9:
            answer -= numbers[i]
    return answer

print(solution([1,2,3,4,6,7,8,0]))
print(solution([5,8,4,0,6,7,9]))                