# hashing in python 
#                  prestoring value into some data struc... like list/dictionary/sets and fetining it 
n = [5,2,5,86,5,2,9,7,7,3]
m = [88,5,1,2,3,6,5,4,8,9]

'''hash_list =[0]*11
for num in n:
    if num >=1 and num <= 10:
        hash_list[num]+=1
for num in m:
    if num<1 or num >10:
            print(0)
    else:
            print(hash_list[num])'''

# from dictionary 
n = [5,2,5,86,5,2,9,7,7,3]
m = [88,5,1,2,3,6,5,4,8,9]

freq_dict = {}
for num in n :
    count = 0 
    for x in m:
      if num==x :
        count += 1  
    freq_dict[num]= count    
print(freq_dict) 


# for character hashing 

s = "asbbbbbbbbbb"
q = ['d','e','b']

for char in s:
    count = 0

    for x in q:
        if x==char:
           count += 1
print(x,count)   


# char\\\
s = "asbbbbbbbbbb"
q = ['d','e','b']

hash_list = [0]*27
for ch in s:
   ascii_val = ord(ch)
   index = ascii_val - 97
   hash_list[index]+=1 
for ch in q:
   ascii_val = ord(ch)
   index = ascii_val - 97
   print(hash_list[index])   