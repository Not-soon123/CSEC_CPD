FirstString = input()
SecondString = input()
if FirstString.lower() == SecondString.lower() :
    print(0)
elif FirstString.lower() > SecondString.lower() :
    print(1)
else:
    print(-1)
