
# This is a function the most comon "unit" of a computer program.  Functions can take in zero or 
# more parameters.  Basically a variable that's passed into a function.  In this case the 
# parameter is a variable called triangle_character.  
def print_triangle(triangle_character:str) -> None:
    
    # This is called a sanity check or input sanitization... if we didn't do this what would 
    # happen when the computer program ran with an empty string or a Null/None for the input?
    if triangle_character is None or triangle_character is "":
        triangle_character = "#"

    # For loops tell computers to do something a specific amount of times they're the 
    # quintesencial/most common type of loop there are more types (while, do while)
    # but effectively a loop runs until something happens in this case until it's incremented
    # the variable i from 1 to 10 meaning this loop will run ten times
    for i in range(1, 10):
        print("")
        for j in range (1, i):
            print(triangle_character, end='')

# Main functions tell the compiler or interpreter where to start the program they are optional 
# in python try it!
if __name__ == "__main__":
    print_triangle("P")

# Question 1.
# Can you make the triangle larger say size 20?

# Question 2:
# What happens if you use more than just one character to print the triangle?  Is that a bug?

# Question 3 (optional):
# Optional can you make it so you can create any arbitrary size triangle without needing to
# change the code every time? Hint: try this after the next exercise.