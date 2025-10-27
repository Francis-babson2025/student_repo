# ========================================
# Python Intro: Functions, Modules, __name__, Loops, and Input
# ========================================


'''
TWO BIG concepts:
1) Get user unput in a while loop with a try except block
2) run your main program as a function with:
    if __name__ == "__main__":
        my_main_program()

    this way, you can keep my_main_program() at the top and
    supporting functions below.


NOTE: do not worry about imports for now
'''

# Importing helper modules
import utils as ut         # Utility functions (e.g., clear_screen)
import basic_update as bs  # Custom module with extra functions

# ------------------------------------------------
# Concept 1: __name__ variable
# When a Python script is run directly, __name__ == "__main__"
print("Python built-in __name__ variable demo")
print("__name__ is:", __name__)

input("\nPress Enter to continue program 0...\n")

# ------------------------------------------------
# Concept 2: Functions
def start():
    print("Starting...")

def stop():
    print("Stopping...")

def myProgram_1():
    # Simple input-based menu
    print("1 to start")
    print("2 to stop")

    choice = int(input("Enter 1 or 2: "))
    if choice == 1:
        start()
    else:
        stop()

if __name__ == "__main__":
    myProgram_1()

input("\nPress Enter to continue program 1...\n")

# ------------------------------------------------
# Concept 3: Loops and error handling
def myProgram_2():
    ut.clear_screen()  # Clear the screen (from utils module)

    while True:
        print("3 to start")
        print("4 to stop")

        choice_txt = "Enter 3 or 4: "

##################################################################
# This section shows how to get user input in a while loop correctly *******
        while True:
            try:
                choice = int(input(choice_txt))
                break
            except ValueError:
                choice_txt = "Invalid input! Enter 3 or 4: "
##################################################################



        if choice == 3:
            start()
        elif choice == 4:
            stop()
        else:
            print("Exiting menu...")
            break

if __name__ == "__main__":
    myProgram_2()

input("\nPress Enter to continue program 2...\n")

# ------------------------------------------------
# Concept 4: Using functions from another module

def myProgram_3():
    ut.clear_screen()

    while True:
        print("5 to start")
        print("6 to stop")

        txt = "Enter 5 or 6: "
        while True:
            try:
                choice = int(input(txt))
                break
            except ValueError:
                txt = "Try again, enter 5 or 6: "

        if choice == 5:
            start()
            bs.run_basic()  # Call a function from another module
        elif choice == 6:
            stop()
            print("__name__ in this script:", __name__)
        else:
            print("Exiting menu...")
            break

if __name__ == "__main__":
    myProgram_3()
else:
    print("Imported as a module, __name__ is:", __name__)

input("\nPress Enter to continue program 3...\n")

# ------------------------------------------------
# Concept 5: Organizing main program and helper functions
def main_program():
    helper_1()

def helper_1():
    print("Running helper function 1")

'''
Best practice:
- Keep main program at the top
- Define helper functions below
- Functions must be read before they are called
'''

if __name__ == "__main__":
    main_program()


'''
Concepts / Tools Covered in This Example

__name__ variable - Detect if script is run directly or imported.
Functions - def start(), def stop(), def helper_1().
Calling functions - Both within the same script and from another module (bs.run_basic()).
Modules and imports - import utils as ut, import basic_update as bs.
Input / output - Using input() and print().
Loops - while True: for menus and input validation.
Error handling - try / except to catch invalid input.
Menu design - Simple text-based menus with options.
Screen control - Calling ut.clear_screen() from an external module.
Organizing code - Keeping main program at the top, helper functions below.
if __name__ == "__main__": pattern - Ensures main program runs only when intended.
'''