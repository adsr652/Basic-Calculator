def pat(rows):
    for row in range(1,rows+1):
        for column in range(1, row+1):
            print("*",end=" ")
        print()
a=int(input("Enter No. of rows :"))   
pat(a)




'''
no_rows=int(input("Enter any no. : "))
for row in range(1, no_rows+1):
    for column in range(1, row+1):
        print("*",end=" ")
    print()

''''
