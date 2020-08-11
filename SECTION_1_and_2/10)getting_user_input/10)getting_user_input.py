size_input = input("How big is your house in square feet?: ")
square_feet = int(size_input)
square_meters = square_feet / 10.8
print(f"the house is {square_meters:.2f} square meters or {square_feet} square feet")