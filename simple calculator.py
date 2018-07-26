def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
print('enter operation:+-*/')
s= input ()
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if s== '+':
   print(x,"+",y,"=", add(x,y))

elif s == '-':
   print(x,"-",y,"=", sub(x,y))

elif s == '*':
   print(x,"*",y,"=", mul(x,y))

elif s == '/':
   print(x,"/",y,"=", div(x,y))
else:
   print("Invalid input")
