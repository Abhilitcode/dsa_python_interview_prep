#The Fibonacci series is a sequence of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.
# Here’s how the Fibonacci series begins:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, …

# Each subsequent number is found by adding up the two numbers before it.

# Mathematically, it can be defined by the recurrence relation:

# F(n) = F(n-1) + F(n-2)

# using recursion
class Solution:
    def fibonnacci(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        return self.fibonnacci(n-1) + self.fibonnacci(n-2)

if __name__ == "__main__":
    obj = Solution()
    n = int(input("Enter a number:"))
    print(obj.fibonnacci(n))

#using backtracking

# class Solution:
#     def fibonnacci(self, n):
#         if n == 0:
#             return 0
#         if n==1:
#             return 1
        
#         result = self.fibonnacci(n-1) + self.fibonnacci(n-2)

#         print(f"fib({n}) = {result}")

#         return result 

# if __name__ == "__main__":
#     obj = Solution()
#     n = int(input("Enter the number:"))
#     print(obj.fibonnacci(n))


