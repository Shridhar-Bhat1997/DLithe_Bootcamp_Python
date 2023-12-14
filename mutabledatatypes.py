# mutable datatypes in python

my_list=[1,2,5,6.7,"python"]
print(my_list)
print(type(my_list))

# accessing elements from a list
print(my_list[0]) #indexing
print(my_list[0:2]) # slicing
print(my_list[-1]) # negative indexing

del my_list[4]
print(my_list)

my_list2=["python"] * 3
print(my_list2)

print("functions in a list")

print(min([34,23,1,22]))
print(max([34,67,32,23,89,12,0,45]))
print(len([1,2,3,4,5]))
print(list("strings"))

print("methods in a list")

li=[4,3,2,7,5,1,5,4]
print(li)
print(li.count(4))
print(li.index(7))
print(li.sort())
print(li.remove(5))
print(li.reverse())
print(li.insert(2,20))
li2=li
print(li2.clear())
print(li.append(67))

print("-----------------------------------------")

print("Python sets")
my_set={2,6,7,1}
print(type(my_set))
my_set2=set()
print(type(my_set2))

print("---------------------------------------------")

print("python dictionaries")

data={
    "id":101,
    "name":"John",
    "address":"Mysore"
}
print(type(data))
print(data)

print(data["name"])
data["address"]="Bangalore"
print(data)

data["salary"]=20000
print(data)

del data["salary"]
print(data)

print(len(data))

print("dictionary methods")
print(data.keys())
print(data.values())
print(data.items())
print(data.get('address'))

data2={"Phone":98665382}
data.update(data2)
print(data)
