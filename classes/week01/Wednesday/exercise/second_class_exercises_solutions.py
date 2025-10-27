# print 'hello' 5 times using an arithmetic operator

print("hello " * 5)



# print 'hello' 5 times using a loop

for i in range(5):
    print('hello')


# print 'hello' 5 times on the same line using a loop

for i in range(5):
    print('hello', end = ' ')
print()


''' using nested loops print the following:

00 01 02
10 11 12
20 21 22

'''

'''
example of nested loops.  think of the outer loop as rows
and the inner loop as columns.  we start with row = 0 and then for
each column we print 0col0 0col1 0col2 and then print() for a new row
or 00 01 02
then row becomes 1 and we repeat the process
10 11 12
and again
20 21 22
'''

for row in range(3):
    for col in range(3):
        print(str(row) + str(col), end = ' ')
    print()

# define txt and input some text from the keyboard into it

txt = input('Please enter some text: ')
print(txt)


# print each letter in txt 
txt = input('Please enter some text: ')
for letter in txt:
    if letter.isalpha():
        print(letter, end = '')
print()

# assign the variable letter to the first letter in txt
txt = 'now id the time'
letter = txt[0]
print(letter)

# print out all the letters in txt that are equal to the first letter

'''
say txt = 'the cat in the hat was read today'
't' is the first letter

result: tttt
'''

txt = 'the cat in the hat was read today'
for letter in txt:
    if letter == txt[0]:
        print(letter, end = '')
print()


'''
# suppose we had a list of n elements. create a new list that
  shifts the elements by 3

  myList = ['apple', 'orange', 'pear', 'blueberry', 'peach']
  shifted_list = ['pear', 'blueberry', 'peach', 'apple', 'orange']

  Hints:
     1) use len(), %, enumerate
     2) also assign shifted_list = [None] * length  (you'll need to determine 
        the length variable)
     3) shift inside the for loop
     4) print out the printed list outside the for loop
'''
myList = ['apple', 'orange', 'pear', 'blueberry', 'peach']
shifted_list = [None] * len(myList)
shift = 3

for idx, item in enumerate(myList):
    new_idx = (idx + shift) % len(myList)
    shifted_list[new_idx] = item

print(shifted_list)



# don't recalculate len()

myList = ['apple', 'orange', 'pear', 'blueberry', 'peach']
length = len(myList)
shifted_list = [None] * length
shift = 3

for idx, item in enumerate(myList):
    new_idx = (idx + shift) % length
    shifted_list[new_idx] = item

print(shifted_list)


# what id you didn't know about enumerate?

myList = ['apple', 'orange', 'pear', 'blueberry', 'peach']
length = len(myList)
shifted_list = [None] * length
shift = 3

idx = 0
for item in myList:
    new_idx = (idx + shift) % length
    shifted_list[new_idx] = item
    idx += 1

print(shifted_list)


'''
notice this line: shifted_list = [None] * length
this create [None, None, None, None, None]
as we go from  0 to 4 in the loop we can index directly into the 
new list.

below we use shifted_list = [] so if we tried to set shifted_list[3] = 'apple'
we would get an error.  Instead, we need to append but to do that we need to 
start with the item that will be shifted to the start of the list.

the start of the shifted list will always be length - shift
and will need to go from there to length - shift + length.
then the old_idx will be idx % length so we append in this order
2, 3, 4, 0, 1  --see below--
'''


myList = ['apple', 'orange', 'pear', 'blueberry', 'peach']

length = len(myList)
shifted_list = [] 
shift = 3
for idx in range(length - shift, length - shift + length):
    old_idx = idx % length    
    shifted_list.append(myList[old_idx])
print(shifted_list)

'''
Concepts covered, tools for your toolchest

Arithmetic operators on strings (*)
Loops (for, nested loops)
Controlling print output (end)
String indexing and iteration
Conditionals
List manipulation and modular arithmetic
Using len() and enumerate()

'''

