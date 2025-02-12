# Take input for Limak's and Bob's weights
Weight_of_Limak, Weight_of_Bob = map(int, input().split())

# Initialize the year counter
Year = 0

# Run the loop until Limak's weight is greater than or equal to Bob's weight
while Weight_of_Limak <  Weight_of_Bob:
    Weight_of_Limak = 3*Weight_of_Limak
    Weight_of_Bob = 2*Weight_of_Bob
    Year += 1

# Output the number of years it takes for Limak to have a higher weight than Bob
print(Year)
