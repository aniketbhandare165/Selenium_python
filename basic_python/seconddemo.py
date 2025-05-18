values = [1,2,"rahul", 4,5.2]
# list is data type that allows multipole values and can be different data types

print(values[0])
print(values[-1])
print(values[1:3])
values.insert(3,"shetty")
print(values)
values.append("End")
print((values))

values[2] ="RAHUL"

del values[0]
print(values)

# TUples
# same as list data type but immutable
val =(1,2,3,4.5)
print(type(val))
print(val[1])
# val[2] = "three"
print(val)

# dictionary
dict_1 = {"name":"aniket", 4:"abcd", "c":"hello world"}
print(dict_1)
print(dict_1["c"])
print((dict_1[4]))

dict = {}
dict["firt_name"] = "Aniket"
dict["Last_name"] = "Bhandare"
dict["gender"] = "Male"

print(dict)
print(dict["gender"])