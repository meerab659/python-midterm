('''
addition
subtraction
multiplication
divition
''')
num1=int(input("enter the value num1"))
num2=int(input("enter the value num2"))
opr=input("enter the opr.....")         
if opr == "+":
    print(num1+num2)
elif opr == "-":
    print(num1-num2)
elif opr == "*":
    print(num1*num2)
elif opr == "/":
    print(num1/num2)
else:
    ("invalid opr....")
