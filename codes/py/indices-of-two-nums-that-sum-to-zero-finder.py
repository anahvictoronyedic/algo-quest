
# Define a function named 'test' that takes a list of numbers 'nums' as input
from .utils.input_utils import Input_Utils

def test(nums):
    # Create a set 's' from the given list 'nums'
    s = set(nums)
    
    # Iterate over each element 'i' in the set 's'
    for i in s:
        # Check if the negation of 'i' is also in the set 's'
        if -i in s:
            # If found, return the indices of 'i' and its negation in the original list 'nums'
            return [nums.index(i), nums.index(-i)]

# Assign a specific list of numbers 'nums' to the variable
nums = [1, -4, 6, 7, 4]

# Assign a specific list of side lengths 'sides' to the variable
nums = Input_Utils.get_number_list_interactively({"confirmText":"Inputed List:"})

# Print a message indicating the operation to be performed
print("Indices of two numbers that sum to 0 in the said list:")

# Print the result of the test function applied to the 'nums' list
print(test(nums))
