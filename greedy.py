n = 3
lost = [1]
reserve = [1]
count = 0
temp = len(lost)
total = 0

for i in range(len(lost)):  #잃어버린 학생이
    for j in range(len(reserve)): # 빌려줄 수 있는 학생을 돌면서 체육복을 빌린다
        if len(lost) == 0 or len(reserve) == 0: #체육복을 다 빌렸거나, 빌려줄 수 있는 학생이 없으면 break
            break
        #print(lost[i], reserve[j])
        if lost[i] - 1 == reserve[j] or lost[i] + 1 == reserve[j]: #잃어버린 학생이 체육복을 빌렸으면
            lost.remove(lost[i]) #빌린 학생과
            reserve.remove(reserve[j]) #빌려준 학생을 리스트에서 제외시킨다
            count += 1 # 체육복을 빌린 학생 수 증가
            #print(lost, reserve)
total = n - temp + count # 체육수업을 들을 수 있는 학생: 전체학생수 - 체육복을 잃어버린 학생 수 + 체육복을 빌린 학생 수
print(total)