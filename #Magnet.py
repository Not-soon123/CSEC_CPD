Number0f_Magnet = int(input())
char_list = []

count = 0
previous = None
for Domain in range(Number0f_Magnet):
    char = int(input().strip())
    char_list.append(char)
    if char_list[Domain] != previous:
        count+=1
        previous = char_list[Domain]
 
    #char_set = set(char_list)
print (count)
