def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        print("Erreur : division par zéro !")
        return None
    return a / b

def average(numbers):
    if len(numbers) == 0:
        print("Erreur : liste vide !")
        return None
    return sum(numbers) / len(numbers)

if __name__ == "__main__":
    print("Addition 2 + 3 =", add(2, 3))
    print("Soustraction 5 - 2 =", sub(5, 2))
    print("Multiplication 4 * 3 =", mul(4, 3))
    print("Division 10 / 2 =", div(10, 2))
    print("Moyenne de [2, 4, 6] =", average([2, 4, 6]))
