
# given a list of values [1,2,4] can you print a string where there are AT LEAST as many underscores as the current list
# element's value number of underscores in the output string for example:

# Given:  [1, 2, 4, 3]
# Output: _1_2____4____3___

# data[0] = 1
# String = _1 (no previous underscores so add one then the current value)

# etc...

def space_func(data:list) -> str:

    counter = 0
    output_str = ""

    for current_num in data:

        if current_num > counter:
            difference = current_num - counter
            
            for i in range(0, difference):
                output_str += '_'
            counter += difference
        output_str += str(current_num)

            
    return output_str


# Given a list of positive numbers like [1,2,3,2] can you create a function to return a string where there are at least 
# as many underscores before AND after a number in the list as the number itself.  Don't forget to include the number 
# in the output string!

# Given: [1,2,3,2]
# output: _1__2___3___2__ (notice the 'extra' dashes after the 1, after the first 2 and before the last 2)

def underscore_func(data:list) -> str:
    
    # your code goes here!
    pass

    previous_num = 0 
    result = ""

    if data is None or len(data) == 0:
        return result
   
    for i in range(0, len(data)):

        current_num = data[i]

        underscores = current_num if current_num >= previous_num else previous_num

        result += str(current_num).rjust(underscores + len(str(current_num)), '_')
        previous_num = current_num

    result += "".rjust(data[-1], '_') 

    return result

if __name__ == "__main__":
        
    print("Test1: [1,2,3,2]")
    print("Expected: _1__2___3___2__")
    print("Actual:   " + underscore_func([1,2,3,2]))
    
    print("Test2: [1,2,3,0]")
    print("Expected: _1__2___3___0")
    print("Actual:   " + underscore_func([1,2,3,0]))

    print("Test3: [4,2,3,1]")
    print("Expected: ____4____2___3___1_")
    print("Actual:   " + underscore_func([4,2,3,1]))

    print("Test4: []")
    print("Expected: ")
    print("Actual:   " + underscore_func([]))

'''
func underscore_func(array: [Int]) -> String {

  // Your code goes here
}
    
print("Test1: [1,2,3,2]")
print("Expected: _1__2___3___2__")
print("Actual:   " + underscore_func(numbers: [1,2,3,2]))
    
print("Test2: [1,2,3,0]")
print("Expected: _1__2___3___0")
print("Actual:   " + underscore_func(numbers:[1,2,3,0]))

print("Test3: [4,2,3,1]")
print("Expected: ____4____2___3___1_")
print("Actual:   " + underscore_func(numbers:[4,2,3,1]))

print("Test4: []")
print("Expected: ")
print("Actual:   " + underscore_func(numbers:[]))

print("Test5: [1,1,2,2]")
print("Expected: _1_1__2__2__")
print("Actual:   " + underscore_func(numbers:[1,1,2,2]))
'''