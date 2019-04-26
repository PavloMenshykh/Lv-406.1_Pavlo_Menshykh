def start():
    while True:

        try:
            var_a = float(input("Enter variable a:\n"))
            print("Variable a is " + str(var_a))
        except:
            print("Enter a numerical value")
        else:
            break

    while True:

        try:
            var_b = float(input("Enter variable b:\n"))
            print("Variable b is " + str(var_b))
        except:
            print("Enter a numerical value")
        else:
            break

    while True:

        try:
            var_act = int(input("What do you want to do?\n\
              1) add\n\
              2) substract\n\
              3) multiply\n\
              4) divide\n"))
        except:
            print("Enter a integer value")
            continue
        if var_act > 0 and var_act <= 4:
            if var_act == 1:
                print("addition")
                print("Result is " + str(var_a + var_b))
            elif var_act == 2:
                print("substraction")
                print("Result is " + str(var_a - var_b))
            elif var_act == 3:
                print("multiplication")
                print("Result is " + str(var_a * var_b))
            elif var_act == 4:
                print("division")
                print("Result is " + str(var_a / var_b))
            break
        else:
            print("Choose correct option")


while True:
    restart = input("Press enter to exit or type start\n")
    if restart == "start":
        start()
    else:
        exit()
