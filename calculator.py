def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def divison(x,y):
    if y==0:
        print("Zero Divison Error!")
        return None
    return x/y
def average(x,y):
    return (x+y)/2
def calculator():
    while True:
        print("Select Operator!")
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Divison")
        print("5.Average")
        print("6.Exit")
        choose=input("Enter Choice:")
        if choose == '6':
            print("Good Day!")
            break
        if choose in ('1','2','3','4','5'):
            try:
                n1=float(input("Enter First Value:"))
                n2=float(input("Enter Second Value:"))
            except ValueError:
                print("Invalid Input")
                continue
            if choose == '1':
                print(f"{n1}+{n2}={add(n1,n2)}")
            elif choose == '2':
                print(f"{n1}-{n2}={subtract(n1,n2)}")
            elif choose == '3':
                print(f"{n1}*{n2}={multiplication(n1,n2)}")
            elif choose == '4':
                print(f"{n1}/{n2}={divison(n1,n2)}")
            elif choose == '5':
                print(f"Average of {n1} and {n2}={average(n1,n2)}")
        else:
            print("Invalid Input!")
calculator()