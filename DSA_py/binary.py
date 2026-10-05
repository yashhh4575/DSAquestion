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
