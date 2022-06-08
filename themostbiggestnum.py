def solution(numbers):
    answer = ''
    mylist = []
    for i in range(len(numbers)):
        mylist.append(str(numbers[i]))
    
    s = sorted(mylist, key=lambda x : x[0], reverse=True)
    return ''.join(s)





    #return answer
print(solution([6,10,2]))    
