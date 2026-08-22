#appraoch 1 math appraoch space-: o(1) time-: o(lognbase10)
# // --> quotient without decimal, %--> remainder
# % 10  → GET the last digit 
# // 10 → REMOVE the last digit
# scroll down for understanding why while x>reverse is taken

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x%10==0 and x!=0):  #condition for negative, last digit zero and if only zero
            return False
        
        reverse = 0
        while x>reverse:
            last_digit = x%10 
            reverse = reverse*10 + last_digit  # *10 bcuz it shifts the digits one place to the left
            x = x//10

        #get out of loop n compare for even n odd length
        #for even length and odd leneth(1st n last digit shld match n ignore the middle) respectively
        if x==reverse or x==reverse//10:
            return True
        
        return False

    
if __name__ == "__main__":
    obj = Solution()
    print(obj.isPalindrome(121))
    print(obj.isPalindrome(-121))
    print(obj.isPalindrome(10))
    print(obj.isPalindrome(1331))
    print(obj.isPalindrome(123))
    print(obj.isPalindrome(0))

    #appraoch 2 slicing appraoch space-: o(n) time-: o(n)
        #if x<0:
        #     return False
        #return str(x) == str(x)[::-1]

# We use while x > reverse: as the condition because it allows us to process only half of the number, which makes the algorithm significantly faster and avoids integer overflow issues.

# Here is why this logic works:

# 1. Stopping at the Midpoint
# When you reverse a number digit by digit, x decreases while reverse increases. The moment reverse becomes greater than or equal to x, you have reached or passed the middle of the number.

# For an even-length palindrome (e.g., 1221):

# Start: x = 1221, reverse = 0

# Step 1: x = 122, reverse = 1 (122 > 1 → continue)

# Step 2: x = 12, reverse = 12 (12 > 12 is False → STOP)

# Result: x == reverse (12 == 12), so it's a palindrome.

# For an odd-length palindrome (e.g., 12321):

# Start: x = 12321, reverse = 0

# Step 1: x = 1232, reverse = 1 (1232 > 1 → continue)

# Step 2: x = 123, reverse = 12 (123 > 12 → continue)

# Step 3: x = 12, reverse = 123 (12 > 123 is False → STOP)

# Result: Discard the middle digit (reverse // 10 gives 12). Since x == reverse // 10 (12 == 12), it's a palindrome.
