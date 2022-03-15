# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars

InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({  
               "FirstName": "Akhil",  
               "LastName": "Nandhakumar",  
               "DOB": "Novermber 1",  
               "Residence": "San Diego",  
               "Email": "akhil@nandhakumar.net",  
               "Fav_Cars":["2020 Dodge Charger","2022 Mercedes AMG Black Series","2008 Kia Rio"]  
              })  

InfoDb.append({  
               "FirstName": "Joe",  
               "LastName": "Joe",  
               "DOB": "April 20",  
               "Residence": "San Diego",  
               "Email": "joe@joe.com",  
               "Fav_Cars":["joe mobile","joe mobile","joe mobile"]  
              })

# given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])  # using comma puts space between values
    print("\t", "Cars: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Fav_Cars"]))  # join allows printing a string list with separator
    print()

# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion
## hack 2a: def for_loop()
## hack 2b: def while_loop(0)
## hack 2c : def recursive_loop(0)
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)

def while_loop(n):
  while n < len(InfoDb):
      print_data(n)
      n += 1
  return

def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)

def recur_factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * recur_factorial(n-1)


def factorial_tester():
    num = int(input("Enter a number for factorial: "))
    # check if the number is negative
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    else:
        print("The factorial of", num, "is", recur_factorial(num))

def tester():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion

