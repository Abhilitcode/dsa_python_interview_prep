#appraoch 1 math appraoch space-: o(1) time-: o(lognbase10)
# // --> quotient without decimal, %--> remainder
# % 10  → GET the last digit 
# // 10 → REMOVE the last digit

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
