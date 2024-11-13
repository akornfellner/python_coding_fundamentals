print("Einfacher Rechner")
print("=================")
print()

left_input = input("Linker Operand: ")
operation = input("Operation: ")
right_input = input("Rechter Operand: ")

left_number = float(left_input)
right_number = float(right_input)

result = 0

if operation == "+":
    result = left_number + right_number
elif operation == "-":
    result = left_number - right_number
elif operation == "*":
    result = left_number * right_number
elif operation == "/":
    result = left_number / right_number

print()
print(f"Ergebnis von {left_number} {operation} {right_number} ist {result}")
