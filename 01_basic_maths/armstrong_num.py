#definition of armstrong number: 
# An armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits. 
# for example, 153 is an armstrong number because 1^3 + 5^3 + 3^3 = 153==ORIGINAL NUMBER.


class Solution:
    def armstrongNumber (self, n):
        og_num = n
        num_digits = len(str(n)) 

        total = 0

        while n>0:

            digit = n%10  #last digit of the num 
            total += digit ** num_digits
            n = n//10 #reducing the number one by one 
        
        return total == og_num 

    
if __name__ == "__main__":
    obj = Solution()
    print(obj.armstrongNumber(153))
    print(obj.armstrongNumber(370))
    print(obj.armstrongNumber(9474))
    print(obj.armstrongNumber(123))
