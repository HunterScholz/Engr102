def main():
    
    # Errors are a natural part of coding.
    # Every programmer will encounter errors that they need to resolve.
    # In this module, you will learn some common errors and how you might be able to resolve them.
    # Some errors VSCode will find before you even run the code. You'll see yellow or red squiggly lines under.
    # Some errors VSCode will not be able to find, and you'll only know when you run the code.

    # Whenever you see "TODO" in the comments, it means that there is something for you to do there before you can continue.


    # TIP: You can control or command + left click the function to move down to the function.


    # TODO: Read the def you_forgot_something() and fix the error
    you_forgot_something()
    
    
    # TODO: Read the def it_matters() and fix the error
    it_matters()

    # TODO: Read the def hello_world() information and work through.
    hello_world()

    # TODO: Read the def it_does_not_compute() information and work through.
    it_does_not_compute()

    # TODO: Read the def my_list_is_too_short() information and work through.
    my_list_is_too_short()

    # TODO: Read the def everyone_knows_this_math_rule() information and work through.
    everyone_knows_this_math_rule()

    # TODO: Read the def giving_functions_the_wrong_stuff() information and work through.
    giving_functions_the_wrong_stuff()

    # TODO: Read the def make_your_own_error() information and work through.
    make_your_own_error()

    # TODO: Read the def handling_errors() information and work through.
    handling_errors()

    # TODO: You're done! Stage your changes, and be sure to push them to your remote repository.


def you_forgot_something():
    # Run the code. type of error occurs?
    # To see the type of error, you should see "xxxxxxxError:" in the output below

    # TODO: What is the type of error for this?
    # Your Answer: 

    # TODO: What is the difference between = (single equals) and == (double equals)?
    # You may need to use google to find the answer.
    # Your Answer: 

    if 1 + 1 = 2:
        print("They are equal!")

    # TODO: Resolve the error and run the code again to make sure nothing happens


def it_matters():

    # You'll notice that indents actually matter in Python

    # TODO: What is the type of error for this?
    # Your Answer: 

    for i in range(10):
    print(i)

    # TODO: Resolve the error and run the code again to make sure nothing happens

def hello_world():
    # Whoops! There's something wrong with this hello world function!
    # Something is misspelled!

    # TODO: What is the type of error for this? (What's in the place of xxxxxxx)
    # Your answer: 
    
    prnit("Hello World")

    # TODO resolve the error, and run the code again to make sure nothing happens.

def it_does_not_compute():

    # What happens when you try to divide a string by an integer?

    # TODO: What is the type of error for this? (What's in the place of xxxxxxx)
    # Your answer: 

    x = "18"    # This is a string
    y = 3       # This is an integer

    z = x / y

    # TODO resolve the error, and run the code again to make sure nothing happens.

def my_list_is_too_short():

    # Let's take a look at this list.
    # Lists are indexed starting at 0
    # So:
    # my_list[0] == "C"
    # my_list[1] == "O"
    # my_list[2] == "O"
    # my_list[3] == "L"

    # What happens if we try to get an index that isn't within 0-3?

    # TODO: What is the type of error for this?
    # Your answer: 

    my_list = ["C", "O", "O", "L"]
    print(my_list[4])

    # TODO resolve the error, and run the code again to make sure nothing happens.


def everyone_knows_this_math_rule():

    # Something bad will happen if we break a rule of math...

    # TODO: What is the type of error for this?
    # Your answer: 

    x = 0
    y = 10

    z = y / x

    # TODO resolve the error, and run the code again to make sure nothing happens.

def giving_functions_the_wrong_stuff():

    # What happens if you try to use a function, give it the correct data type, but not something it can work with?

    # the int() function is built-in and converts an integer to a string

    # TODO: What is the type of error for this?
    # Your answer: 

    my_int = int("5") # This works fine, because "5" is a number
    my_int_2 = int("Dan") # What happens if we try to pass a non-number?

    # TODO resolve the error, and run the code again to make sure nothing happens.

def make_your_own_error():
    
    # Sometimes we may want to raise our own error.

    # This can be because we want to ensure that the data is as expected.
    # For example, perhaps we have a function that is intended to handle only a number between 1 and 10.
    # What happens if the function gets -5? or 12? It will likely cause an unexpected error somewhere deeper in the code.
    # However, we can stop the code in an expected way by raising our own error.

    x = 12 # Oops, this isn't between 1 and 10

    if x < 1 or x > 10:
        raise TypeError("The number must be between 1 and 10")
    
    # TODO: Run the code to see how our raised error occurs

    # Did you notice that TypeError does not make sense? The data type is correct (integer), but the value is not.
    # TODO: Change TypeError to another error that makes more sense.

    # TODO: Fix the value of x so the error no longer occurs


def handling_errors():
    # Sometimes we may expect an error to occur, but we don't want it to crash our program.
    # Instead, we want to handle the error, and proceed.

    # For example, maybe we want to use the int() function to convert a string to an integer.
    # So, we ask the user to give us a number to convert, but instead they give us a word.

    bad_user_input = "What is a number?"

    # Should this crash our code?
    # Probably not. Maybe instead we will just assign them a number if they don't give us one.
    
    # in this case, we can TRY to cast the string as an integer.
    # we know that we will get a ValueError if they don't give us a valid value.
    # So if we get a ValueError we can instead just assign them a number

    try: # try to run some code
        int(bad_user_input)
    except ValueError: # except will run if the ValueError exception is found
        print("Well, that wasn't a number, so we'll just give you one")
        bad_user_input = 7
    else: # else is optional, but it will run if the exception isn't found.
        print("Hey, you know how to type a number. Good job!")

    
# Whenever you create a python project, you should have this statement at the bottom.
# This tells the python script to run the main() function.
if __name__ == "__main__":
    main()