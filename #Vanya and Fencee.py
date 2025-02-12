n, h = map(int, input().split())  
width = 0


for _ in range(n):
    ai = list(map(int, input().split())) 
    
   
    for height in ai:
        if height <= h:
            width += 1
        else:
            width += 2

print(width)
