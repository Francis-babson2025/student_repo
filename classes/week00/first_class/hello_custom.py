# %%
print("Hello, World!     ")

# %%
name = input("Please enter your name: ")
print("Hello, " + name + "!")

# new comment


# another comment
"""
The print() function will print out strings and numbers.  However you can't 
concatenate a number with a string.  Use the str() function to convert a number 
to a string.

e.g. print('my age is ' + str(50))

you may print multiple items seperated by commas.  This will add a space between items

e.g. print('my age is', 5)

-> my age is 5

By default the print() function will add a new line at the end.  It adds '\n' which
is the control character for a new line.  You may control this by setting the end parameter.

e.g. print('my age is ', end = '')  - end may equal anything.
     print(5)

     what happens if you next: 
     print(' my age is an odd number')
     print('it is not a perfect square')
                    


There are some additional parameters with print() but you won't be using them in this course.
Check your favorite AI if interested.

The input() function takes only 1 parameter, the prompt you want displayed at the terminal
for input.  IMPORTANT: all input from the terminal comes in as a string.

i.e.
 
age = input('please enter your age : ')

if now try: age = age + 1 we get an error becauseage is a numeral (text) and you can  not add a number to text.

Figure out on your own how to convert an numeral to an integer or a float.  Whay happens if you try to convert
a string to a number.  e.g. txt = 'Hello'  -> try to convert txt to an integer or float
"""
