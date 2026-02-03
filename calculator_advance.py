def calculator(a, b, op):
    return {"+": a+b, "-": a-b, "*": a*b, "/": a/b}.get(op, "Invalid operator")

print(calculator(10,20,"+"))