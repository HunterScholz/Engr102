# This studio uses a simple caesar shift cipher encrypt and decrypt.
# Feel free to look through the functions and see if you can figure out how they work.


def main():
    # Let's learn how to use the debugger.
    # For this assignment, you shouldn't add any lines of code at all.
    # Instead, wherever you see Answer: put your answer in.

    # Use breakpoints to answer the questions

    # put a breakpoint on the line below (click to the left of the number 11 on the side)
    secret_password = decrypt('TQK KAG RAGZP FTQ OAPQ', 12)

    # When you run the code in debug mode it will stop on that line.
    # You'll see the various variables on the side, as well as a debug menu at the top.
    # Mouse over each of the debug buttons.
    # The line hasn't run yet, so we don't know what the secret password is.
    # If you press the "step over" button, it will progress through one line of code
    # This will execute the function that decrypts the secret_password
    # You'll see the secret password in the Run and Debug section of the left side.

    # TODO: Copy and paste the secret password next to Answer
    # Answer: 

    # Remember you can move forward through code, but you can't move backwards
    # So, make sure your clicks are deliberate!!!

    # Use the red square to stop the code, and remove your previous breakpoint.

    # Next, I'll give you another message to decode.
    # This time you won't have the code to to decrypt,
    # However, you can actually run custom code at the breakpoint!

    secret_code = 'LSKLU YPUN KSJ DOLU'
    shift_code = 7

    # Put a break point below on line 35. This is after the secret code and the shift code are generated.
    print("Break Point here!")

    # This mean, you can run decrypt(secret_code, shift_code) to decrypt the message
    # in the terminal area below, click the "DEBUG CONSOLE" header
    # In here, you can actually freely type code.
    # This code will run based on the current break point in the code.
    # If you typed it correctly, you should get the decrypted message!
    # TODO: Copy and paste the decrypted message
    # Answer: 

    # Stop the code and let's continue...


    # Next, let's practice stepping into a function with the debugger.
    # Put a breakpoint on the line below (line 50) and run the debugger
    step_into_me()
    
    # When the code stops, you can use the step into button (down arrow) to step into the function
    # This will start at the beginning of the function, and you can continue stepping over
    # There is an answer in the text in the function
    # TODO: Copy and paste the answer from step_into_me()
    # Answer: 

    # Stop the debugger and continue reading.

    # Another cool thing we can do with the debugger is actually modify variables

    # Look at this
    x = 6
    y = 8

    print("THIS IS 42!", x*y)

    # Uh oh! The print is a dirty liar! 6*8 is 48...
    # Without changing the code above, we can make the print statement true.
    # Put a break point on line 68, and run the debugger.
    # When the code stops on line 68, you can look on othe left side in Run and Debug
    # You'll see the various local variables (Locals), including x and y.
    # You can actually double click y and type a new value in.
    # Try typing 7, and then stepping over. Looks like it's not a liar after all!
    # But wait, look carefully, there is also a global variable (Globals) called "final_answer"
    # TODO: Type the value of final_answer
    # Answer: 

    
    # Now you're done! Move on to the errors.py studio.
    return







def decrypt(text, s):
    return encrypt(text, 26-s)


def encrypt(text,s):
    result = ""
 
    # traverse text
    for c in text:
        if (c.isupper()):
            result += chr((ord(c) + s-65) % 26 + 65)
        elif (c.islower()):
            result += chr((ord(c) + s - 97) % 26 + 97)
        else:
            result += c
 
    return result


def step_into_me():
    s = "Hey, you stepped into the function."
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    s = "you can use the step over button to continue to this line of code"
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    s = "I guess you came for the answer..."
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    s = "The answer is 'Step Step Steppity Step'."
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    s = "Eventually, you might get tired of stepping over after you've seen what's in the function."
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    s = "Especially a function as pointless as this one..."
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    s = "I mean, all it's doing is reassigning the value of s over and over..."
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    s = "Hmm... what can we do?"
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    s = "No idea..."
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    s = "I mean, you can keep mashing step over until you finish."
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    s = "But, maybe you want to save some mouseclicks."
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    s = "if there was only a way to resolve this..."
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    s = "THERE HAS TO BE A BETTER WAY!"
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    s = "So, if you continue to step over, eventually you'll reach return"
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    s = "once you reach return, the debugger will return back to the code that called the function."
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    s = "However, if you're done, you can also use the 'step out' button."
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    s = "it looks like an up arrow."
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    s = "use that to get out of this nightmare..."
















































    s = "or if you made it this far, then I guess you can keep stepping over..."



































    return
    

if __name__ == "__main__":

    global final_answer
    final_answer = "YOU ARE DONE!"
    main()

final_answer = ""