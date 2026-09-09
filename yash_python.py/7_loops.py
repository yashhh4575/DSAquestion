x = 1
while x <= 20:
    if x % 2 == 0:
        print("even")
    else:
        print("odd")    
    x += 1    

x = int(input("enter the valve : "))
count = 0
for i in range(1, x + 1 ):
    if x % i == 0:
        count += 1
if count == 2:
    print("prime")
else:
    print("not prime")         

