numbers = [100, 101, 102, 103, 104]
start = [1,2]
finish = [2,4]
sum1 = 0
sum2 = 0
answer = []

sum1=(sum(numbers[start[0]:finish[0]+1]))
sum2=(sum(numbers[start[1]:finish[1]+1]))
answer.append(sum1)
answer.append(sum2)
print(answer)
