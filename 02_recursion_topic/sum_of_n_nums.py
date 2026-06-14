#before recursion
def sum_of_nums(n):
    if n==0:
        return 0
    
    result = n + sum_of_nums(n-1)

    return result

if __name__ == "__main__":
    print(sum_of_nums(5))



#backtrack recursion
# def sum_of_nums(n):
#     if n==0:
#         return 0

#     result = n + sum_of_nums(n-1)

#     print(f" {n} + sum({n-1}) = {result}")

#     return result 

# if __name__ == "__main__":
#     print(sum_of_nums(5))