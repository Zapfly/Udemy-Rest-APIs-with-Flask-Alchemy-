def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg
    return total

print(multiply(1, 3, 5))

#----------

def add(x, y):
    return x + y
nums = [3, 5]
print(add(*nums))
#----
nums2 = {"x":15, "y": 25}
print(add(**nums2)) #will pass the arguments based on the key names nums2["x"] will be the x argument

#----------

def apply(*args, operator):
    print(operator)
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "What you talking about willus?"

print("Final example")
print(apply(1, 3, 6, 7, operator="+")) #not working?