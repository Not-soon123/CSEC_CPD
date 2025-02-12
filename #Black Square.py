# jury student
# game name blacksquare
# phone screen divided in to 4 vertical strip
# each second a black square appears
# game rule ;- by using the second makeing the Bl..square go away
# when he thech he wasted ai calories on touching i-th strip
# finally :- calculate how many calories Jury need to destroy all squares
# input :- 4 separeated integer in space
# string :- 1 if first...stripe and for all also
a1,a2,a3,a4 = map(int, input().split())


strip = input()

total_calory = 0

update_strip = list(strip)
update_strip.sort()


for i in update_strip:
    if i == "1" :
        total_calory += a1
    elif i == "2":
        total_calory += a2
    elif i == "3":
        total_calory += a3
    else:
       total_calory += a4
print(total_calory)  
