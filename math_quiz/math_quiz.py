import random


def generateRandomNumbers(min, max):
    # function to generate random numbers
    """
    Random integer.
    """
    return random.randint(min, max)


def generateOperator():
    return random.choice(['+', '-', '*'])


def calculation(n1, n2, o):
    if ( type(n1) is int and type(n2) is int):
        p = f"{n1} {o} {n2}"
        # operator '+' for the addition 
        if o == '+': a = n1 + n2
        # operator '-' for the subtraction 
        elif o == '-': a = n1 - n2
        # operator '*' for the multiplication
        else: a = n1 * n2
        return p, a

    else:
    # check for type(n1) is int and type(n2) is int
        raise TypeError("Invalid number type")

def math_quiz():
    s = 0
    t_q = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        n1 = generateRandomNumbers(1, 10); n2 = generateRandomNumbers(1, 5.5); o = generateOperator()

        PROBLEM, ANSWER = calculation(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
