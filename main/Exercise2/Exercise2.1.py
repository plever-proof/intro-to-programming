
# This is a function the most comon "unit" of a computer program.  Functions can take in zero or 
# more parameters.  Basically a variable that's passed into a function.  
def print_triangle(triangle_character:str) -> None:
    
    print("%s" % triangle_character)
    print("%s%s" % (triangle_character, triangle_character))
    print("%s%s%s"% (triangle_character, triangle_character, triangle_character))
    print("%s%s%s%s"% (triangle_character, triangle_character, triangle_character, triangle_character))
    print("%s%s%s%s%s"% (triangle_character, triangle_character, triangle_character, triangle_character, triangle_character))

    
# Main functions tell the compiler or interpreter where to start the program they are optional 
# in python try it!
if __name__ == "__main__":
    print_triangle("*")

# Question 1.
# Can you make the triangle larger say size 7?

# Question 2:
# What happens if you use more than just one character to print the triangle?  Is that a bug?
