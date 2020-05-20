import time
import random
import timeit
randomlist = []
for i in range(0,10):
    n = random.randint(1,100)
    randomlist.append(n)
# print('random list ',randomlist)
start_time = time.time()
# It's a combination of two things - merging and sorting
# Exploits the fact that arrays of 0 or 1 element are always sorted
# Works by decomposing an array into smaller arrays of 0 or 1 elements,
# then building up a newly sorted array
# O(n log n)
# 1. Create an empty array, take a look at the smallest values in each input array. 2 counters
# 2. while there are still values we haven't looked at...
#   a) If the value in the first array is smaller than the value in the second
#       array, push the value in the first array into our results and move on to the
#       next value in the first array
#   b) If the value in the first array is larger than the value in the second array,
#       push the value in the second array into our results and move on to the next value
#       in the second array
#   c) Once we exhaust one array, push in all remaining values from the other array

# TO-DO: complete the helper function below to merge 2 sorted arrays
# O(n + m) time and O(n + m) space
# def merge2(arrA, arrB):
#     elements = len(arrA) + len(arrB)
#     merged_arr = [None] * elements

#     index_merged = index_A = index_B = 0
#     for index_merged in range(elements):
#         if index_A == len(arrA):
#             merged_arr[index_merged:] = arrB[index_B:]
#             break
#         elif index_B == len(arrB):
#             merged_arr[index_merged:] = arrA[index_A:]
#             break
#         elif arrA[index_A] <= arrB[index_B]:
#             merged_arr[index_merged] = arrA[index_A]
#             index_A += 1
#         elif arrB[index_B] <= arrA[index_A]:
#             merged_arr[index_merged] = arrB[index_B]
#             index_B += 1
    
#     return merged_arr

def merge(arr1, arr2):
    results = []
    i, j = 0, 0
    
    while i < len(arr1) and j < len(arr2):
        if arr2[j] > arr1[i]:
            results.append(arr1[i])
            i += 1
        else:
            results.append(arr2[j])
            j += 1
    # if arr1 still has values in it
    while i < len(arr1):
        results.append(arr1[i])
        i += 1
    # if arr2 still has values
    while j < len(arr2):
        results.append(arr2[j])
        j += 1

    return results

# print(merge([1,10,50], [100,2,14,99,]))
# print(merge([100], [1,2,3,4]))
# 1. Break up the array into halves until you have arrays that are
#   empty or have one element. slice() len(arr) <= 1
# 2. Once you have smaller sorted arrays, merge those arrays with other
#   sorted arrays until you are back at the full length of the array
# 3. Once the array has been merged back together, return the merged (and sorted) array
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    # Divide arr until arr length is 1 [4]
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    # call the helper function to start merging arrL and arrR
    return merge(left, right)

# merge_sort(randomlist)

end_time = time.time()
print('Merge sort ', merge_sort(randomlist))
# print(timeit.timeit(merge_sort(randomlist)))
# print (f"runtime: {end_time - start_time} seconds")

# implement an merge_sort_in_place
# In-place means it does not occupy extra memory for merge operation as in standard case.
# Pseudo code:
# 1. Maintain two pointers which point to start of the segments which have to be merged.
# 2. Compare the elements at which the pointers are present.
# 3. If element1 < element2 then element1 is at right position, simply increase pointer1.
# 4. Else place element2 in its right position and all the elements at the right of 
# element2 will be shifted right by one position. Increment all the pointers by 1.

# Indexing function that includes the right index.
def get_partial_list(origin_list, left_index, right_index):
    return origin_list[left_index:right_index+1]

# Merge two sub arrays of arr
def merge_in_place(arr,start,mid,end):
    L = get_partial_list(arr,start,mid)
    R = get_partial_list(arr,mid+1,end)
    i = 0
    j = 0
    k = start
    for l in range(k,end+1):            # changed
        if j >= len(R) or (i < len(L) and L[i] < R[j]):
            arr[l] = L[i]
            i = i + 1
        else:
            arr[l] = R[j]
            j = j + 1

    return A

# 
def merge_sort_in_place(arr,l,r):
    # Check left and right
    if r - l > 0:                          # changed
        # Get the middle index
        mid = int((l+r)/2)
        # call f with left and mid
        merge_sort_in_place(arr,l,mid)
        merge_sort_in_place(arr,mid+1,r)             # changed
        merge_in_place(arr,l,mid,r)
    
    return arr

A  = [20, 30, 21, 15, 42, 45, 31, 0, 9]
# merge_sort_in_place(A,0,len(A)-1)                 # changed
# print('in place ',A)


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr

