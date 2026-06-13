#another appraoch. o(sqrt(n)) time and o(1) space 
# as we are not storing the factors in a list and we are iterating only till sqrt(n).

class Solution:
    def isPrime(self,n):
        if n<=1:
            return False
        
        i=2
        while i*i <=n:
            if n%i ==0:
                return False
            
            i+=1 
        
        return True 
    
if __name__ == "__main__":
    obj = Solution()
    print(obj.isPrime(12))
    print(obj.isPrime(7))
    print(obj.isPrime(15))
    print(obj.isPrime(20567))
    print(obj.isPrime(1))

#brute force appraoch to find prime number.
#space and time is o(n) as we are storing the factors in a list and iterating from 1 to n.

# class Solution:
#     def isPrime(self,n):
#         count = 0
#         if n<=1:
#             return False
#         for i  in range(1,n+1):
#             if n%i==0:
#                 count +=1
            
#         if count == 2:
#                  return True
#         else:
#             return False

# if __name__ == "__main__":
#     obj = Solution()
#     print(obj.isPrime(12))
#     print(obj.isPrime(13))
#     print(obj.isPrime(15))
#     print(obj.isPrime(20567))
