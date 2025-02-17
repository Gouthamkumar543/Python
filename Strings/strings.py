# concationation
# Name = "goutham"
# Name2 = "kumar"

# c = Name + " " + Name2
# print(c)

# length of srting
# print(len(c))

# indexing
# print(c[0])
# print(c[3])
# print(c[4])
# print(c[7])
# print(c[12])
# print(c[8])
# print(c[10])



# c[0] = "h"  # not possible



# slicing

# print(c[0:8])
# print(c[0:])
# print(c[:10])
# print(c[:])
# print(c[-5:-1])  # slicing start from -1 but the word strting must give in the starting index 
# print(c[-5:])


# string functions - endswith , capitalized, replace, find, count

# endswith

# print(c.endswith("hello"))
# print(c.endswith("kumar"))

# capitalized the first letter 
# print(c.capitalize())

# replace
# replace every letter present in the sentence

# str ="Hello every one my name is goutham and i am here to say about my intro, in this i would like to say my hobbies myine"

# print(str.replace("i","he"))
# print(str.replace("my","world"))


# find
# returns the index of the element we are finding

# print(str.find("goutham"))


# conditional statements    

a = int(input("enter a number"))
b = int(input("enter a number"))
c = int(input("enter a number"))

if(a >= 51 & a <= 100):
    if(a == 100):
        print("hello")
    else:
        print("world")
elif(b >= 26):
    if(b == 50):
        print("hiiiii")
    else:
        print("byeeeeee")
elif(c <= 25):
    if(c == 25):
        print("heyyy")
    else:
        print("yupppp")
