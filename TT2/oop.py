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
