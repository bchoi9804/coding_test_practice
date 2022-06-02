def solution(s, n):
    answer = ''
    for x in s:
        if x == ' ':
            answer += ' '
        else:
            if x.isupper():
                answer += chr((ord(x)-ord('A')+n) % 26 + ord('A'))    
            elif x.islower():
                answer += chr((ord(x)-ord('a')+n) % 26 + ord('a'))
    print(answer)

#string.ascii_uppercase
#string.ascii_lowercase     

#대소문자 구분
# chr((ord(x)-ord('a')+n)%26+ord('a')) <- 이 알고리즘에 대한 이해 필요               