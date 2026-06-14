#backtracking appraoch for factorial of a number. 
def factorial(n):
    if n==0:
        return 1
    
    result = n * factorial(n-1)
    print(f"{n} * {n-1}! = {result}")

    return result

if __name__ == "__main__":
    print(factorial(5))
    print(factorial(0))
    print(factorial(1))
    print(factorial(10))

#recursion is a programming technique where a function calls
#  itself in order to solve a problem. 
# A common example of recursion is the calculation of the factorial of a number.
# def factorial(n):
#     if  n ==0:
#         return 1
#     return n *factorial(n-1)

# if __name__ == "__main__":
#     print(factorial(5))
#     print(factorial(0))
#     print(factorial(1))
#     print(factorial(10))