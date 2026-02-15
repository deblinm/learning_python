def calculate (a,b, operation):
    if operation.lower() == "total":
        return a+b
    elif operation.lower() == "difference":
        return a-b
    elif operation.lower() == "product":
        return a*b
    elif operation.lower() == "division":
        return a/b
    elif operation.lower() == "remainder":
        return a%b
    else:
        raise ValueError("Invalid operation")


a = 10
b = 3

# print sum, difference, product, division

result=calculate(a,b,operation="total")
print (result)
result=calculate(a,b,operation="difference")
print (result)
result=calculate(a,b,operation="product")
print (result)
result=calculate(a,b,operation="division")
print (result)
result=calculate(a,b,operation="remainder")
print (result)

country = "USA"
years = 5

# print: I have lived in USA for 5 years
print(f"I have lived in {country} for {years} years")


x = "10"
y = 10
print(int(x) + y)
