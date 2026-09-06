# o(n) time complexity

def check_arr(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False 

    return True 

arr = list(map(int,input("enter an array: ").split())) 
obj = check_arr(arr)
print(obj)