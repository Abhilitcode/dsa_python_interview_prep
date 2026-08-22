#pre-order printing

# def print_nums(n):

#     if n==0:
#         return
    
#     print(n)

#     print_nums(n-1)

# if __name__ == "__main__":
#     print_nums(5)

#same thing but post order or unwinding. 
#refer to 1st docs to understand unwinding.

def print_nums(n):

    if n==0:
        return 
    
    print_nums(n-1)
    print(n) 

if __name__ == "__main__":
    print_nums(5)

    #here first it will call all the functions till n becomes 0 and 
    # then it will print the numbers in the backtracking way.