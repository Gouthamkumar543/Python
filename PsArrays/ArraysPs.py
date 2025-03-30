# #Finfding the largest numbers -1

# def finding(x):
#     largerNumber = 0
#     #print(x[5])
#     for i in x:
#         if i > largerNumber:
#             largerNumber=i
#     return largerNumber

# numbers = [1,3,4,60,7,9]
# print(finding(numbers))





# #Sum of all Numbers -3

# def Sum_of_numbers(x):
#     total=0
#     for i in x:
#         total += i
#     return total
# numbers=[3,36,7,7,8,7]
# print(Sum_of_numbers(numbers))


# #Without function
# numbers = [3,4,5,8,9]
# total = 0

# for i in numbers:
#     total += i
# print(total)



#Removing the duplicates elements from the list  -4

# def remove_duplicates(arr):
#     new_array = []

#     for i in arr:
#         found = False
#         for j in new_array:
#             if i == j:
#                 found = True
#                 break
#         if not found:
#             new_array += [i]

#     return new_array

# numbers = [1, 1, 2, 3, 4, 4, 5, 6, 6, 7]
# print(remove_duplicates(numbers))





#Sorted in ascending order -5

# def Sorted(ele):
#     for i in range(len(ele) -1):
#         print(i)
#         if ele[i] > ele[i+1]:
#             return print(False)
#     return print(True)

# num = [0,1,2,3,4]
# Sorted(num)

# arr = [1,2,3,45]
# Sorted(arr)





#Reverse the elements -6

# def Reverse(x):
#     new_array = []
#     for ele in range(len(x)-1,-1,-1):
#         # print(ele)
#         new_array += [x[ele]]
#     print(new_array)

# num = [1,2,3,4,5]
# Reverse(num)








#Remove Falsy values from arr -7

# def Removing_Empty_Values(arr):
#     new_arr=[]
#     for item in arr:
#         if item:
#             new_arr += [item]
#     print(new_arr)

# arr = [0, 1, False, 2, '', 3, None, [], {}, set(), float()]
# Removing_Empty_Values(arr)







#find_unique_elements in arry - 8

# def find_unique_elements(arr):
#     unique_elements = []  
#     for i in arr:
#         count = 0
#         for j in arr:
#             if i == j:
#                 count += 1
#         if count == 1:
#             unique_elements += [i] 
#     return unique_elements

# arr = [1, 2, 2, 3, 4, 4, 5]
# print(find_unique_elements(arr))





#Sum of even numbers -9

# def Sum_Even(arr):
#     new_array = 0
#     for item in arr:
#         if item % 2 == 0:
#             new_array += item
#     print(new_array)

# arr = [1,2,3,4,5,6,7,8,9,0,7,8,4,3,3,2,100]
# Sum_Even(arr)