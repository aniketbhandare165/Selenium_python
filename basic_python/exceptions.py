
ItemInCart =0
#2 items will be added to cart

# if ItemInCart != 2:
#     raise Exception("Products cart count not matching")

assert(ItemInCart == 0)


#try catch machanism
try:
    with open('test.txt', 'r') as file:
        file.read()
except:
    print("some how i reached this block because there is failure in try block")

try:
    with open('testlog.txt', 'r') as file:
        file.read()
except Exception as e:
    print(e)

finally:
    print("cleaning up resources")