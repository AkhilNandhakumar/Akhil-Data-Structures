class Factorial:
  def __init__(self, number):
    self.number = number 
  
  def __call__(self):
    if self.number < 0:
      print("Error! please enter a positive number.")
      return self.number
    if self.number == 1:
      return self.number
    else:
      value = 1
      for i in range (1, (self.number)+1):
        value = value*i
        print(f"Step: {i} - Value: {value}")
      print(f"Final value is {value}")


class Exponent:
  def __init__(self, number):
    self.number = number 
  
  def __call__(self):
    if self.number <= 0 or self.number > 20:
      print(f"Error! You inputted {self.number}. please enter an integer from 1-20.")
      return self.number
    else:
      value = (self.number**self.number)
      print(f"Base Number was {self.number}, {self.number}^ {self.number} is {value}")


def exponent():
  ex1 = Exponent(5)
  ex2 = Exponent(2)
  ex3 = Exponent(9)
  ex4 = Exponent(50)

  print("------------------------------")
  
  print("testing self exponent using base 5:")
  ex1()
  
  print("------------------------------")
  
  print("testing self exponent using base 2:")
  ex2()
  
  print("------------------------------")

    
  print("testing self exponent using base 2:")
  ex3()
  
  print("------------------------------")
  
  print("testing bound error:")
  ex4()
  

def factorial():
  fact1 = Factorial(3)
  fact2 = Factorial(5)
  fact3 = Factorial(-2)
  
  print("------------------------------")
  
  print("testing factorial of 3:")
  fact1()
  
  print("------------------------------")
  
  print("testing factorial of 5")
  fact2()
  
  print("------------------------------")
  
  print("testing error neg. value")
  fact3()
  
  print("------------------------------")
