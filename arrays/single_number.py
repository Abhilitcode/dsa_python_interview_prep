#optimal appraoch 0(n), o(1)
#axor appraoch bcuz it will simply cancel out the match and remaining is the single num.
def single_number(arr):
    xor =0 
    for num in arr:
        xor = xor ^ num

    return xor 

arr = list(map(int,input("enter the array:").split()))
obj = single_number(arr)
print(obj)



#first appraoch O(n), O(n)
# def single_number(arr):
#     freq = {}

#     for num in arr:
#         freq[num] = freq.get(num,0) +1
#         print(freq)

#     for num in arr:
#         if freq[num] == 1:
#             return num 
        
# #returns 1st single number
# arr = list(map(int,input("enter the array:").split()))
# obj = single_number(arr)
# print(obj)