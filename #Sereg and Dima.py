card = int(input())  # Number of cards
No0f_card = list(map(int, input().split()))  # List of cards

# Initialize scores for Sereje and Dima
sereje = 0
Dima = 0

# Iterate over the list of cards from both ends
left = 0
right = card - 1

for i in range(card):
    if i % 2 == 0:  # Sereje's turn (even turns)
        if No0f_card[left] > No0f_card[right]:
            sereje += No0f_card[left]
            left += 1  # Move the left pointer
        else:
            sereje += No0f_card[right]
            right -= 1  # Move the right pointer
    else:  # Dima's turn (odd turns)
        if No0f_card[left] > No0f_card[right]:
            Dima += No0f_card[left]
            left += 1  # Move the left pointer
        else:
            Dima += No0f_card[right]
            right -= 1  # Move the right pointer

# Print the final scores
print(sereje, Dima)
