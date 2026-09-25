num = 58392
while num > 0:
    ld = num % 10
    print(ld)
    num = num // 10

num = 58392
count = 0
while num > 0:
     count += 1
     num = num // 10
print(count)   


n = 121
num = n
result = 0
while num > 0:
     ld = num % 10
     result = (result*10)+ ld
     num = num // 10
print(n == result)     

# recursion question 
nums = 5
def fun(nums):
     if nums == 0:
          return
     fun(nums-1)
     print(nums) 
fun(nums)


nums = 5
def fun(nums):
     if nums == 0:
      return 
     print(nums)
     fun(nums-1)
fun(nums)   

# ARRAY 

nums = [12, 5, 18, 7, 25, 9]

n = len(nums)
largest = float("-inf")
for i in range(0,n):
    if nums[i]>largest:
        largest = nums[i]
print(largest)            


nums = [10, 20, 5, 8, 15]    

n = len(nums) 
largest = float("-inf")
s_largest = float("-inf")
for i in range(0,n):
     if  nums[i]>largest :
        s_largest = largest
        largest = nums[i]
     
     elif   nums[i] > s_largest and nums[i] != largest:
            s_largest =nums[i]
print(s_largest)            
         


            

