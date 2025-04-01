# easy lvl
# reverse the string -1

# def Reverse_Srting(x):
#     new_String = ""

#     for i in range(len(x)-1,-1,-1):
#         new_String += x[i]
#     print(new_String)

# string = "goutham"
# Reverse_Srting(string)


# Check if the string is pallinedrome or not -2

# def pallinedrome(x):
#     p_string = x[::-1]
#     # print(p_string)
#     if x == p_string:
#         return print(True)
#     return print(False)

# string="racecar"
# pallinedrome(string)



# Check vowles and update the count -3

# def Vowles_count(x):
#     count = 0
#     vowles = "aeiouAEIOU"
#     for i in x:
#         if i in vowles:
#             count += 1
#     return print(count)

# string = "hello"
# Vowles_count(string)


#we can take vowles value as single word or array of single letters


#removing vowles from the string -4

# def Removing_vowles(x):
#     new_string = ""
#     vowles = ["a","e","i","o","u","A","E","I","O","U"]
#     for i in x:
#         if i not in vowles:
#             new_string += i
#     print(new_string)

# srting = "goutham"
# Removing_vowles(srting)




# Check if String Contains Only Digits -5
# def is_digit(x):
#     for i in x:
#         if not("0"<=i<="9"):
#             return False
#     return True

# print(is_digit("12345"))






# Check if it contains only digits -5

# def Check_Only_Digits(x):
#     Digits = "1234567890"
#     for i in x:
#         if i not in Digits:
#             return print(False)
#     return print(True)

# string = "00368375"
# Check_Only_Digits(string)




#Convert String to Title Case -6
# def titlecase(x):
#     res = ""
#     cap = True
#     for i in x:
#         if cap and "a"<=i<="z":
#             res += chr(ord(i)-32)
#         else:
#             res += i
#         cap = (i==' ')
#     print(res)

# titlecase("hello goutham all")




# Convert String to Number -7
# def to_num(x):
#     res = 0
#     for i in x:
#         digit = ord(i)- ord("0")
#         res = res*10+digit
#     print(res)

# to_num("123")







# Count Occurrences of a Character -8  
# def char_count(x,z):
#     count = 0 
#     for i in x:
#         if i == z:
#             count += 1
#     return count

# print(char_count("hello world","l"))




# medium lvl

# Routate the arr based on steo count -1

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

# arr = [1,2,3,4,5,7,8,9]
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
