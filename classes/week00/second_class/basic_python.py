#%%
'''
Python has built in variables. One of them is __name__
when you run a python script __name__ is set to the text string "__main__"
When __name__ = "__main__" you know that your code is running
'''
import utils as ut
import basic as bs



if __name__ == '__main__':
    print("our code is running", __name__)

x=input('\nprogram 0\n')

# %%

def myProgram():
    print('1 to start')
    print('2 to stop')    

    choice = int(input('enter 1 or 2 : '))

    if choice == 1:
        start()
    else:
        stop()

def start():
    print('starting')
    

def stop():
    print('stopping')

if __name__ == '__main__':
    myProgram()

x=input('\nprogram 1\n')
#%%



def myProgram():

    ut.clear_screen()

    while True:
        print('3 to start')
        print('4 to stop')

        choice = int(input('enter 3 or 4 : '))

        if choice == 3:
            start()
        elif choice == 4:
            stop()
        else:
            break

def start():
    print('starting')

def stop():
    print('stopping')

if __name__ == '__main__':
    myProgram()

x=input('\nprogram 3\n')
#%%

import utils as ut
import basic_update as bs
def myProgram():

    ut.clear_screen()

    while True:
        print('5 to start')
        print('6 to stop')
        
        txt = 'enter 5 or 6: '
        while True:
            try:
                choice = int(input(txt))
                break
            except ValueError:
                txt = 'try again, enter 5 or 6: '

        if choice == 5:
            start()
        elif choice == 6:
            stop()
        else:
            break

def start():
    print('starting')
    bs.run_basic()
    

def stop():
    print('stopping')
    print(__name__)

if __name__ == '__main__':
    myProgram()
else:
    print(__name__)


#%%



def main_program():
    helper_1()

def helper_1():
    print("helper 1")

'''
running your main program as a function allows you keep your main program at
the top of your script and all your helper functions below.  Because python is
an interpeted language code is read line by line.  All functions must be read
before they are used.
'''
if __name__ == '__main__':
    main_program()


# %%
