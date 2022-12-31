
def add(a, b):
    ans = a + b
    ans1 = str(ans)
    print("Answer: " + ans1)

def sub(a,b):
    ans = a - b
    ans2 = str(ans)
    print("Answer: " + ans2)
def mul(a,b):
    ans = a * b
    ans3 = str(ans)
    print("Answer: " + ans3)

def div(a,b):
    ans = a / b
    ans4 = str(ans)
    print("Answer: " + ans4)
while True:
    print("A.ADD")
    print("B.SUBTRACT")
    print("C.MULTIPLY")
    print("D.DIVIDE")
    print("E.EXIT")

    cal = input("Arithmetic Operator: ")

    if cal == "a" or cal == "A":
        print("Addition")
        a = int(input("input first number: "))
        b = int(input("input the second number: "))
        add(a,b)
    elif cal == "b" or cal == "B":
        print("Subtraction")
        a = int(input("input first number: "))
        b = int(input("input the second number: "))
        sub(a,b)
    elif cal == "c" or cal == "C":
        print("Multiplication")
        a = int(input("input first number: "))
        b = int(input("input the second number: "))
        mul(a,b)
    elif cal == "d" or cal == "D":
        print("Division")
        a = int(input("input first number: "))
        b = int(input("input the second number: "))
        div(a,b)
    elif cal == "d" or cal == "D":
        print("Exit")
        quit()
