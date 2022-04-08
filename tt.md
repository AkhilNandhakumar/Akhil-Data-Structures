{% include nav.html %}

# Tech Talk Work + Data Structures Projects

***

### Table of Contents:
- [Replit Runtime](#runtime)
- [Week 0 Details](#tt0-details)
- [Week 1 Details](#tt1-details)
- [Week 2 Details](#tt2-details)

*** 

### Runtime:
        
 <iframe height="600px" width="600x" src="https://replit.com/@AkhilNandhakuma/Akhil-Data-Structures?lite=true"></iframe>       


***

### TT0 Details
- Worked on making a menu with submenus for python
- Made the static menu, need to still make the menu using proper data structures and try/excepts

***

### TT1 Details
- Added infoDB to menu under LISTS
- Added Fibonacci recursive to menu under NUMBERS

Python For Loops  
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).  
This is less like the for keyword in other programming languages, and **works more like an iterator method** as found in other object-orientated programming languages.
With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.  
The range() Function:  
To **loop through a set of code a specified number of times**, we can use the range() function,  
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

Recursion means a defined function can call itself.  
The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. There must be a **termination/exit condition** that allows the function to exit without calling itself. This condition allows the recursion to stop - that is, without it the function would call itself over and over again, resulting in an error.
However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.
***

### TT2 Details
- Created a Class to do factorials using OOP method
```
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
```
- Created a Class to raise a number to an exponent that is the same value as itself using OOP
- Made an imperative version of the same thing.
```
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
def imperative_exponent(num):
  if num <= 0 or num > 20:
    print(f"Error! Selected numbber: {num}. Please use an integer from 1-20.")
    return num
  else:
    value = (num**num)
    print(f"Base Number was {num}, {num}^{num} is {value}.")
```
- Created a Class to determine whether or not 
a phrase/word is a palindrome, included error 
support to notify where the palidrome is 
discontinued. 
```
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
                count = count + 1

            else:
                print(f"Error found at letter #{i+1} in '{self.user_input}', "
                      f"which was the letter '{self.user_input[i]}'.")
                break

        if count == self.length:
            print(f"The word/phrase, '{self.word}', is a Palindrome.")

        else:
            print(f"The word/phrase, '{self.word}', is not a Palindrome.")
```
***
