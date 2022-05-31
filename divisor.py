def solution(arr, divisor):
    answer = []
    for element in arr:
        if element % divisor == 0:
            answer.append(element)
        else:
            pass

    if len(answer) != 0:
        return sorted(answer)
    else:
        return [-1]            