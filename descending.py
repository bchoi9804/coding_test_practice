n = 118372

a = str(n)
a = list(a)
print(a)

for i in range(len(a)):
    for j in range(len(a)-1):
        temp = 0
        if a[j] < a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
print(int(''.join(a)))