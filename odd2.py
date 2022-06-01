s = "try hello world"

s= s.split(" ")
#print(s)

for k in range(len(s)): #문장 속 단어 수만큼 반복 3 = [0,1,2]
    s_list = list(s[k]) # 단어별 리스트 생성
    for i in range(len(s_list)): #각 단어당 수만큼 반복
        if i % 2 == 0: #짝수일때 (0포함)
            s_list[i] = s_list[i].upper() #대문자 전환 후 대체
        elif i % 2 == 1:
            s_list[i] = s_list[i].lower() #소문자 전환 후 대체
    s[k] = ''.join(s_list) #각 단어 합침
answer = " ".join(s) # 문장 합침
print(answer)                