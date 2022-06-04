def solution(n, lost, reserve):
    answer = 0

    reserve_del = set(reserve) - set(lost) # 체육복을 빌려줄 수 있는 사람이 체육복을 잃어버렸을 때 공통요소를 - 연산자를 이용해 제거
    lost_del =set(lost)-set(reserve) # 겹치는 수를 양쪽 리스트에서 모두 지워야 한다.

    for i in reserve_del:
        if i-1 in lost_del:
            lost_del.remove(i-1)

        elif i+1 in lost_del:
            lost_del.remove(i+1)

    answer = n - len(lost_del)

    return answer