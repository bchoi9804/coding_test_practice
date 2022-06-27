def solution(numbers):
    numbers = sorted(numbers)
    print(numbers)
    answer= [] 
    sum = 0

    for i in range(len(numbers)):
        for j in range(1, len(numbers)):
            print(numbers[i])
            print(numbers[j])
            sum = numbers[i] + numbers[j]
            answer.append(sum)
    
    answer = set(answer)
    answer = list(answer)

    return answer

solution([5,0,2,7])