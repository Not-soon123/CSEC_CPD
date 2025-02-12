No_of_game_played = int(input()) 
winner = input() 

Anton = 0
Danik = 0


for i in winner:
    if i == "A":
        Anton += 1
    elif i == "D":
        Danik += 1

if Anton > Danik:
    print("Anton")
elif Danik > Anton:
    print("Danik")
else:
    print("Friendship")
