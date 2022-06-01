def solution(strings, n):
    answer = []
    result = []
    for s in strings:
        s = s[n] + s
        answer.append(s)
    answer = sorted(answer)

    for i in answer:
        i = i[1:]
        result.append(i)
    return result    
