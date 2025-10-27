
'''
Why do we have both try and if blocks?
'''

# types of if blocks

x = 5

######################## 
# simple if statement

if x == 5:
    print('x is 5')

pause=(input('pause\n\n'))
########################



 

########################
# simple if else statement, may have only one else

if x == 5:
    print('x is 5')
else:
    print('x is not 5')

pause=(input('pause\n\n'))
########################





########################
# simple if elif (may have many elif)

if x > 5:
    print('x is greater than 5')
elif x < 5:
    print('x is less than 5')

pause=(input('pause\n\n'))
#########################





#########################
# simple if elif else

if x > 5:
    print('x is greater than 5')
elif x < 5:
    print('x is less than 5')
else:
    print('x equals 5')

pause=(input('pause\n\n'))
######################### 

#**********************************************
# when using elif, may have as many as you need 
#**********************************************  


# Types of try blocks


x = 10
y = 0

######################## 
# Try/except with a generic exception (catches most exceptions)
try:
    result = x / y
    print("Result:", result)
except:
    print("Something went wrong!")

pause=(input('pause\n\n'))
######################## 





######################## 
# Basic try/except: catch a specific exception
try:
    result = x / y
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero!")

pause=(input('pause\n\n'))
######################## 





########################
# Try/except with multiple excepts

try:
    result = x / y
    print("Result:", result)
except ZeroDivisionError:
    print("You tried to divide by zero!")
except TypeError:
    print("Invalid types used for division!")

pause=(input('pause\n\n'))
########################






########################
# Try/except/else: code in else runs only if no exception occurs
# place code not causing exception in else block

try:
    result = x / y    
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Result:", result)
    print("Division successful!")

pause=(input('pause\n\n'))
########################





########################
# Try/except/finally: finally block always runs
try:
    result = x / y
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This always runs, error or not")

pause=(input('pause\n\n'))
########################





########################
# Try/except/else/finally: full structure
x = 10
y = 0
try:
    result = x / y    
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Result:", result)
    print("Division succeeded!")
finally:
    y = 1
    result = x / y
    print("Cleanup complete")
    

pause=(input('pause\n\n'))
########################

#********************************************************
# when using multiple excepts, you may have as many as needed
#********************************************************


#*********************************************
# key difference between if and try blocks
#
# if blocks are used for logical control of what gets
# executed in your code.
#
# try blocks are used to catch machine errors
#
##############################################


#addendum
# list of python's built in exceptions


'''
Base classes

    BaseException - the base class for all exceptions
    Exception - the base class for all non-system-exiting exceptions
    ArithmeticError - base class for numeric errors
    BufferError - errors related to buffer operations
    LookupError - base class for indexing/key errors

Concrete Exceptions
    Arithmetic Errors
    FloatingPointError - floating point operation failed
    OverflowError - result too large to represent
    ZeroDivisionError - division by zero

Assertion / Debugging
    AssertionError - raised by assert statements
    DebuggerInitializationError - rare, for debugger initialization

Attribute / Name Errors
    AttributeError - invalid attribute reference
    NameError - name not found in local or global scope
    UnboundLocalError - local variable referenced before assignment

Import / Module Errors
    ImportError - failed import
    ModuleNotFoundError - module not found

Index / Key / Lookup Errors
    IndexError - sequence index out of range
    KeyError - dictionary key not found
    LookupError - base class for IndexError and KeyError

Type / Value Errors
    TypeError - invalid type operation
    ValueError - invalid value
    UnicodeError - base for UnicodeEncodeError, UnicodeDecodeError, UnicodeTranslateError

I/O and File Errors
    EOFError - end of file reached
    FileExistsError - file already exists
    FileNotFoundError - file not found
    IsADirectoryError - expected a file, found a directory
    NotADirectoryError - expected a directory, found a file
    PermissionError - permission denied
    BlockingIOError - non-blocking operation would block

Memory / Resource Errors
    MemoryError - out of memory
    RecursionError - maximum recursion depth exceeded
    BufferError - errors with buffer operations

OS / System Errors
    OSError - base class for system errors
    ConnectionError - base class for network connection errors
        BrokenPipeError
        ConnectionAbortedError
        ConnectionRefusedError
        ConnectionResetError
TimeoutError - operation timed out

Stop / Control Flow
    StopIteration - iterator exhausted
    StopAsyncIteration - async iterator exhausted
    SystemExit - raised by sys.exit()
    KeyboardInterrupt - Ctrl+C interrupt

Warning / Deprecation
    Warning - base for all warnings
        DeprecationWarning
        PendingDeprecationWarning
        RuntimeWarning
        SyntaxWarning
        UserWarning
        FutureWarning
        ImportWarning
        UnicodeWarning
        BytesWarning
        ResourceWarning

Other Miscellaneous
    StopAsyncIteration - raised to signal async iterator completion
    SystemError - interpreter detected internal error
    NotImplementedError - abstract method not implemented
    RuntimeError - generic runtime error
    ReferenceError - weak reference no longer exists
    EnvironmentError - alias of OSError in older Python versions
'''

'''
ChatGPT said:

Here's a cheat sheet of common exceptions:

Exception Name	        When It Happens / Description	                        Example
---------------------------------------------------------------------------------------------------
*ValueError	            Function receives the right type but invalid value	    int("abc")
*TypeError	            Operation or function applied to an invalid type	    "hello" + 5
*ZeroDivisionError	    Division or modulo by zero	                            10 / 0
*IndexError	            Accessing a list/tuple with an invalid index	        [1,2,3][5]
*KeyError	            Accessing a dictionary with a non-existent key	        {"a":1}["b"]
*FileNotFoundError	    Opening a file that doesn't exist	                    open("nofile.txt")
IOError	                General input/output problems                       	open("/protected/file.txt")
AttributeError	        Accessing a non-existent attribute of an object	        "abc".fake_method()
ImportError	            Fails to import a module	                            import non_existent_module
*Exception	            Base class for most built-in exceptions; can catch many errors	
                        try: 
                            1/0 
                        except Exception: 
                            print("Error")


* EXCEPTIONS ARE MOST COMMON IN AN INTRO COURSE.
'''
