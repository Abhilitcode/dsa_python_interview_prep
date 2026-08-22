#using recurssion to reverse an array
#A base case in recursion should be an if statement, not a while loop.

# Step-by-Step Breakdown
# Suppose the user types: 10 20 30 40 into the terminal.

# 1. input()
# What it does: Reads whatever the user types as a single string.

# Result: "10 20 30 40"

# 2. .split()
# What it does: Splits the string by spaces into a list of string pieces.

# Result: ['10', '20', '30', '40'] (Notice these are still text strings with quotes!)

# 3. map(int, ...)
# What it does: Applies the function int() to every item in that list to convert each string into a real integer number.

# Result: A map object holding 10, 20, 30, 40 as real numbers.

# 4. list(...)
# What it does: Converts that map object into a standard Python list.

# Result: [10, 20, 30, 40]

# MAIN RECURSSION APPRAOCH 
# def reverse_array(arr, left, right):
#     if left >= right:
#         return 
    
#     #swap 
#     arr[left], arr[right] = arr[right], arr[left] 

#     #recursive call
#     reverse_array(arr, left+1, right-1)

# if __name__ == "__main__":
#     arr = list(map(int, input().split()))
#     print("Original array:", arr) 
#     reverse_array(arr, 0, len(arr)-1)
#     print("Reversed array:", arr) 

#TWO POINTER APPROACH 
def reverse_array(arr):
    left = 0
    right = len(arr)-1 

    while left < right:

        arr[left], arr[right] = arr[right], arr[left]

        left +=1 
        right -=1 

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print("Original array:", arr) 
    reverse_array(arr)
    print("Reversed array:", arr)