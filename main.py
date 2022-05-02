from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def divide(n1, n2):
  return n1 / n2

def multiply(n1, n2):
  return n1 * n2

operations = {
  "+": add,
  "-": subtract,
  "/": divide,
  "*": multiply
}
def calculator():
  continue_calc = True
  print(logo)
  
  num1 = float(input("What is the first number? "))
  
  for operator in operations:
    print(operator)
  
  while continue_calc:
  
    operation_symbol = input("Pick an operator above. ")
    
    num2 = float(input("What is the second number? "))
    
    answer = operations[operation_symbol](num1,num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    cont_decision = input(f"Type \"y\" to continue calculating with {answer}, or type \"n\" to exit. ").lower()
  
    if cont_decision == "y":
      num1 = answer
    else:
      continue_calc = False
      calculator()

calculator()
  