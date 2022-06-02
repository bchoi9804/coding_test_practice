num = 626331

count = 0
while num != 1 or count == 500:
    if num % 2 == 0:
        num = num // 2
        #print(num)
    else:
        num = num * 3 + 1
        #print(num)
    count += 1

#if count < 500:
#    print(count)
#else: 
#    print(-1)       

print(count) if count < 500 else print(-1)                  