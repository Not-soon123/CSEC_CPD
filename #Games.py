def count_games_in_guest_uniform(n, teams):
    count = 0
    for i in range(n):
        hi, ai = teams[i]  # home and guest uniform colors of team i
        for j in range(n):
            if i != j:
                _, aj = teams[j]  # guest uniform color of team j
                if hi == aj:  # if home team's home uniform matches guest's guest uniform
                    count += 1
    return count

# Read input
n = int(input())  # number of teams
teams = [tuple(map(int, input().split())) for _ in range(n)]

# Calculate the result
result = count_games_in_guest_uniform(n, teams)

# Output the result
print(result)
