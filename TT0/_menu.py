from TT0 import animation, matrix, pattern, swap

from TT1 import fibonacci, lists

from TT2 import oop

# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------

def menu():
    title = "Main Menu!" + banner
    menu_list = main_menu.copy()
    buildMenu(title, menu_list)

def numbermenu():
    title = "Numbers!" + banner
    buildMenu(title, number_menu)

def datamenu():
    title = "Data!" + banner
    buildMenu(title, data_menu)

def visualmenu():
    title = "Visuals and Graphics!" + banner
    buildMenu(title, visual_menu)
  
# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------


main_menu = [
    ["Numbers and Math! ", numbermenu],
    ["Data! ", datamenu],
    ["Visuals and Graphics! ", visualmenu],
]

number_menu = [
    ["Matrix Keypad! ", matrix.matrix],
    ["Number Swap! ", swap.swap],
    ["Fibonacci Numbers! ", fibonacci.fibonacci],
    ["Oject Oriented Factorial! ", oop.factorial],  
]

data_menu = [
    ["Info Lists and Loops! ", lists.tester],
]

visual_menu = [
    ["Car Animation! ", animation.animation],
    ["Triangle Pattern! ", pattern.triangle_pattern],
]

border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------


def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again
