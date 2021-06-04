print("This is the Program Of Prime Number")
initial = int(input("Enter initial range: "))  
final = int(input("Enter final range: "))  
  
for num in range(initial,final + 1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           print(num)  
