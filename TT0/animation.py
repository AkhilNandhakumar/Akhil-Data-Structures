import time

ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[3;0H\u001B[2"
ANIMATION_COLOR = u"\u001B[31m\u001B[2D"
RESET_COLOR = u"\u001B[0m\u001B[2D"

def animation_print(position):
    print(ANSI_CLEAR_SCREEN)
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
