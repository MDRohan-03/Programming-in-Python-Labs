base = int(input("Enter the base: "))
power = int(input("Enter the power: "))

result = 1

for i in range(power):
    result = result * base

print("Result:", result)