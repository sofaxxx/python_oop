import math


def is_odd(a):
    if a % 2 == 0:
        return True
    else:
        return False
def random_numbers():
    count1 = 0
    count2 = 0
    list_of_numbers = [i for i in range(0,1000)]
    for i in list_of_numbers :
        if is_odd(i) == True:
            count2 += 1
        elif is_odd(i) == False :
            count1 += 1
    numbers = {
        "odd" : count1,
        "even" : count2

    }
    print(numbers)
def multiple(*args):
    mul = [*args]
    count = 0
    print(mul)
    for i in range(len(mul)):
        count += 1
        answer = math.prod(mul)
    print(answer)
def process_order(*args, **kwargs):
    order_info = {
        "Продукты" : args,
        "Информация " : kwargs

    }
    return order_info

def calculate():
    act = str(input("Действие :"))
    def sum():
        a = float(input("1 число"))
        b = float(input("2 число"))
        print( a + b)

    def prod():
        a = float(input("1 число"))
        b = float(input("2 число"))
        print( a * b)

    def sub():
        a = float(input("1 число"))
        b = float(input("2 число"))
        print(a - b)

    def div():
        a = float(input("1 число"))
        b = float(input("2 число"))
        print(a/b)
    if act == "*":
        prod()
    elif act == "/":
        div()
    elif act == "-":
        sub()
    else :
        sum()
calculate()
