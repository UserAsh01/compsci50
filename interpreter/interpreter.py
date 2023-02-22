#prompt user for math expression
expr = input("Expression: ")

#split into 3 parts : x, operator, z
x, op, z = expr.split()

x = int(x)
z = int(z)

#calulate result based on operator
if op == "+":
    result = x + z
elif op == "-":
    result = x - z
elif op == "*":
    result = x * z
elif op == "/":
    result = x / z


