# Imports allow you to use POWERFUL libraries that other programmers have already created
import time

# Classes are the second most common "unit" of a computer program they are effectively a 
# container for all the RELATED functions and code.  Basically if you want to do a number
# of similar or related tasks you put them in a class so they're not scattered everywhere
# in the code
class MagicNumber():

    # Classes have what's called a constructor it lets you set them into a specific state
    # before you use any of the functions in them.  In this case I'm letting users set
    # their default number or use my default number of 12345
    def __init__(self, my_number:int=12345) -> None:

        # Classes can also have "class member" variables that are shared across every
        # function in a class.  Very useful!
        self.my_number = my_number

    def magic_eight_ball(self) -> None:

        original_number = self.my_number
        print("Aha!  I see you have selected: %s" % self.my_number)

        # Libraries allow you to use powerful complex commands like in this case I'm telling
        # the program to just wait 2s before continuing.  Which seems easy but HOW DO YOU TELL
        # A COMPUTER NOT TO DO SOMETHING!?! Well that takes work... A LOT OF WORK! 
        time.sleep(2)

        # Variables hold a value you can assign anything to them (more or less). What this line 
        # does is take the existing value of the variable self.my_number removes 1 from it then
        # reasigns it to the original variable called self.my_number it's not a math equation 
        # exactly but pretty close.
        self.my_number = self.my_number - 1
        print("I will first subtract 1 from your number: %s " % self.my_number)
        time.sleep(2)

        # If you were wondering self is a special type of variable called a self reference
        # or "this" in other languages.  Basically it references the instance of the class
        # called an object.  Don't worry too much about that just think of it as a link to 
        # this class.
        self.my_number = self.my_number * 3
        print("Next I will multiply it by 3: %s " % self.my_number)

        time.sleep(2)
        twelve = 12
        self.my_number = self.my_number + twelve
        print("Next I'm adding %s to your number: %s" % (twelve, self.my_number))

        time.sleep(2)
        self.my_number = self.my_number / 3
        print("Next I'll divide your number by 3: %s" % self.my_number)

        time.sleep(2)
        self.my_number = self.my_number + 5
        print("Next I'll add 5 to the number: %s" % self.my_number)

        time.sleep(2)
        self.my_number = self.my_number - original_number
        print("The magic eight ball says: %s" % self.my_number)

        time.sleep(2)
        print("Tada!!!")
    
    def enter_your_number(self) -> None:
        
        # programs can even take input... mouse movement, keyboard key presses, head tracking in VR
        # you name it!  In this case the function input is taking key presses.
        your_input = input("Input your number: ")
        self.my_number = int(your_input)

if __name__ == "__main__":

    # Computer programs are like very complex recipes you tell a computer to add a dash of
    # number input... a sprinkle of loops... a cup of variable modification and TADA you 
    # have a repeatable set of steps that more or less always gives you the same result.
    magic = MagicNumber()
    magic.enter_your_number()
    magic.magic_eight_ball()


# Question 1:
# What happens if the user inputs something that isn't a number?  

# Question 2 (optional):
# Can you fix the bug that happens if a user inputs a string instead of a number? 
# Hint this is harder than it looks but you could "try" to "catch" folks out here...
