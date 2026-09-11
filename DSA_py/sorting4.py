# section sort
nums = [2,3,5,4,1,6,8,9,11,16]

def section_sort(nums):
    n = len(nums)
    for i in range(0,n):
        mini_ind = i
        for j in range(i+1,n):
            if nums[j]<nums[mini_ind]:
                mini_ind = j
        nums[i],nums[mini_ind]=nums[mini_ind],nums[i]  
section_sort(nums)    
print(nums)

# bubble sorting 
nums = [3,2,4,5,6,3,1,8,10]
n = len(nums)
for i in range(n-2,-1,-1):
    for j in range(0,i+1):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]
print(nums)            

# insertion sort 

nums = [3,5,6,4,8,9,10,7,1]

n = len(nums)
for i in range(1,n):
    key = nums[i]
    j=i-1
    while j>=0 and nums[j]>key:
        nums[j+1]=nums[j]
        j-=1
        nums[j+1]= key
print(nums)       

# merge two sorted array 

left = [ 1,2,3,4]
right = [1,1,2,3,4,5,6,7]

def merge_array(left,right):
    result = []
    i, j = 0,0
    n, m = len(left),len(right)
    while i<n and j<m:
        if left[i]<=right[j]:
         result.append(left[i])
         i += 1
        else:
            result.append(right[j])
            j += 1
        if i<n:
            while i<n:
                result.append(left[i])
                i += 1
        if j<m:
            while j<m:
                result.append(right[j])
                j += 1
        return result 
print(merge_array(left,right))                               

# merge sort 

nums = [3,1,2,4,1,5,2,6,4]

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    
    mid = len(arr)//2

    left_arr = arr[ :mid]
    right_arr = arr[mid: ]

    left = merge_sort(left_arr)
    right = merge_sort(right_arr)

    return merge_array(left,right) 
print(merge_sort(nums)) 

# quick sort 

nums = [4,1,7,6,3,2,8]

def partition(nums, low, high):
    pivot = nums[low]
    i = low 
    j = high
    while i<j:
        while nums[i]<=pivot and i<= high -1:
            i+=1
        while nums[j]>pivot and j>=low+1:
            j-=1
        if i<j:
            nums[i],nums[j]= nums[j],nums[i]
        nums[j],nums[low]=nums[low],nums[j]
        return j        

def quick_sort(nums,low,high):
    if low<high:
     p_ind = partition(nums,low,high)
     quick_sort (nums,low, 
                p_ind-1)
     quick_sort (nums,p_ind+1,
                high)
quick_sort(nums,0,len(nums)-1)
print(nums)
    