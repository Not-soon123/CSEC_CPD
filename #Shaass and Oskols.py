def count_birds_after_shots(n, birds, m, shots):
    for xi, yi in shots:
        xi -= 1  # Convert to 0-based index for easier access
        yi -= 1  # Convert to 0-based index for easier access
        
        # Calculate how many birds will jump to the wire above (if any)
        if xi > 0:  # There is a wire above
            birds[xi - 1] += yi
        
        # Calculate how many birds will jump to the wire below (if any)
        if xi < n - 1:  # There is a wire below
            birds[xi + 1] += birds[xi] - (yi + 1)
        
        # After the shot, all birds on the xi-th wire are gone
        birds[xi] = 0

    return birds

# Input reading
n = int(input())  # Number of wires
birds = list(map(int, input().split()))  # Birds on each wire
m = int(input())  # Number of shots

shots = []
for _ in range(m):
    x, y = map(int, input().split())
    shots.append((x, y))

# Process the shots
final_bird_counts = count_birds_after_shots(n, birds, m, shots)

# Output the final number of birds on each wire
for bird_count in final_bird_counts:
    print(bird_count)
