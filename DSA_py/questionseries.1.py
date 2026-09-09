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

   

