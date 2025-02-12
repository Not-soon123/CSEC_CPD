# Grigoriy
# Embosser :- devise that allow to print the next of plastic tape
# Text is printed sequentially character by character
# a devise consists wheel with lower case letter ,and abutton to print the choosen letter
# static poinert initially points to letter "a"
# it allowed to rotate the alphabetic wheel
#  It's not required to return the wheel to its initial position with pointer
#..on the letter 'a'.
# the string is only lower case
#Name0f_Exahabit = input()
#rotation = 0
#for i in Name0f_Exahabit:
   # if i.isalpha():
       # position = ord(i) - ord('a')+1
       # pposition = 26 - (position-1)
      #  if pposition > position:
            #rotation += position
        #else :
           # rotation += pposition
        #rotation += min(position,pposition)
#print(rotation)
# Read input string
Name0f_Exahabit = input().strip()


rotation = 0


current_position = ord('a')


for char in Name0f_Exahabit:
  
    target_position = ord(char)

    
    clockwise_distance = (target_position - current_position) % 26
    counterclockwise_distance = (current_position - target_position) % 26

  
    rotation += min(clockwise_distance, counterclockwise_distance)

    
    current_position = target_position


print(rotation)

