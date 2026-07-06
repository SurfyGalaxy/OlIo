import random

MAX_INT_SIZE = 127
MIN_INT_SIZE = -128
difficulty = 2

def nonzero_int() -> int:
    if random.choice([True, False]):
        return random.randint(1, MAX_INT_SIZE)
    return random.randint(MIN_INT_SIZE, -1)

def make_new_problem() -> str:
    equation = [random.randint(MIN_INT_SIZE, MAX_INT_SIZE)]
    size = difficulty - 1
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
    equation = ''.join(str(item) for item in equation)
    return equation