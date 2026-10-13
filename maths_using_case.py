# match cases
op = input("enter your operator for arithmetic operation ")
a=int(input("Enter any Number : "))
b=int(input("Enter any Number : "))
match(op) :
  case "+":
    print("Addition : ",a+b)
  case "-":
    print("Substraction : ",a-b)
  case "*":
    print("Multiplication : ",a*b)
  case _:
    print("Invalid choice")
