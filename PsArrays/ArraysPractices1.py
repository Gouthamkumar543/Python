# def largest(x):
#     num=0
#     for i in x:
#         if i > num:
#             num = i
#     print(num)

# nuumbers = [11,2,3,4,5,6,7,8,9]
# largest(nuumbers)

# def SUM(x):
#     total=0
#     for i in x:
#         total += i
#     print(total)

# nuumbers = [1,2,3,4,5,6,7,8,9]
# SUM(nuumbers)


# Total = 0
# arr = [1,2,3,4,5,6,7,8,9]

# for i in arr:
#     if i > Total:
#         Total = i
# print(Total)

# for i in arr:
#     Total += i

# print(Total)


# def Dulicate(x):
#     newArr = []

#     for i in x:
#         found = False
#         for j in newArr:
#             if i == j:
#                 found = True
#                 break
#         if not found:
#             newArr += [i]

#     print(newArr)

# num= [1,1,1,2,2,2,23,3,3,3,3,44,4,5,6,7]
# Dulicate(num)



# def Sorted(x):
#     arr = []

#     for i in range(len(x) -1,-1,-1):
#         arr += [x[i]]
#     print(arr)

# num = [1,2,3,4,5,6,7,8,9]
# Sorted(num)



# def Duplicate(ele):
#     new_array = []
#     for i in ele:
#         ele_found = False
#         for j in new_array:
#             if i == j:
#                 ele_found = True
#         if not ele_found:
#             new_array += [i]
#     print(new_array)

# num = [1,1,1,1,1,1,2,2,2,3,3,3,4,4,4,5,55,5]
# Duplicate(num)


# def uni(x):
#     new_arr = []
#     for i in x:
#         count = 0
#         for j in x:
#             if i==j:
#                 count += 1
#         if count == 1:
#             new_arr += [i]
#     print(new_arr)

# num = [1,1,1,1,15,1,2,72,2,3,37,3,47,43,4,53,55,5] 
# uni(num)