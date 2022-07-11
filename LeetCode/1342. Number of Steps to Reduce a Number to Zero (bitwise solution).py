from numpy import number

# Odd numbers always have a last bit of 1. 
# Subtracting 1, from an odd number, changes the last bit from 1 to 0.
# Dividing by 2 removes the last bit from the number (when last number 0)
# The bits slid along, and each became the "last" bit. 
# Notice how the 0s took one step to remove, and the 1s took two steps to remove.
# This means that we could simply analyze the binary representation of the starting num to determine the number of steps needed to reduce it.
# So, to get our answer, we can just add two steps for every 1, and add one step for every 0, for each bit in the binary representation.

# In Python, we can use bin(...) to convert an int to binary. 
# Like in Java, the binary number is represented as a str. 
# However, it also contains 0b on the start—this is simply a code to say the str is a binary number. 
# The "pythonic" thing to do is chop these two characters off with a list splice. i.e., 
# to get the binary for num, you would do bin(num)[2:].

def numberOfSteps (num):
    
    steps = 0

    # Get the binary for num, as a String. Remove the "0b" off the start with splice.
    binary = bin(num)[2:]
    
    # Iterate over all the bits in the binary string.
    for bit in binary:
        # Must use "1", not 1 here. The bits are strings!
        if bit == "1": # If the bit is a 1 
            steps = steps + 2 # Then it'll take 2 to remove.
        else: # bit == "0"
            steps = steps + 1 # Then it'll take 1 to remove.

    # We need to subtract 1, because the last bit was over-counted.
    print(steps - 1)

numberOfSteps(10)