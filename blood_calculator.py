#blood_calculator.py
def interface() :
    print ("Blood Calcualtor")
    keep_running=True
    while keep_running:
        print ("Make choice")
        print("1- HDL Analysis")
        print("9 - Quit")
        choice = int(input("Make a choice: "))
        print(type(choice))
        if choice == 9:
            keep_running=False
        elif choice == 1:
            HDL_Driver()


    print(choice)
    return choice

def HDL_Driver() :
    hdl_value=hdl_input()
    hdl_character=hdl_analysis(hdl_value)
    hdl_output(hdl_value,hdl_character)

def hdl_input() :
    hdl_value = int(input("Enter HDL Value: "))
    return hdl_value

def hdl_analysis(hdl_value) :
    if hdl_value >= 60: 
        return "normal"
    elif 40<= hdl_value < 60:
        return "Borderline low"
    else:
        return "Low"

def hdl_output(hdl_value,hdl_character):
    print("The hdl value of {} is considered {}".format(hdl_value,hdl_character))
    return


interface()