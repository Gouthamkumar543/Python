# Convert Array to Object -1

# def Objects(x):
#     new_obj = {}
#     for i in range(len(x)):
#         key = x[i][0]
#         value = x[i][1]
#         new_obj [key] = value
#     return new_obj

# arr = [["name", "Alice"], ["age", 25]]
# print(Objects(arr))




# Merge Two Objects -2

# obj1=  {"a": 1, "b": 2}
# obj2={"b": 3, "c": 4}

# def Objects(x,z):
#     new_obj={}
#     for i in x:
#         new_obj[i] = x[i]
#     for j in z:
#         new_obj[j] = z[j]
#     return new_obj

# print(Objects(obj1,obj2))



# count the number of properties -3

# def Objects(x):
#     count = 0
#     for i in x:
#         count += 1
#     return count

# obj = {'a': 1, 'b': 3, 'c': 4, "d":45}
# print(Objects(obj))



# get objects keys -4

# def Objects(x):
#     arr = []
#     for i in x:
#         arr += [i]
#     return arr

# obj = {'a': 1, 'b': 3, 'c': 4, "d":45}
# print(Objects(obj))




# Get Object values -5

# def Objects(x):
#     arr = []
#     for i in x:
#         arr += [x[i]]
#     return arr

# obj = {'a': 1, 'b': 3, 'c': 4, "d":45}
# print(Objects(obj))


# check if the obj is empty or not

def Objects(x):
    if len(x) == 0:
        return True
    return False

obj = {"a":3}
print(Objects(obj))