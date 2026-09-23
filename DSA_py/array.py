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

# right rotate an array by one place 

nums = [2,3,4,5,6,7,8,1]

temp = nums[n-1]
for i in range(n-2,-1,-1):
   nums[i+1] = nums[i]
nums[0] = temp
print(nums)

# right rotate an array by k place
# brute force 

nums = [2,3,4,5,12,4,1]
k = 2
n = len(nums)
rotation = k%n

for _ in range(0,rotation):
   e = nums.pop()
   nums.insert(0,e)
print(nums)   

# best way 

nums = [22,33,44,55,66,77,88,99]

n= len(nums)
k=3

def reverse(nums,left,right):
   while left<right:
      nums[left],nums[right]=nums[right],nums[left]
      left += 1
      right -= 1
reverse(nums,n-k,n-1)
reverse(nums,0, n-k-1)
reverse(nums,0,n-1)      
print(nums)

# move zero to the end

# brute force way

nums = [1,2,3,4,5,0,7,8,0,11,44,0,88]

n = len(nums)
temp = []

for i in range(0,n):
   if nums[i] != 0:
      temp.append(nums[i])
nz = len(temp)
for i in range(0,nz):
   nums[i]=temp[i]
for i in range(nz,n):
   nums[i]=0 
print(nums)      

# optimal sol

nums = [2,3,4,5,0,7,0,9]

nums = [2, 3, 4, 3, 0, 7, 0, 9]

def moveZeroes(nums):

    n = len(nums)

    if len(nums) == 1:
        return

    i = 0

    while i < len(nums):
        if nums[i] == 0:
            break
        i += 1

    if i == len(nums):
        return

    j = i + 1

    while j < len(nums):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

        j += 1

moveZeroes(nums)

print(nums)

# linear search 

nums = [1, 2, 3, 4, 5, 6, 7, 8]
target = 4

n = len(nums)

for i in range(0, n):
    if nums[i] == target:
        print(i)
        break
else:
    print(-1)


# marge 2 sorted array 

nums1 = [1, 1, 1, 2, 4, 6, 7]
nums2 = [1, 2, 3, 6, 7, 8, 9, 10]

n = len(nums1)
m = len(nums2)
result = []

i = 0
j = 0

while i < n and j < m:

    if nums1[i] == nums2[j]:

        if len(result) == 0 or result[-1] != nums1[i]:
            result.append(nums1[i])

        i += 1
        j += 1

    elif nums1[i] < nums2[j]:
        i += 1

    else:
        j += 1

while i < n:
    if len(result) == 0 or result[-1] != nums1[i]:
        result.append(nums1[i])
    i += 1

while j < m:
    if len(result) == 0 or result[-1] != nums2[j]:
        result.append(nums2[j])
    j += 1

print(result)    

# find the missing number 
# brute force

nums = [1,2,3,4,6,7,8,9]

n = len(nums)
for i in range(0,n+1):
    if i not in nums:
        print(i)

# optimal way

def missingNumber(nums):
    n = len(nums)

    total = n * (n + 1) // 2

    return total - sum(nums)


nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]

print(missingNumber(nums))