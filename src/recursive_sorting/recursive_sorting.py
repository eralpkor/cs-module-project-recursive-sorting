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
def merge2(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [None] * elements

    


    return merged_arr

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

print(merge([1,10,50], [100,2,14,99,]))
print(merge([100], [1,2,3,4]))
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
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    # call the helper function 
    return merge(left, right)


print('Merge sort ', merge_sort([10, 24, 76, 73, 72, 1, 9]))

# implement an in-place merge sort algorithm
# In-place means it does not occupy extra memory for merge operation as in standard case.
def merge_in_place(arr, start, mid, end):
    # Your code here


    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
