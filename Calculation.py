num1 = int(input("Enter a no."))
num2 = int(input("Enter 2nd no."))
cal = int(input("click 1 for addition, click 2 for minus, click 3 for prod, click 4 div "))
if(cal==1):
    print("Addition {num1} and {num2} gives: ",(num1+num2))
elif(cal==2):
    print("Minus {num1} and {num2} gives: ",(num1-num2))
elif(cal==3):
    print("Prod {num1} and {num2} gives: ",(num1*num2))
elif(cal==4):
    print("Division {num1} and {num2} gives: ",(num1%num2))
else:
    print("invalid input")
