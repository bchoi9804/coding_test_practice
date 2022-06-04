def solution(L, x):
    answer = []
    
    if x in L: # x가 리스트 내에 있는 경우
        for i in range(len(L)): # 각 원소를 살펴서
            if L[i] == x: #각 인덱스 값이 x에 해당하는 경우 
                answer.append(i) # 해당 인덱스를 answer에 추가
            else:
                pass
    else: # x가 리스트에 없을 경우
        return [-1]
    
    return answer