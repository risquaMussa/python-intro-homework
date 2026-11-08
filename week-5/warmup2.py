#Warmup 2: Input Validation with a While Loop
while True:
    try:
        number = int(input("Enter a positive integer: "))
        if number > 0:
            print(f"Got it: {number}")
            break
        else: 
         print("That's not a positive integer. Try again.")  
    except ValueError:
        print("That's not a positive integer. Try again.")
    


#number = input("Enter a positive integer: ")
#while not number.isdigit() or int(number) <= 0:
    #print("that is not a postive integer try again")

    #number = int(input("enter a postive integer"))
    #print(f"got it: {number}"")
    


    