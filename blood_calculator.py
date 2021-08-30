#blood_calculator.py
def interface() :
    print ("Blood Calcualtor")
    keep_running=True
    while keep_running:
        print ("Make choice")
        print("9 - Quit")
        choice = int(input("Make a choice: "))
        print(type(choice))
        if choice == 9:
            keep_running=False

    print(choice)
    return choice

interface()