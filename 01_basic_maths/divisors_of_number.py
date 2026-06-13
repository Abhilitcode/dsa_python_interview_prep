#O(sqrt(n)) approach n space time-: o(sqrt(n))
#here we are finding pairs 1*20 = 20, 2*10 = 20, 4*5 = 20, etc. so
#  we can find the factors in pairs and store them in a list and return the sorted list.

class Solution:
    def getDivisors(self,n):
        factors = []
        i = 1
        while i*i<=n:
            if n%i==0:
                factors.append(i)
                if i!= n//i:
                    factors.append(n//i)
            
            i+=1
        
        return sorted(factors)
if __name__ == "__main__":
    obj = Solution()
    print(obj.getDivisors(12))
    print(obj.getDivisors(15))
    print(obj.getDivisors(20567))

#brute force approach
#not suitable for large numbers as it will take o(n) time and space.
# class Solution:
#     def getDivisors(self,n):
#         factors = []
#         for i in range(1,n+1):
#             if n%i==0:
#                 factors.append(i)
        
#         return factors

# if __name__ =="__main__":
#     obj = Solution()
#     print(obj.getDivisors(12))
#     print(obj.getDivisors(15))