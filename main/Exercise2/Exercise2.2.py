
# Next we're going to do this a little smarter using something called a loop!
def print_triangle(triangle_character:str) -> None:

    # For loops tell computers to do something a specific amount of times they're the 
    # quintesencial/most common type of loop there are more types (while, do while)
    for i in range(1, 10):
        print("")
        for j in range (1, i):
            print(triangle_character, end='')

if __name__ == "__main__":
    print_triangle("*")

# Question 1.
# Can you make the triangle larger say size 20?

# Question 2:
# What happens if you pass in something called a None?  

# Question 3 (optional):
# Optional can you make it so you can create any arbitrary size triangle without needing to
# change the code every time? Hint: try this after the next exercise.