# array started from hear 
# first question an array 

# largest element in an array 

nums = [22,34,55,99,1,2,4]

largest = nums[0] #largest = float("-inf") it is represent - infinite
n = len(nums)
for i in range(0,n):
    if nums[i]>=largest:
        largest = nums[i]
print(largest)  

# remove duplicates from a sorted array 

nums = [1,1,1,2,2,3,4,5,7,7,8,9,10]

n = len(nums)
freq_map = {}
for i in range(0,n):
    freq_map[nums[i]]=0

j=0
for k in freq_map:
    nums[j]=k
    j+=1
print(j)
