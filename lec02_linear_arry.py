def solution(L, x):
    if x > L[-1]: # 예외를 먼저 처리하는 것이 관건
        L.append(x) # x가 가장 큰 원소일때
    else:
        for i in range(len(L)): # 그 외
            if x <= L[i]: 
                L.insert(i, x) # i가 인덱스 자체
                break
    return L
