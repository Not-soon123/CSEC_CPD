N0of_stone = int(input())
color = input()
count = 0


for i in range(1, N0of_stone):
    if color[i] == color[i - 1]:
        count += 1

print(count)
