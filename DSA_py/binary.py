# Binary Search 

nums = [2,3,4,5,6,8,9,15]
target = 5

def binarysearch(nums,target):
    n = len(nums)
    low = 0
    high = n-1
    while low<=high:
        mid = (low+high)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            low = mid + 1
        else:
            high = mid -1
    return -1
print(binarysearch(nums,target))          


# recu....


def binarySearch(nums, low, high, target):

    if low > high:
        return -1

    mid = (low + high) // 2

    if nums[mid] == target:
        return mid

    elif nums[mid] < target:
        return binarySearch(nums, mid + 1, high, target)

    else:
        return binarySearch(nums, low, mid - 1, target)


nums = [2, 4, 6, 7, 9, 11, 18, 19]
target = 13

ans = binarySearch(nums, 0, len(nums) - 1, target)

print("Index:", ans)

# Search Insert Position

nums = [1, 3, 4, 5, 8, 9, 14, 15, 19, 20, 21]
target = 16

n = len(nums)

low = 0
high = n - 1

while low <= high:
    mid = (low + high) // 2

    if nums[mid] >= target:
        high = mid - 1
    else:
        low = mid + 1

print(low)

# Floor & Ceil in Sorted Array

nums = [2, 3, 3, 4, 5, 6, 7, 7, 7, 8, 9, 10, 12, 13]
target = 6

n = len(nums)
ceil = -1
floor = -1

low = 0
high = n - 1

while low <= high:
    mid = (low + high) // 2

    if nums[mid] == target:
        floor = nums[mid]
        ceil = nums[mid]
        break

    elif nums[mid] > target:
        ceil = nums[mid]
        high = mid - 1

    else:
        floor = nums[mid]
        low = mid + 1

print(floor, ceil)

# Find First & Last Occurrence in Sorted Array

nums = [1,2,3,3,3,3,3,3,3,3,3,5,6,7]
target = 3

n = len(nums)
first = -1
last = -1

for i in range(0,n):
    if nums[i]==target:
        if first == -1:
            first = i
        last = i  
print(first,last)

 # optimal ways 

nums = [1,2,3,3,3,3,3,3,3,3,3,5,6,7]
target = 3

def lowerBound(nums, target):
    n = len(nums)
    lb = -1

    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] >= target:
            lb = mid
            high = mid - 1
        else:
            low = mid + 1

    return lb


def upperBound(nums, target):
    n = len(nums)
    ub = -1

    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] > target:
            ub = mid
            high = mid - 1
        else:
            low = mid + 1

    return ub

# Output
print("Lower Bound:", lowerBound(nums, target))
print("Upper Bound:", upperBound(nums, target))

# Count Occurrences in Sorted Array

nums = [1,2,3,3,3,3,3,3,3,3,3,5,6,7]
target = 3

n = len(nums)
first = -1
last = -1

for i in range(0,n):
    if nums[i]==target:
        if first == -1:
            first = i
        last = i          
print(last-first+1)



nums = [1,2,3,3,3,3,3,3,3,3,3,5,6,7]
target = 3

def lowerBound(nums, target):
    n = len(nums)
    lb = -1

    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] >= target:
            lb = mid
            high = mid - 1
        else:
            low = mid + 1

    return lb


def upperBound(nums, target):
    n = len(nums)
    ub = n

    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] > target:
            ub = mid
            high = mid - 1
        else:
            low = mid + 1

    return ub

# Output
print("Lower Bound:", lowerBound(nums, target))
print("Upper Bound:", upperBound(nums, target))




