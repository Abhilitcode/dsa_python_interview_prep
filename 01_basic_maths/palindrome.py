#appraoch 1 math appraoch space-: o(1) time-: o(lognbase10)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x%10==0 and x!=0):
            return False
        
        rev = 0
        while x>rev:
            last_digit = x%10 
            rev = rev*10 + last_digit 
            x = x//10 

        
        if x==rev or x==rev//10:
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
        #return str(x) == str(x)[::-1])
