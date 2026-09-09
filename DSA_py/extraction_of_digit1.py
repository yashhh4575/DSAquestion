n = 5873
num = n 

while num > 0:
    last_digit = num % 10
    print(last_digit)
    num = num // 10

# count digit my digit is anything 
n = 5873
nums = n
count = 0
while nums > 0:
    count += 1
    nums = nums // 10 
print(count)   

# with log we can also solve calculate the function 

n = 5873
num = n
from math import *
def count_digit(num):
        return(int(log10(num)+1))
print(count_digit(num))

# check panlindrome is_ture or is_flase
# palindrone is that kind of number in which both side are same left to right and R TO L

n = 121
num = n 
result = 0
while num > 0:
     ld = num % 10
     result = (result*10)+ld
     num = num // 10
print(n == result)   


# armstrong number 
#                 aisa number hota h isnumber ka bar number pe power add kare yska sum same aaye wahi hota h 
 
n = 153
num = n 
total = 0
nod = len(str(n))
while num > 0:
     ld = num % 10
     total= total +(ld ** nod)
     num = num // 10
print(total==n)     
     
# print factors 
num = 20 
result=[]
for i in range(1,num+1):
     if num % i == 0:
        result.append(i)
print(result)        

# better solution 

num = 20
result =[]
for i in range(1,num//2):
     if num % i == 0:
          result.append(i)
result.append(num)
print(result)           

# optimal solution 
num = 22
from math import sqrt
result=[]
for i in range(1,int(sqrt(num)+1)):
     if num % 2 == 0:
          result.append(i)
          if num // i != i:
               result.append(num // i)
result.sort()               
print(result)               


# frequency map/ dictionary 
num = [2,3,4,1,3,55,7,5,3,2,4,3,2,1,]
freq_map = {}  
for i in range(0,len(num)):
     if num[i] in freq_map:
          freq_map[num[i]] += 1
     else:
          freq_map[num[i]]=1  
print(freq_map)   

# 2nd method 
num = [2,3,4,1,3,55,7,5,3,2,4,3,2,1,]
hash_map = {}
n = len(num)
for i in range(0,n):
     hash_map[num[i]]=hash_map.get(num[i],0)+1
print(hash_map)     

      