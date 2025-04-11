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

# def Goutham(x,n):
#     n = n%len(x)
#     res = [0]*len(x)
#     for i in range(len(x)):
#         res[(i+n)%len(x)] = x[i]
#     return res

# arr = [1,2,3,4,5]
# n = 2

# print(Goutham(arr,n))


# def Step(x,n):
#     n = n%len(x)
#     res = [0]*len(x)
#     for i in range(len(x)):
#         res[(i+n)%len(x)] = x[i]
#     return res

# arr = [1,2,3,4,5,6,7,8,9]
# x= 3
# print(Step(arr,x))





# arr1 = [1, 2, 3]
# arr2 = [2, 3, 4]
# def intersection(x,z):
#     res = []
#     for i in x:
#         for j in z:
#             if i == j and i not in res:
#                 res += [i]
#     return res

# print(intersection(arr1,arr2))



arr = [1,2,3,4,5]
# n = 2
# def count(arr,n):
#     n = n%len(arr)
#     res = [0]*len(arr)
#     for i in range(len(arr)):
#         res[(i+n)%len(arr)] = arr[i]
#     return(res)
# print(count(arr,n))


# arr1=[1,2,3,4,5,6,8]
# arr2=[2,4,57,57,4,6,3]
# def intersection(x,z):
#     res=[]
#     for i in x:
#         for j in z:
#             if i == j and i not in res:
#                 res += {i}
#     return res
# print(intersection(arr1,arr2))


# arr=[23,24,25,27]
# def missingnumber(x):
#     total = ((len(x)+1)*(len(x)+2))//2
#     sum =0
#     for i in x:
#         sum += i
#     return total-sum
# print(missingnumber(arr))



# def max(x):
#     firsthigest=x[0]
#     secondhigest=x[1]
#     if firsthigest<secondhigest:
#         firsthigest,secondhigest=secondhigest,firsthigest
    
#     for i in x[2:]:
#         if i >firsthigest:
#             secondhigest = firsthigest
#             firsthigest =i
#         elif i >secondhigest:
#             secondhigest=i
#     return firsthigest*secondhigest

# arr = [1,2,3,4,5,6,7]
# print(max(arr))


# arr = [1,2,3,4,5]
# step = 2
# def rotate(arr,n):
#     n = n % len(arr)
#     res = [0]*len(arr)
#     for i in range(len(arr)):
#         res[(i+n)%len(arr)] = arr[i]
#     return res

# print(rotate(arr,step))


# arr1=[1,2,3,4,5,6,7,8,9]
# arr2=[3,5,6,3,6,7,55]
# def intersection(x,z):
#     res=[]
#     for i in x:
#         for j in z:
#             if i == j and i not in res:
#                 res += [i]
#     return res
# print(intersection(arr1,arr2))


# arr = [1,2,4,5]
# def missing(x):
#     total = ((len(x)+1)*(len(x)+2))//2
#     sum =0
#     for i in x:
#         sum +=i
#     return total-sum
# print(missing(arr))


# arr = [1,2,3,4,5]
# def product(x):
#     first = x[0]
#     second = x[1]
#     if first < second:
#         first,second = second,first
    
#     for i in x[2:]:
#         if i > first:
#             second = first
#             first = i
#         elif i > second:
#             second = i
#     return first*second

# print(product(arr))



# arr=[0,1,0,23,0,5,6]
# def zeros(x):
#     res=[0]*len(x)
#     index = 0
#     for i in x:
#         if i != 0:
#             res[index]=i
#             index += 1
#     return res
# print(zeros(arr))


arr = [1,2,3,4,5,6,7,89]
target = 7

def goutham(x,z):
    res=[]
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if x[i]+x[j]==z:
                res += [[x[i],x[j]]]
    return res

print(goutham(arr,target))