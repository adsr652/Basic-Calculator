def recu_fact(num):
    if num==1:
        return num
    else:
        return num * recu_fact(num-1)
num= int(input("Enter any no. : "))
if num < 0:
    print("Factorial cannot be found for negative integer")
elif num==0:
    print("Factorial of 0 is 1")
else:
    print("Factorial of", num, "is: ", recu_fact(num))
