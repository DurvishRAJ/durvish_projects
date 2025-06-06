print("**********CALCULATOR**********")


a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))

select=int(input("Select the operation to perform:\n 1.Addition\n 2.subtraction\n 3.Multiplication\n 4.Division\n 5.Modulus\n 6.Exponentiation\n 7.Floor division\n Enter your choice:"))

if select==1:
    print("Addition of two numbers is:",a+b)
  
elif select==2:
  print("Subtraction of tow no. is:",a-b)

elif select==3:
  print("Multiplication of two no. is:",a*b)

elif select==4:
  print("Division of two no.is:",a/b)

elif select==5:
  print("Modulus of tow no. is:",a%b)

elif select==6:
  print("Exponentiation of tow mo. is:",a**b)

elif select==7:
  print("Floor Division of tow no. is:",a//b)

else:
  print("Invalid Choice -_-")

print("**********THANK YOU**********")
