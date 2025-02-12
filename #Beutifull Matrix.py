# Read the 5x5 matrix
matrix = [list(map(int, input().split())) for _ in range(5)]

# Find the position of '1' in the matrix
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            x, y = i + 1, j + 1  # 1-based indexing
            break

# Calculate the minimum moves to bring (x, y) to the center (3, 3)
moves = abs(x - 3) + abs(y - 3)

# Output the result
print(moves)

