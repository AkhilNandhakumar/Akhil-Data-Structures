def fibonacci(i):  
   if i <= 1:  
       return i  
   else:  
       return(fibonacci(i-1) + fibonacci(i-2))  
 

length = int(input("Length of sequence: "))
if length <= 0:
   print("Enter a positive number")  
else:  
   for j in range(length):  
       print(fibonacci(j))