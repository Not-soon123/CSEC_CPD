n = int(input())
value = 0
if 1<=n<=1000:
    for _ in range(n):
        Petya,Vasya,Tonya = list(map(int,input().split()))
        Problem_solved = Petya + Vasya + Tonya
        if Problem_solved >= 2:
            value +=1
print(value)
        
        
 
 
