# immutable datatypes in python

print("python tuples")
my_tuple=("strings",123,3.5)
print(my_tuple)
print(type(my_tuple))

print("-------------------------------")

print("Python numbers")
num1=4
num2=4.6
num3=7j

print("-------------------------------")

print(type(num1))
print(type(num2))
print(type(num3))

print("---------------------------------------")

print("Python strings")

message="Programming is fun"
print(type(message))

print("string methods")
print(message.capitalize())
print(message.upper())
print(message.lower())
print(len(message))
substr="is"
print(message.find(substr))

msg2="@@@@message"
print(msg2.lstrip('@'))

msg3="messages####"
print(msg3.rstrip('#'))

# split the strings into a list
txt = "hello, my name is Peter, I am 26 years old"
x = txt.split(", ")
print(x) 

# The join() method takes all items in an iterable and joins them into one string.
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x) 


txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three")
print(x)