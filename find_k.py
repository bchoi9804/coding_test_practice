def solution(array, commands):
    answer = []
    for i,j,k in commands:        
        arr = array[i-1:j]
        arr2 = sorted(arr)
        arr3 = arr2[k-1]
        answer.append(arr3)    
    return answer

# def solution(array, commands):
#     answer = []
#     for i,j,k in commands: #[i,j,k]를 원소로 가진 2차원 배열 commands
#         arr = array[i-1:j]
#         arr2 = sorted(arr)
#         arr3 = arr2[k-1]
#         answer.append(arr3)
#     return answer        