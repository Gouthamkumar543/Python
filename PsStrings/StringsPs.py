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


# def goutham(x):
#     new = ""
#     for i in range(len(x)-1,-1,-1):
#         new += x[i]
        
#     if x == new:
#         return True
#     return False
    
    
# arr = "racecar"
# print(goutham(arr))



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


# find the longest wrd -1

# def find_longest_word(s):
#     longest = ""
#     word = ""
    
#     for i in range(len(s)):
#         if s[i] != ' ':
#             word += s[i]
#             # print(word)
#         else:
#             if len(word) > len(longest):
#                 longest = word
#             word = ""
    
#     if len(word) > len(longest):
#         longest = word

#     return longest

# s = "The quick brown fox jumps over the lazy dogssssss "
# print(find_longest_word(s))




# find the first non repeating letter -3
# def Non_duplicate(x):
#     for i in range(len(x)):
#         # print("i values",i)
#         unique = True
#         for j in range(len(x)):
#             # print(j)
#             if i != j and x[i] == x[j]:
#                 unique = False
#                 break
#         if unique:
#             return x[i]
#     return None 

# s = "swwiss"
# print(Non_duplicate(s)) 
