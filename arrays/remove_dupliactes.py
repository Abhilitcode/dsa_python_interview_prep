#leetcode problem 26
#o(n). o(1) in in place modification, two pointers appraoch

# 💼 Interview POV
# Q: Why can you use two pointers here?

# Because the array is sorted, so duplicates are adjacent.

# Q: What do the two pointers do?

# j scans the array looking for new unique values, while i keeps track of where the next unique value should be placed.

# Q: Why not use a set?

# A set would require O(n) extra space, while the problem asks for an in-place solution.

# Q: Why don't we actually delete elements?

# Because LeetCode only cares about the first k positions after modification.

def remove_duplicate(nums):
    if len(nums)==0:
        return 0

    i= 0
    for j in range(1,len(nums)):
        if nums[i] != nums[j]:
            i +=1
            nums[i] = nums[j] 

    return i+1 #---> return the unique elements

arr = list(map(int,input("enter the array: ").split()))
obj = remove_duplicate(arr)
print(obj)

