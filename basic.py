a = 5
b = 3.2
c = "Hello"

print(b)

print("------------------------------------")

# Multiple assignments
x = y = z = "same"
print(z)

print("----------------------------")
a="guru"
b=99
print(a+str(b))

print("-----------------comments----------------")

# Hello from Python

"""This is multiline
comments in 
Python Programming"""

print("---------------------------------------")

print("print statements in Python")

print("Hello, World!")

name = "Ramu"
age = 30
print("Name:", name, "Age:", age)

name = "Bob"
age = 25
print(f"Name: {name}, Age: {age}")

name = "Charlie"
age = 40
print("Name: {}, Age: {}".format(name, age))

print("One", "Two", "Three", sep="#")

print("Hello","Karnataka","Bangalore",sep=" ",end="?")

print("-----------------------------------------------------")

print("typecasting in python")

data1=int(3.5)
print(data1)

data2=float(5)
print(data2)

data3=str(5.7)
print(type(data3))

print("--------------------------------------------")

a=10
print(bin(a))
print(oct(a))
print(hex(a))
print(id(a))

print("---------------------------------")

# num=input("enter a number:")
# print(num)

print("Membership operators are used to test if a sequence is presented in an object:")
x = ["apple", "banana"]
print("pineapple" not in x) 
print("banana" in x) 

print("-------------------------------------------------------")

print("Conditional statements")
num = 56
if num > 0:
 print("Positive number")
elif num == 0:
 print("Zero")
else:
 print("Negative number")

print("-------------------Python Loops-------------------------")

# n = int(input("Enter n: "))
# sum = 0
# i = 1
# while i <= n:
#  sum = sum + i
#  i = i+1 
# print("The sum is",sum)

numbers = [6,5,3,8,4,2,5,4,11]
sum2 = 0
for val in numbers:
 sum2 = sum2+val
print("the sum is",sum2)

print("-------------- range()----------------------")

print(range(10))
print(list(range(1,5)))
print(list(range(10,20,2)))

print("----------Loop control statements----------------")

i = 0
while i < 5:
    print(i)
    if i == 3:
        break  # Terminates the loop when i equals 3
    i += 1
    
print("----------------")

x = [1,2,3,4]
for i in x:
 if i==2:
    pass #Pass actually does nothing. It continues to execute statements below it.
    print("This statement is from pass.")
    
print("----------------")
    
for i in range(5):
    if i == 2:
        continue  # Skips iteration when i equals 2
    print(i)









