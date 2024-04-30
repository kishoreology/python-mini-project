def add(n1, n2):
  return n1 + n2
def subtract(n1, n2):
  return n1 - n2
def multiply(n1, n2):
  return n1 * n2
def divide(n1, n2):
  return n1 / n2
operations = {"+": add,"-": subtract,"*": multiply,"/": divide}
def calculator():
  from art import logo
  print(logo)
  num1 = float(input("What's the first number?:"))
  for symbol in operations:
    print(symbol)
  should_continue = True
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    if input(f"Type 'y' to continue calculating {answer}, type 'n' to start new:")=='y':
      num1 = answer
    else:
      should_continue = False
      from replit import clear
      clear()
      calculator()
calculator()
