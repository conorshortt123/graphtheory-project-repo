import regex
import compiler
import shunting
import classes

def docs():
    print("+-------------------------------+")
    print("|        DOCSTRING PRINT        |")
    print("| Prints info on python program |")
    print("+-------------------------------+\n")

    print(" 1 = Info on shunting.py")
    print(" 2 = Info on regex.py")
    print(" 3 = Info on compiler.py")
    print(" 4 = Info on classes.py")
    print(" 0 = Exit")
    options = [1, 2, 3, 4, 0]

    x = input('\nEnter your choice: ')
    x = int(x)
    while x is not 0:
        if x in options:
            if x == 1:
                print("\n============== DOCS FOR SHUNT FUNCTION ==============\n")
                print(shunting.shunt.__doc__)
            elif x == 2:
                print("\n============== DOCS FOR MATCH FUNCTION ==============\n")
                print(regex.match.__doc__)
                print("\n============== DOCS FOR FOLLOWES FUNCTION ==============\n")
                print(regex.followes.__doc__)
            elif x == 3:
                print("\n============== DOCS FOR COMPILER FUNCTION ==============\n")
                print(compiler.compile.__doc__)
            elif x == 4:
                print("\n============== DOCS FOR CLASSES ==============\n")
                print(classes.State.__doc__)
                print(classes.Fragment.__doc__)
            else:
                break
        else:
            print("Invalid entry, try again.")

        x = input('\nEnter your choice:')
        x = int(x)
