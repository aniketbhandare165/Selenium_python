#read the file and store all the lines in list
#reverse the list
# write the list back to the file
with open('test.txt', 'r') as file:
    read_data = file.readlines()
    data_to_write = read_data[::-1]
    with open('test.txt', 'w') as file1:
        for i in data_to_write:
            file1.write(i)