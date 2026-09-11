# array started from hear 
# first question an array 

# largest element in an array 

nums = [22,34,55,99,1,2,4]

largest = nums[0]
n = len(nums)
for i in range(0,n):
    if nums[i]>=largest:
        largest = nums[i]
print(largest)   