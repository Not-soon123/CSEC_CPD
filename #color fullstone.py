def final_position(s, t):
    # Liss starts on the first stone (index 0)
    position = 0

    # Process each instruction
    for instruction in t:
        # Check if the instruction matches the stone color Liss is currently on
        if s[position] == instruction:
            # Move Liss one stone forward if the colors match
            if position < len(s) - 1:
                position += 1
    
    # Return the final position in 1-based index
    return position + 1

# Input reading
s = input().strip()  # Sequence of stones
t = input().strip()  # Instructions

# Output the final position
print(final_position(s, t))
