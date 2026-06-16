#usingd recurssion to reverse an array

# def reverse_array(arr, left, right):
#     if left >= right:
#         return 
    
#     #swap 
#     arr[left], arr[right] = arr[right], arr[left] 

#     #recursive call
#     reverse_array(arr, left+1, right-1)

# if __name__ == "__main__":
#     arr = list(map(int, input().split()))
#     print("Original array:", arr) 
#     reverse_array(arr, 0, len(arr)-1)
#     print("Reversed array:", arr) 

#TWO POINTER APPROACH 
def reverse_array(arr):
    left = 0
    right = len(arr)-1 

    while left < right:

        arr[left], arr[right] = arr[right], arr[left]

        left +=1 
        right -=1 

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print("Original array:", arr) 
    reverse_array(arr)
    print("Reversed array:", arr)