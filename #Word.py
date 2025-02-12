CorrectWord = input()
upper = 0
lower = 0
for Char_ in CorrectWord:
    if Char_.isupper() :
        upper +=1
    elif Char_.islower():
        lower +=1
if upper > lower:
    print(CorrectWord.upper())
elif upper < lower:
    print(CorrectWord.lower())
else :
    print(CorrectWord.lower())
    
        
