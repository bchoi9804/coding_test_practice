arr1 = [[1,2],[2,3]] # 애초에 행렬 수가 같으니까 반복문을 하나만 써도 됨
arr2 = [[3,4],[5,6]]
answer = []

for i in range(len(arr1)): # n차원 배열 수 만큼 반복
    result = []
    for j in range(len(arr1[i])): # 각 차원의 요소 개수만큼 반복
        result.append(arr1[i][j]+arr2[i][j]) #같은 위치의 값을 더해서 result에 추가하기
    answer.append(result) # 2차원 배열값을 구하기 위해 빈리스트도 2개
    
print(answer)

#2번째 풀이

import numpy as np

def arraysum(arr1, arr2):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    answer = arr1 + arr2
    return answer.tolist()
        