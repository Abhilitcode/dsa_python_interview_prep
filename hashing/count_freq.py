
#hashing Store information in a way that allows very fast lookup.
#o(n), o(n)
class Solution:
    def count_frequency(self, arr):
        freq = {}
        for num in arr:
            if num in freq:
                freq[num] +=1
            else:
                freq[num] = 1 
        
        return freq

if __name__ == "__main__":
    obj = Solution()

    arr = [5,4,3,2,1,1,2,2,3,4]

    print(obj.count_frequency(arr))

#brute force appraoch 
#i =1 ->n times, j -> 1,2,3.. n times (first thn i will iterate further)
#o(n^2), o(1)
# class Solution:
#     def count_frequency(self, arr):
#         for i in arr:
#             count = 0
#             for j in arr:
#                 if i == j:
#                     count +=1 
        
#             print(f"{i}:{count}")

# if __name__ == "__main__":
#     obj = Solution()

#     arr = [5,4,3,2,1,1,2,2,3,4]
    
#     print(obj.count_frequency(arr))

