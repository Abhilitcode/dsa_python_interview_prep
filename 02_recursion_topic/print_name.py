# def print_name(n):

#     #base condition for recurssion
#     if n==0:
#         return
    
#     #before recursion
#     print("Abhishek")

#     #recursive call
#     print_name(n-1)

# if __name__ == "__main__":
#     print_name(5)

#backtracking means print after the recursive call 

def print_name(n):

    if n==0:
        return
    
    print_name(n-1)
    print("Abhishek")

if __name__ == "__main__":
    print_name(5)

#we will experiemnt with numbers in the next file. 