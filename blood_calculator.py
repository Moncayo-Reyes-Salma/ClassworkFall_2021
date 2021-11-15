# blood_calculator.py


def interface():
    print("Blood Calcualtor")
    keep_running = True
    while keep_running:
        print("Make choice")
        print("1- HDL Analysis")
        print("2- LDL Analysis")
        print("9 - Quit")
        choice = int(input("Make a choice: "))
        print(type(choice))
        if choice == 9:
            keep_running = False
        elif choice == 1:
            HDL_Driver()
        elif choice == 2:
            LDL_Driver()

    print(choice)
    return choice


def HDL_Driver():
    hdl_value = hdl_input()
    hdl_character = hdl_analysis(hdl_value)
    hdl_output(hdl_value, hdl_character)


def hdl_input():
    hdl_value = int(input("Enter HDL Value: "))
    return hdl_value


def hdl_analysis(hdl_value):
    if hdl_value >= 60: 
        return "normal"
    elif 40 <= hdl_value < 60:
        return "Borderline low"
    else:
        return "Low"


def hdl_output(hdl_value, hdl_character):
    print("The hdl value of {} is considered {}".format(hdl_value,
                                                        hdl_character))
    return


def LDL_Driver():
    ldl_value = ldl_input()
    ldl_character = ldl_analysis(ldl_value)
    ldl_output(ldl_value, ldl_character)


def ldl_input():
    ldl_value = int(input("Enter LDL Value: "))
    return ldl_value


def ldl_analysis(ldl_value):
    if ldl_value < 130:
        return "normal"
    elif 130 <= ldl_value < 159:
        return "Borderline High"
    elif 160 <= ldl_value < 189:
        return "High"
    elif ldl_value >= 190:
        return "Very High"


def ldl_output(ldl_value, ldl_character):
    print("The hdl value of {} is considered {}".format(ldl_value, ldl_character))
    return


if __name__ == "__main__":
    interface()
