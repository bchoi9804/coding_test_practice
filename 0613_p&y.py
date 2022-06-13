# def solution(s):
#     s = [a for a in str(s)]
#     y_cnt = 0
#     p_cnt = 0

#     for a in s:
#         if a == 'p' or a == 'P':
#             p_cnt += 1
#         elif a == 'y' or a == 'Y':
#             y_cnt += 1

#     if p_cnt != y_cnt:
#         return False
#     else:
#         return True                    





def solution2(s):
    return s.lower().count('p') == s.lower().count('y') #대소문자 구분이 없으므로 모두 소문자로 변환해서 비교한다.

print(solution2("pPoooyY"))
print(solution2("Pyy"))    