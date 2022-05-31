def solution(n):
    odd: "수"
    even: "수박"
    if n % 2 == 0:
        return even * (n//2)
    else:
        return even * (n//2) + odd    
         