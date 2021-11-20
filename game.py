Name=str(input("Enter your Name:"))
print("Hi",Name,"lets Play")

while True:
    username=input ("Your answer 1:")
    if username=="4":
        print("correct answer\n")
    else:
        print("wrong answer  , hint:the answer is bewtween 0-9\n")
        
    password=input ("Your answer 2:")
    if password=="8":
        print("correct answer\n")
    else:
        print("wrong answer  , hint:bigger than 5\n")
        
    if username=="4" and password=="8":
        a="You Won"
        center = a.center(185,'*')
        print("",center)
        break
    elif username=="e":
        break
    elif password=="e":
        break
    else:
        print("wrong  , hint:the answer is less than 9\n")

        
    
