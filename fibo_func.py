def recu_fibo(n):
    if n <= 1:
        return n
    else:
        return(recu_fibo(n-1)+ recu_fibo(n-2))
nterms= int(input("Enter any no. : "))
if nterms<=0:
    print("Enter a Positive Value")
else:
    print("Fibonacci Series :")
    for i in range(nterms):
        print(recu_fibo(i))
