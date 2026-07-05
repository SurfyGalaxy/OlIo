import random

MAX_INT_SIZE = 127
MIN_INT_SIZE = -128
difficulty = 10

def make_new_problem() -> tuple:
    operator = random.randint(1, 4)
    a = random.randint(MIN_INT_SIZE, MAX_INT_SIZE)
    b = random.randint(MIN_INT_SIZE, MAX_INT_SIZE)

    if a == 0 and b == 0:
        a = nonzero_int(a)


    if operator == 1: 
        operator = "+"
    elif operator == 2:
        operator = "-"
    elif operator == 3:
        operator = "*"
    else:
        operator = "/"
        if b == 0:
            b = nonzero_int()
    
    return (a, operator, b)

def nonzero_int() -> int:
    if random.choice([True, False]):
        return random.randint(1, MAX_INT_SIZE)
    return random.randint(MIN_INT_SIZE, -1)

def make_new_problem() -> list:
    equation = [random.randint(MIN_INT_SIZE, MAX_INT_SIZE)]
    size = difficulty
    while size > 0:
        operator = random.randint(1, 4)
        if operator == 1:
            equation.append("+")
            equation.append(random.randint(MIN_INT_SIZE, MAX_INT_SIZE))
        elif operator == 2:
            equation.append("-")
            equation.append(random.randint(MIN_INT_SIZE, MAX_INT_SIZE))
        elif operator == 3:
            equation.append("*")
            equation.append(random.randint(MIN_INT_SIZE, MAX_INT_SIZE))
        else:
            equation.append("/")
            equation.append(nonzero_int())
        size -= 1
    return equation
