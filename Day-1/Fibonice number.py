num = input ("enter number:")
sum = 0

def fib(n):
    a,b=0,1
    while True:
        if a>n:
            return True
        if a>n:
            return False
        a,b=b,a+b

for i in num:
    if (fib(int(i))):
        sum += int(i)
print(sum)
