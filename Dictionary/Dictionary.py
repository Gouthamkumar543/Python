# Dictionary
# we can use any data type inside dic such as tuple, list, boolean, numbers, string

# Details = {
#     "Name" : "goutham",
#     "Age" : 21,
#     "Gender" : "male",
#     "Subjects" : ("eng", "mat", "sci", "Bio"),
#     "Marks" : [75,68,97,67],
#     "Aduld" : True,
#     11 : 20121539011
# }

# print(Details["Name"])
# print(Details["Subjects"])


# Details["Name"] = "gouthamkumar"
# print(Details["Name"])

# Details["Subjects"] = "english"

# print(Details)


Student = {
    "Name" : "Goutham kumar",
    "Roll number" : 11,
    "Marks" : {
        "eng" : 72,
        "mat" : 75,
        "sci" : 90
    }
}

# print(len(Student))

# print(Student["Marks"]["eng"])

# print(Student.keys())

# print(list(Student.keys()))

# print(Student.values())

# print(list(Student.values()))

# print(Student.items())

# print(list(Student.items()))
# print(tuple(Student.items()))

# dic = tuple(Student.items())
# print(dic)

# print(dic[0])

# print(Student["Name"])  # return the value of the keys
# print(Student.get("Name"))   # return the value of the keys

# # print(Student["Name2"])  # return err when the key is not present
# print(Student.get("Name2"))   # return None when key is not present

# Location = {
#     "Location" : "Hyderabad",
#     "postalcode" : 500055,
#     "street" : "gajularamaram"
# }


# Student.update(Location)  #update the old dict to new my combining teo dicts
# print(Student)


# Student.update({"phone":123456789})
# print(Student)