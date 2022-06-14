# def solution(arr):
#     arr = set(arr)
#     return [int(a) for a in arr]

def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i == len(arr)-1:
            answer.append(arr[i])
        else:
            if arr[i] != arr[i+1]:
                answer.append(arr[i])
    return answer               

print(solution([1,1,3,3,0,1,1]))    
print(solution([4,4,4,3,3]))   