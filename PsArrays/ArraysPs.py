# easy lvl

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





# find the second largest number -2

# def goutham(x):
#     max1 = x[0]
#     max2 = x[1]
    
#     if max2 > max1:
#         max1,max2 = max2,max1
        
#     for i in range(2,len(x)):
#         print(i)
#         if x[i] > max1:
#             max2 = max1
#             max1 = x[i]
#         elif x[i] > max2:
#             max2 = x[i]
#     return max2
    
# arr =  [3, 1, 4, 1, 5, 9]
# print(goutham(arr))




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



# medium lvl

# Routate the arr based on step count -1

# def rotate_array(arr, k):
#     k = k % len(arr)
#     result = [0] * len(arr)
#     for i in range(len(arr)):
#         result[(i + k) % len(arr)] = arr[i]
#     return result

# arr = [1,2,3,4,5]
# k = 3
# print(rotate_array(arr, k))




# insection of 2 arrays -2
# def intersection(x,z):
#     res = []
#     for i in x:
#         for j in z:
#             if i == j and i not in res:
#                 res += [i]
#     return res

# arr1 = [1, 2, 3]
# arr2 = [2, 3, 4]
# print(intersection(arr1, arr2))





# find the missing number -3 
# def Missing(x):
#     total = (len(x)+1)*(len(x)+2)//2
#     sum = 0
#     for i in x:
#         sum += i
#     return total - sum

# arr = [1,2,3,5]
# print(Missing(arr))





# find the max products of 2 numbers -4
# def Max(x):
#     max1=x[0]
#     max2=x[1]
#     if max1 < max2:
#         max1,max2 = max2,max1

#     for i in x[2:]:
#         if i > max1:
#             max2 = max1
#             max1 = i
#         elif i > max2:
#             max2 = i
#     return max1 * max2

# arr = [1,12,3,4,5,7,8,9]
# print(Max(arr))



# Move zeros to end - 5
# def Zero_to_end(x):
#     new_arr = [0] * len(x)
#     index = 0
#     for i in range(len(x)):
#         if x[i] != 0:
#             new_arr[index] += x[i]
#             index +=1
#     return new_arr

# arr = [28,10,450,1,0,2,3,4,5]
# print(Zero_to_end(arr))


# pair the sum of arry to the given target - 6
# def pair_sum(arr, target):
#     pairs = []
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i] + arr [j] == target:
#                 pairs += [[arr[i], arr[j]]]
#     return pairs

# arr = [2, 4, 3, 5, 7, 8, 9]
# target = 7
# print(pair_sum(arr, target))



# find peack element - 7
# def find_peak(arr):
#     n = len(arr)
    
#     if n == 1:
#         return arr[0]
#     if arr[0] >= arr[1]:
#         return arr[0]
#     if arr[n-1] >= arr[n-2]:
#         return arr[n - 1]
    
#     for i in range(1, n - 1):
#         if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
#             return arr[i]
    
#     return None

# arr = [1,2,1,]
# print(find_peak(arr))
 


# find the first duplicate -8 
# def Duplicate(x):
#     for i in range(len(x)):
#         for j in range(i+1,len(x)):
#             if x[i] == x[j]:
#                 return x[i]
#     return None

# arr = [2, 1,2,3, 3, 5,5]
# print(Duplicate(arr))





# Flatten a Nested Array -9
       
# def flatten_array(arr):
#     result = []
    
#     def flatten(sub_arr):
#         for i in sub_arr:
#             if isinstance(i, list):
#                 flatten(i)
#             else:
#                 result += [i]
    
#     flatten(arr)
#     return result

# arr = [1, [2, [3, [4]], 5]]
# print(flatten_array(arr))
