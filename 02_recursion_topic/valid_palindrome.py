#using recursion to check if a string is a palindrome
#also if string is alphanumeric or not .  #time-:o(n), space o(n)

# def check_palindrome(s,left,right):
#     if left >= right:
#         return True
    
#     if s[left] != s[right]:
#         return False
    
#     return check_palindrome(s, left +1, right -1)


# def ismemory(s: str) -> bool:
#     store = ""
#     for char in s:
#         if char.isalnum():
#             store += char.lower()
    
#     return check_palindrome(store, 0, len(store)-1) 

# if __name__ == "__main__":
#     s= input("Enter the string:")
#     print(ismemory(s))

#Two pointer appraoch --> space o(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #space --> o(1)
        left = 0
        right = len(s)-1 

        while left < right:
            #this is for not alphanumeric and then skip those char n move
            while left < right and not s[left].isalnum():
                left +=1
            
            while left < right and not s[right].isalnum():
                right-=1
            
            if s[left].lower() != s[right].lower():
                return False 
            
            left +=1 
            right-=1
        return True 

if __name__ == "__main__":
    s = input("Enter a string:")
    obj = Solution()
    if obj.isPalindrome(s):
        print(f"{s} is a palindrome")
    else:
        print(f"{s} is not a palindrome")





    
