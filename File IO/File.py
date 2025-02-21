# File I/O - r,rt,w,wt

# read and readline

# to read the entire file
# f = open("file.txt","r")

# data = f.read()
# print(data)
# print(type(data))

# f.close()


# # to read only 10 letters of file
# f = open("file.txt","r")

# data = f.read(10)
# print(data)
# f.close()


# # read the file line by line

# f = open("file.txt","r")

# # data = f.read()

# # we are reading the complete data
# # print(data)

# # readline shows empty data as the dat is read before it shows next line
# # by default it give an \n char at the ending of text so we wll take one empty space
# line = f.readline()
# print(line)

# line2 = f.readline()
# print(line2)













# to append data for existing data

f = open("file.txt","a")

data = f.write("\n this is write")
f.close()

# this a also creates the fille if not exists

f = open("demo.txt","a")

data = f.write("\n this is write")
f.close()
