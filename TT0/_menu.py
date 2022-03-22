from TT0 import animation, matrix, pattern, swap

from TT1 import fibonacci, lists


# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------


def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    buildMenu(title, menu_list)

def submenu0():
    title = "Week 0" + banner
    buildMenu(title, sub_menu0)

def submenu1():
    title = "Week 1" + banner
    buildMenu(title, sub_menu1)

def submenu2():
    title = "Week 2 - Menu" + banner
    buildMenu(title, sub_menu2)

  
# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------


main_menu = [
    ["Week 0", submenu0],
    ["Week 1", submenu1],
    ["Week 2", submenu2],
]

sub_menu0 = [
    ["Animation", animation.animation],
    ["Swap", swap.swap],
    ["Triangle Pattern", pattern.triangle_pattern],
    ["Matrix Keypad", matrix.matrix],
]

sub_menu1 = [
    ["Fibonacci", fibonacci.fibonacci],
    ["InfoDB Lists/Loops", lists.tester],
]

sub_menu2 = [
    ["OOP Temp", None],
    ["Temp", None],
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
