# # functions

# def sum(a,b):
#     print(a+b)

# sum(345,45678)


# def Loop(a):
#     for i in range(10):
#         if ( a <= 10):
#             print(i+a)


# # a is not increasing becz a is single value
# Loop(8)


# # return

# def sub (x,y):
#     return(x-y)


# # return nedd to stord in variable 
# result = sub(100,10)
# print(result)


# # without parameters we can call functions
# def cal():
#     for i in range(0,2):
#         for j in range(0,2):
#             print("i value :",i,"and j value :",j," = ",i+j)

# cal()


# def avg(x,y,z):
#     Avg = (x+y+z)/3
#     return(Avg)

# numbers = avg(12345,5654,4554)
# print(numbers)




# # default values when parameters are not passed then the in line values are passed as parameters
# def product(a=3,b=5):
#     print(a*b)

# # product(10,7)
# product()




# passing only one pareameter will assign the value for first parameter 
# def product(a,b=5):
#     print(a*b)

# product(10)
# product()



# not possible
# def product(a=2,b):
#     print(a*b)

# product(10)



# # recursion

# def factorial(n):
#     if(n == 0 or n == 1):
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(3))