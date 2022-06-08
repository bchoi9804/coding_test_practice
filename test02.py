#미완성
import itertools

diet = [[360,138,338],[230,102,311],[320,474,214],[131,498,484],[366,176,249],[323,407,116],[265,433,317]]

#sum = (min(diet[0]))
temp = []
for day in diet:
    for cal in day:
        temp.append(cal)
print(temp[1::3])

d_one = temp.index(min(temp[0:3])) #1일 식단 중 가장 적은 cal's idx
sum = d_one
for i in range(len(temp)//3):
    sum += temp[i]
    [d_one:d_one+i]





#print(len(list(itertools.combinations(range(3,1001),3))))