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