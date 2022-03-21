# fibonacci code
def fibonacci():
    num = int(input("Enter sequence length: "))
  # checks if input is valid
    if num < 0:
        print("Enter a number greater than 0")
    else:
      #calls recursion fuction, repeats n times for input
        for n in range(num):
            print(print_fib(n))

def print_fib(i):
  # if the input is 1 or 0, only return the first number
    if i <= 1:
        return i
  # recursion to return a valus, and use that value to re run the function to get the next number.    
    else:
        return(print_fib(i-2) + print_fib(i-1))