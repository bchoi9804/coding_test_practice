s = "try hello world"

#  공백, 짝수-대문자, 홀수-소문자

#단어별로 분리하기
#split: 공백을 기준으로 문자열을 나누어서 리스트로 반환

s = s.split(" ")
print(s)

answer = []
for word in s:
    for i in range(len(word)): #인덱싱할때는 len함수로
        if i % 2 == 0 or i == 0: # 인덱스자리가 홀수일때 
            answer.append(word[i].upper())
        else: #0+짝수
            answer.append(word[i].lower())
    answer.append(" ")            
print(answer)
print("".join(answer))                 