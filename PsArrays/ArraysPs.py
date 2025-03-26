# #Finfding the largest numbers -1

# def finding(x):
#     largerNumber = x[4]
#     #print(x[5])
#     for i in x:
#         if i > largerNumber:
#             largerNumber=i
#     return largerNumber

# numbers = [10,3,4,6,7,9]
# print(finding(numbers))





# #Sum of all Numbers -3

# def Sum_of_numbers(x):
#     total=0
#     for i in x:
#         total += i
#     return total
# numbers=[3,36,7,7,788,7]
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


#Reverse the elements -6

# def Reverse(x):
#     new_array = []
#     for ele in range(len(x)-1,-1,-1):
#         new_array += [x[ele]]
#     print(new_array)

# num = [1,2,3,4,5]
# Reverse(num)


#Sorted in ascending order

def Sorted(ele):
    for i in range(len(ele) -1):
        if ele[i] > ele[i+1]:
            return print(False)
    return print(True)

num = [11,1,2,3,4]
Sorted(num)

arr = [1,2,3,45]
Sorted(arr)