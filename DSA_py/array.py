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

#largest 2nd element in an array
# brute force 

arr = [10, 5, 8, 20, 15]

arr.sort()

print(arr[-2])

# better 

nums = [55, 32, 97, -55, 45, 32, 88, 21]

largest = float("-inf")
s_largest = float("-inf")

for i in range(len(nums)):
    largest = max(largest, nums[i])

for i in range(len(nums)):
    if nums[i] > s_largest and nums[i] != largest:
        s_largest = nums[i]

print(s_largest)

# optimal sol.
nums = [55, 32, 97, -55, 45, 32, 88, 21]

largest = float("-inf")
s_largest = float("-inf")

for i in range(0, len(nums)):

    if nums[i] > largest:
        s_largest = largest
        largest = nums[i]

    elif nums[i] > s_largest and nums[i] != largest:
        s_largest = nums[i]

print(s_largest)



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

# optimal way

nums = [1,1,1,2,2,3,4,5,7,7,8,9,10]

n = len(nums)
#if n==1:
#   return 1
i = 0
j = i+1
while j<n:
   if nums[j] != nums[i]:
    i += 1
    nums[i],nums[j]=nums[j],nums[i]
   j += 1  
print(i+1)   

# cheak the array is sorted

nums = [1,2,3,4,6,7,8,11]

is_sorted = True

n= len(nums)
for i in range(0,n-1):
   if nums[i]>nums[i+1]:
    is_sorted = False
    break
if is_sorted:
   print("true")
else:
   print("false")      

