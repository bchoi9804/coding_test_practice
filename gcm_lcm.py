n = 3
m = 12
a = []
r = []
final = []

for i in range(1, n+1): # 최대공약수
    if n % i == 0:
        a.append(i)     
for j in a:
    if m % j == 0:
        r.append(j)

#최소공배수: 두 수를 최대공약수로 나누어서 몫을 구한 뒤 전부 곱한다.
x = max(r) * n // max(r) * m // max(r)
 
final.append(max(r)) # 출력 리스트 [GCM, LCM]
final.append(x)
print(final)