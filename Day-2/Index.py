num=int(input("enter a number"))
res=0
for i in range(1,num//2+1):
    if (num%i==0):
        print(i)
        res += i
print(res==num)
if(res==num):
    print(num, "it is perfect number")
else:
    print(num, "it is not perfect number")
