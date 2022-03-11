import time
keypad = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          [" ", 0, " "]]

# Menu options as a dictionary
menu_options = {
    1: 'Animation',
    2: 'Numbers',
    3: 'Pattern',
    4: 'Exit'
}

submenu_numby = {
  1: 'Matrix',
  2: 'Swap',
  3: 'Exit'
}

# Print menu options from dictionary key/value pair
def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key] )
    runOptions1()

def print_submenu():
    for key in submenu_numby.keys():
      print(key, '--', submenu_numby[key])
    runOptions2()

# menu option 1

ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[3;0H\u001B[2"
ANIMATION_COLOR = u"\u001B[31m\u001B[2D"
RESET_COLOR = u"\u001B[0m\u001B[2D"

def animation_print(position):
    print(ANSI_HOME_CURSOR)
    print(RESET_COLOR)
    sp = " " * position
    print(ANIMATION_COLOR, end="")
    print(sp + "  ______")
    print(sp + " /|_||_\`.__")
    print(sp + "|   _    _ _\"")
    print(sp + "=`-(_)--(_)-'")
    print(RESET_COLOR)

def animation():
  start = 0
  distance = 30 
  step = 1

  for position in range(start, distance, step):
      animation_print(position)  
      time.sleep(.1)


def matrix():
    for i in keypad:
        for j in i:
            print(j, end=" ")
        print()

def pattern():
  row = int(input('Enter number of rows required: '))
    
  for i in range(row):
      for j in range(row-i):
          print(' ', end='')
    
      for j in range(2*i+1):
          print('*',end='')
      print()
  print("---------------------")
      
def swap():
  a = input("enter first number: ")
  b = input("enter second number: ")
  print("swapping if second number is less than first.")
  print(f"original sequence:  {a}, {b}")
  if b < a:
      b, a = a, b
  print(f"Sequence after swap: {a}, {b}")
  print("---------------------")


# call functions based on input choice
def runOptions1():
    # infinite loop to accept/process user menu choice
    while True:
        try:
            option = int(input('Enter your choice 1-3: '))
            if option == 1:
                animation()
                print_menu()
            elif option == 2:
                print_submenu()
                print_menu()
            elif option == 3:
                pattern()
                print_menu()
            # Exit menu    
            elif option == 4:  
                print('Exiting! Thank you! Good Bye...')
                exit() # exit out of the (infinite) while loop
            else:
                print('Invalid option. Please enter a number between 1 and 4.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')

def runOptions2():
    # infinite loop to accept/process user menu choice
    while True:
        try:
            option = int(input('Enter your choice 1-3: '))
            if option == 1:
                matrix()
                print_menu()
            elif option == 2:
                swap()
                print_menu()
            # Exit menu    
            elif option == 3:  
                print('Exiting! Thank you! Good Bye...')
                exit() # exit out of the (infinite) while loop
            else:
                print('Invalid option. Please enter a number between 1 and 4.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')
        
if __name__=='__main__':
    print_menu()