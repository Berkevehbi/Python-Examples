import scientific_notation_calculations as snc

number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")

operation_input = input("Write the operation you want to perform: (+, -, *, /): ")

if operation_input == "+":
    result = snc.add(number1, number2)
    print("The result is: ", result)
    resultScientific, power = snc.to_scientific_notation(result, 0)
    print("The scientific representation of the result is {} x 10^{}".format(resultScientific, power))

if operation_input == "-":
    result = snc.sub(number1, number2)
    print("The result is: ", result)
    resultScientific, power = snc.to_scientific_notation(result, 0)
    print("The scientific representation of the result is {} x 10^{}".format(resultScientific, power))
    
if operation_input == "*":
    result = snc.mul(number1, number2)
    print("The result is: ", result)
    resultScientific, power = snc.to_scientific_notation(result, 0)
    print("The scientific representation of the result is {} x 10^{}".format(resultScientific, power))
    
if operation_input == "/":
    result = snc.div(number1, number2)
    print("The result is: ", result)
    resultScientific, power = snc.to_scientific_notation(result, 0)
    print("The scientific representation of the result is {} x 10^{}".format(resultScientific, power))
