op = input("enter your operator for arithmetic operation ")
a=10
b=30
match(op) :
  case "+":
    print("Addition : ",a+b)
  case "-":
    print("Substraction : ",a-b)
  case "*":
    print("Multiplication : ",a*b)
  case _:
    print("Invalid choice")
