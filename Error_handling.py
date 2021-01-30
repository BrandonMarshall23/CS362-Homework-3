while True:
    try:
        x = input("Please enter an integer: ")
        x = int(x)
        break
    except ValueError:
        print("No valid integer! Please try again ...")
print("Great, you successfully entered an integer!")

 

if(x % 4) == 0:
    if(x % 100) == 0:
        if(x % 400) == 0:
            print("This is a leap year!!!!!")
        else:
             print("This is not a leap year!")
    else:
        print("This is a leap year!!!!!!")
else:
    print("This is not a leap year!")
