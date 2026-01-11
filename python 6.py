num = float(input("Enter a number: "))
sqrt = num / 2

for i in range(10):
    sqrt = (sqrt + num / sqrt) / 2

print("Square root:", sqrt)
