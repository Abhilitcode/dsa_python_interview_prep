""" First time:
result empty → add the number

After that:
result not empty → check if number is different from last added number
"""
#optimal appraoch O(n+m) for both time n space
def union(arr1,arr2):
    n = len(arr1)
    m = len(arr2)

    i =0
    j =0
    result = []

    #iterate through each array until one gets completed
    while i<n and j<m:
        #if 1 element of the arr1 or arr2 is less thn other
        if arr1[i] < arr2[j]:
            #if result is not empty or last element added in result is same as curr thn 
            # reject it move ahead for increment and if not same append it.
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i +=1 

        elif arr2[j] < arr1[i]:
            if not result or result[-1] != arr2[j]:
                result.append(arr2[j])
            j +=1 
        else:
            #if both elements r same add one of them
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])

            i +=1 
            j +=1

    #if one of the arr1 or arr2 gets completed 
    # add the remaining elemets from resp arrays.
    while i<n:
        if not result or result[-1] != arr1[i]:
            result.append(arr1[i])
        i +=1 

    while j <m:
        if not result or result[-1] != arr2[j]:
            result.append(arr2[j])

        j +=1 

    return result 


#brute force appraoch 
# Time: O((n + m) log(n + m)) because of sorting
# Space: O(n + m) 

# def union(arr1,arr2):
#     result = set()

#     for n in arr1:
#         result.add(n)

#     for m in  arr2:
#         result.add(m)

#     return sorted(result)

arr1 = list(map(int, input("Enter first sorted array: ").split()))
arr2 = list(map(int, input("Enter second sorted array: ").split()))

obj = union(arr1, arr2)
print(obj)