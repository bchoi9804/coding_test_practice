def solution(array, commands):
    answer = []
    for i,j,k in commands:        
        arr = array[i-1:j]
        arr2 = sorted(arr)
        arr3 = arr2[k-1]
        answer.append(arr3)    
    return answer