# Recursion
#            when a function itself...
# skackoverflow is the mean memory  is full

# head recursion 
count = 0
def fun():
    global count
    if count == 4:
        return 
    print("yash")
    count += 1
    fun()
fun()

# tail recursion 

count = 0
def fun():
    global count
    if count == 4:
      return
    count += 1
    fun()
    print("anshiiii")

fun()

# recurion using parameter 

def fun(x,n):
    if n == 0:
        return
    print(x)
    fun(x,n-1)
fun(15,4)  


# print 1 to N using parameter 

def fun(i,n):
    if i > n:
        return
    print(i)
    fun(i+1,n)
fun(1,5)    

# using Tail 

def fun(i,n):
    if i < n:
     return
    fun(i-1,n)
    print(i)
fun(5,1)    


# parameterized and functional recursion 
# print sum of 1 to N
#  parameterized
def fun(sum,i,n):
        if i>n:
          print(sum)
          return
        fun(sum+i,i+1,n)
        
fun(0,1,5)    

#  functional 


def fun(n):
    if n == 1:
        return 1
    return n + fun(n-1)
x = fun(15)
print(x)


#factorial of a number 

n = 4
num = n
def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)
print(factorial(n))   

# reverse an array using recursion 

num = [5,7,3,2,6,1,5,9]

def rev(num, left, right):
    if left >= right:
        return
    num[left],num[right] = num[right],num[left]
    rev(num , left + 1 , right - 1)
rev(num, 0, len(num)-1 )  
print(num)    


# check if string is palindrome using recursion/loops 


s = "abcddcba"
def fun(s,left,right):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return fun (s,left +1 , right -1 )
print(fun(s, 0, len(s)-1))

# fibonacci number 

def fun(n):
    if n == 0 or n == 1:
        return n
    return fun(n-1)+fun(n-2)
n = 10
print(fun(n))   

