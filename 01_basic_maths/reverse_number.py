class Solution:
    def reverse(self, x: int) -> int:
        #another appraoch 2
        if (x>=0):
            rev = int(str(x)[::-1])
        else:
            rev = -(int(str(abs(x))[::-1]))
        
        if x < -2**31 or x > 2**31-1:
            return 0
        
        return rev 
    
#appraoch 1
        # rev = 0
        # sign = 1
        # if x<0:
        #     sign = -1
        #     x = x*-1
        
        # while x>0:
        #     digit = x %10
        #     rev = rev*10 + digit
        #     x = x//10

        # if rev < -2**31 or rev > 2**31-1:
        #     return 0 

        # return rev*sign

if __name__ == "__main__":
    obj = Solution()
    print(obj.reverse(123))
    print(obj.reverse(-123))  