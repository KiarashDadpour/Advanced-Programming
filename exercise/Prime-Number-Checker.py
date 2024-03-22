# This Python code determines whether a given number is prime or not.

num = int(input("enter a number : "))
flag = 0
if num > 0:
    for i in range(2, (num//2)+1):
        if num % i == 0:
            flag = 1
            print("non-prime")
            break
else:
    flag = 1
    print("invalid number !")
if flag == 0:
    print("prime")
  
