import re
 
# -------------------------------------------------------

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

# -------------------------------------------------------

class Exponent:
  def __init__(self, number):
    self.number = number 
  
  def __call__(self):
    if self.number <= 0 or self.number > 20:
      print(f"Error! selected number was {self.number}. please use an integer from 1-20.")
      return self.number
    else:
      value = (self.number**self.number)
      print(f"Base Number was {self.number}, {self.number}^{self.number} is {value}")

# -------------------------------------------------------

class Palindrome:
    def __init__(self, word):
        self.word = word
        self.user_input = re.sub("[^a-zA-Z0-9]+", "", word.lower())
        self.length = len(self.user_input)

    def __call__(self):
        flipped = self.user_input[::-1]
        count = 0
        for i in range(0, self.length):
            print(f"Starting char: '{self.user_input[i]}' --> Ending char: '{flipped[i]}'")
            if self.user_input[i] == flipped[i]:
                count +=1
            else:
                print(f"Error found at letter #{i+1} in '{self.user_input}', "
                      f"which was the letter '{self.user_input[i]}'.")
                break

        if count == self.length:
            print(f"The word/phrase, '{self.word}', is a Palindrome.")

        else:
            print(f"The word/phrase, '{self.word}', is not a Palindrome.")


def palindrome():
    print("--------------------------------------------")
    print("")
    pal3 = Palindrome(word="This doesnt siht...")
    pal3()
    print("")
    print("--------------------------------------------")
    print("")
    pal2 = Palindrome(word="I love dogs!")
    pal2()
    print("")
    print("--------------------------------------------")
    print("")
    pal3 = Palindrome(word="A man, a plan, a canal, panama.")
    pal3()
    print("")
    print("--------------------------------------------")
    print("")
    pal1 = Palindrome(word="Bob, Race Car, Bob.")
    pal1()
    print("")
    print("--------------------------------------------")
   
# -------------------------------------------------------

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

    
  print("testing self exponent using base 9:")
  ex3()
  
  print("------------------------------")
  
  print("testing bound error:")
  ex4()

# -------------------------------------------------------

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

# -------------------------------------------------------

def imperative_exponent(num):
  if num <= 0 or num > 20:
    print(f"Error! Selected numbber: {num}. Please use an integer from 1-20.")
    return num
  else:
    value = (num**num)
    print(f"Base Number was {num}, {num}^{num} is {value}.")


def imp_call():
  print("------------------------------")
  print("testing self exponent using base 5:")
  imperative_exponent(5)
  print("------------------------------")
  print("testing self exponent using base 2:")
  imperative_exponent(2)
  print("------------------------------")
  print("testing self exponent using base 9:")
  imperative_exponent(9)
  print("------------------------------")
  print("testing bound error:")
  imperative_exponent(50)

# -------------------------------------------------------