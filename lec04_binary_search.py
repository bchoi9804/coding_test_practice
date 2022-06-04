def solution(L, x):
    answer = -1 #default x가 L안에 없을 때 반환
    lower = 0
    upper = len(L)-1
    if x in L:
        while lower > upper:
            middle = (lower + upper) //2 # 중간값
            if L[middle] == x:
                answer = middle
                break
            elif L[middle] < x:
                lower = middle + 1
            else:
                upper = middle - 1
    return answer    


#bisect 이진탐색 
# 
#def solution(L, x):
# lower , upper = 0, len(L)-1
# 
# while lower <= upper: # 조건이 참일 동안 반복
#   mid = (lower+upper)//2
#   if x == L[mid]:
#       return mid
#   elif x > L[mid]:
#       lower = mid+1
#   else:
#       upper = mid-1
# return -1  