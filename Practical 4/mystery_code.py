# What does this piece of code do?
# Answer: This code generates 11 random integers between 1 and 10, accumulates their total sum, and prints the final sum (the imported ceil function is unused in the code).

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint  # Import the randint function to generate random integers between a specified range (1-10 in this code)

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil  # Import the ceiling function (rounds up to the nearest integer), but this function is not used in the code

total_rand = 0  # Initialize a variable to store the cumulative sum of all random numbers (starting value = 0)
progress = 0    # Initialize a counter variable to control the number of loop iterations (starting value = 0)

# Loop condition: Execute the loop as long as progress is less than or equal to 10 (runs 11 times total)
while progress <= 10:
    progress += 1          # Increment the counter by 1 (runs first in each loop, resulting in 11 iterations: 1 → 11)
    n = randint(1, 10)     # Generate a random integer between 1 and 10, assign it to variable 'n'
    total_rand += n        # Add the current random number 'n' to the cumulative sum variable 'total_rand'

print(total_rand)  # After the loop ends, print the total sum of the 11 generated random numbers
