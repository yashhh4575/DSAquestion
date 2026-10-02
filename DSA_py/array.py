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
#  return 1
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

# Max Consecutive Ones

nums = [1,0,1,1,1,1,1,0,0,1,1,1]

n = len(nums)
count = 0
max_count = 0
for i in range(0,n):
    if nums[i]==1:
        count += 1
        max_count = max(max_count,count)
    else:
        count = 0
print(max_count)        

# two sum 

nums = [2,3,4,5,6,7,8,9]
target = 14

n = len(nums)
has = {}

for i in range(0, n):
    remaining = target - nums[i]

    if remaining in has:
        print([has[remaining], i])

    has[nums[i]] = i

# max subarray sum 

nums = [-2,1,-3,4,-1,2,1,-5,4]

n = len(nums)
maxi = float("-inf")
for i in range(0,n):
    total = 0
    for j in range(i,n):
        total = total + nums[j]
        maxi =max(maxi,total)
print(maxi)      

# kadence algo
nums = [-2,1,-3,4,-1,2,1,-5,4]

n = len(nums)
maxi = float("-inf")
total = 0
for i in range(0,n):
    total = total + nums[i]
    maxi = max(maxi,total)
    if total < 0:
        total = 0
print(maxi)      

# buy and sell stock 
# brute force 

nums = [2,3,4,1,8,9]

n = len(nums)
max_profit = 0
for i in range(0,n):
     for j in range(i+1,n):
         if nums[i]<nums[j]:
             p = nums[j]-nums[i]
             max_profit = max(max_profit,p)
print(max_profit)         

# optimal way 

price = [2,3,4,1,8,9]

n = len(price)
min_price = float("inf")
max_profit = 0
for i in range(0,n):
      min_price  = min(min_price,price[i])
      max_profit = max(max_profit,price[i]-min_price)
print(max_profit)  

# Rearrange Array Elements by Sign

nums = [2,3,-4,5,-6,-7,9,-10]

n = len(nums)
result = [0]*n
posindex = 0
negindex = 1
for i in range(0,n):
    if nums[i]>=0:
        result[posindex] = nums[i]
        posindex += 2
    else:
        result[negindex] = nums[i]
        negindex += 2
print(result)   

# Longest Consecutive Sequence

nums = [1,2,3,99,101,102,103,104]

n = len(nums)
max_count = 0
for i in range(0,n):
    num = nums[i]
    count = 1
    while num + 1 in nums:
        count += 1
        num = num + 1
    max_count = max(max_count,count) 
print(max_count)  

# opimal way 

nums = [1, 99, 101, 98, 2, 5, 3, 100, 1, 1]

my_set = set(nums)

longest = 0

for num in my_set:
    if num - 1 not in my_set:
        x = num
        count = 1

        while x + 1 in my_set:
            count += 1
            x += 1

        longest = max(longest, count)

print(longest)


# 2D matrix 

nums = [[5, 20, 3], [7, -10, 9], [1, -52, 6]]

rows = len(nums)
cols = len(nums[0])

for i in range(0, rows):
    for j in range(0, cols):
        print(nums[i][j], end=" ")
    print()

# Set Matrix Zeros
#brute force 

def markInability(matrix, row, col):
    r = len(matrix)
    c = len(matrix[0])

    # Mark row
    for j in range(c):
        if matrix[row][j] != 0:
            matrix[row][j] = float("inf")

    # Mark column
    for i in range(r):
        if matrix[i][col] != 0:
            matrix[i][col] = float("inf")


def setZeros(matrix):
    r = len(matrix)
    c = len(matrix[0])

    # Store original zero positions
    zeros = []

    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 0:
                zeros.append((i, j))

    # Mark rows and columns
    for i, j in zeros:
        markInability(matrix, i, j)

    # Convert inf to 0
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == float("inf"):
                matrix[i][j] = 0


# Input
matrix = [
    [7, 1, 2, 3],
    [4, 5, 0, 6],
    [7, 8, 9, 10],
    [11, 12, 13, 14]
]

setZeros(matrix)

print(matrix)

# optimal way

# Input
matrix = [
    [7, 1, 2, 3],
    [4, 5, 0, 6],
    [7, 8, 9, 10],
    [11, 12, 13, 14]
]

row = len(matrix)
col = len(matrix[0])

rowtrk = [0 for _ in range(row)]
coltrk = [0 for _ in range(col)]

for i in range(0,row):
    for j in range(0,col):
        if matrix[i][j]==0:
            rowtrk[i] = -1
            coltrk[j] = -1

for i in range(0,row):
    for j in range(0,col):
        if rowtrk[i] == -1 or coltrk[j] == -1:
            matrix[i][j]=0
print(matrix) 


#   Rotate Matrix by 90 Degrees 

matrix = [
    [7, 1, 2, 3],
    [4, 5, 0, 6],
    [7, 8, 9, 10],
    [11, 12, 13, 14]
]


n = len(matrix)

result = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        result[j][(n - 1) - i] = matrix[i][j]

print(result)

# optimal way 

matrix = [
    [7, 1, 2, 3],
    [4, 5, 0, 6],
    [7, 8, 9, 10],
    [11, 12, 13, 14]
]

n = len(matrix)

for i in range(0, n - 1):
    for j in range(i + 1, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

for i in range(0,n):
    matrix[i].reverse()
print(matrix)    