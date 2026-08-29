# this is calculator
name = input("Whats your good name? :")

"""====================================================="""
"""====================================================="""
print(f"""Hello {name}, Welcome to Python calculator.""")

choice = int(input("""What is you choice:
    1, Addition
    2, Subtraction
    3, Multiplication
    4, Division
    5, Reminder:"""))
 
x = int(input("Enter Integer 1:"))
y = int(input("Enter Integer 2:"))
# --------------------------------
# Addition
def Add( x, y):
    sum = x + y
    return print(" the answer is :" , sum)

# --------------------------------
# --------------------------------
# Subtraction
def Sub( x, y):
    sum = x - y
    return print(" the answer is :" , sum)


# --------------------------------
# --------------------------------
# Multiplication
def Mul( x, y):
    sum = x * y
    return print(" the answer is :" , sum)


# --------------------------------
# --------------------------------
# Divison

def Div( x, y):
    sum = x % y
    return print(" the answer is :" , sum)


# --------------------------------
# --------------------------------
# Reminder

def Rem( x, y):
    sum = x / y
    return """ the answer is :""" + sum


# --------------------------------
match choice:
    case 1:
        Add(x,y)
    case 2:
        Sub(x,y)
    case 3:
        Mul(x,y)
    case 4:
        Div(x,y)
    case 5:
        Rem(x,y)
        


