#optimal approach --> o(n), o(1)

class Solution:
    def majority_element(self, arr):
        largest = arr[0]
        for num in arr:
            if num > largest:
                largest = num
        
        return largest 

if __name__ == "__main__":
    obj = Solution()
    arr = list(map(int,input("Enter the numbers: ").split()))
    print(obj.majority_element(arr))



#brute force appraoch --> sorting o(nlogn), o(1)

# class Solution:
#     def large_element(self, arr):
#         arr.sort()
#         return arr[-1]

# if __name__ == "__main__":
#     obj = Solution()
#     arr = list(map(int,input("Enter the numbers:").split()))
#     print(obj.large_element(arr))