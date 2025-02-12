# k burles
# there are unlimited number of shovel in the shop
# minimem number of the shovel Polcarp has to buy so that he can pay with out chang
# should buy atleast one shovel

k, r = map(int, input().split())

# We iterate over the number of shovels
for n in range(1, 11):
    total_cost = n * k
    # Check if the total cost ends in 0 or r
    if total_cost % 10 == 0 or total_cost % 10 == r:
        print(n)
        break
