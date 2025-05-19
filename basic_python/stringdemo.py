str = "RahulShettyAcademy.com"
str1 = "Consulting firm"
str3 = "RahulShetty"

print(str[1])
print(str[0:5]) # if you want substring in python \
print(str+str1) # concatenation

print(str3 in str) # substing check

var = str.split(".")
print(var[0])
print(var)

str4 = (" great ")
print(str4.strip())
print(str4.lstrip())
print(str4.rstrip())