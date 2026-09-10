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


    
    