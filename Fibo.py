def fibo(x):
    if x == 1 or x == 2:
        return 1
    else:
        return fibo(x-1) + fibo(x-2)

print(fibo(10))

mylist = []
for i in range(1,10):
    mylist.append(fibo(i))
print(mylist)