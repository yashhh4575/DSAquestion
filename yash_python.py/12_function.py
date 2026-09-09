def divide(a, b):
    if b ==  0:
        return None
    else:
        return a/b
print(divide(2,6))    


def sum_of_even(li):
    total = 0
    for i in li:
        if i % 2 == 0:
            total += i
    return total    

print(sum_of_even([1,2,3,4,5,66,77,76,]))




def sum_of_nums (a,b,c):
    return a+b+c
print(sum_of_nums(1,2,3))         



counter = 0
def increment():
    global counter 
    counter = counter + 1
    print(f"counter:{counter}")
def reset():
    global counter 
    counter = 0    
increment()    
increment()
reset()
increment()


# from map 

def add(x, y):
    return x + y
numbers = [1,2,3,4,5,]
total = filter(add, numbers)
print(total)


# for lambda function 

add_yash = lambda x, y : x + y
print(add_yash(1,5))

greak_lambda = lambda : "hello"
print(greak_lambda())

def power(x, y = 2):
    return x ** y

lambda_power = lambda x, y = 2 : x ** y 
print(lambda_power(5))


words = ["apple", "banana", "cat", "ball"]
print(list(filter(lambda s : len(s)>5, words )))

