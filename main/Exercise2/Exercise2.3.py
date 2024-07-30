
# Same function but now you can specify any size with an optional parameter so if you do not 
# Include this parameter you'll end up with 5 rows or include it and make the triangle as big as you want
def print_triangle(triangle_character:str, size:int=5) -> None:
    
    # This is called a sanity check or input sanitization... if we didn't do this what would 
    # happen when the computer program ran with an empty string or a Null/None for the input?
    if triangle_character is None or triangle_character is "":
        triangle_character = "*"

    for i in range(1, size):
        print("")
        for j in range (1, i):
            print(triangle_character, end='')

if __name__ == "__main__":
    print_triangle("*")

# Question 1.
# Can you make the triangle larger say size 50!?

# Question 2:
# Could we use a default character for the triangle character?  If so how?
