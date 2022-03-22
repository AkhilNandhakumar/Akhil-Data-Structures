def swap():
    a = input("enter first number: ")
    b = input("enter second number: ")
    print("swapping if second number is less than first.")
    print(f"original sequence:  {a}, {b}")
    if b < a:
        b, a = a, b
    print(f"Sequence after swap: {a}, {b}")
    print("---------------------")