import scientific_notation_calculations as snc

number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")

oper = input("Yapmak istediğiniz işlemi yazınız: (+, -, *, /): ")

if oper == "+":
    result = snc.add(number1, number2)
    print("The result is: ",result)
    resultScientific, power = snc.toScientificNotation(result, 0)
    print("The scientific representation of the result is {} x 10^{}".format(resultScientific, power))

if oper == "-":
    result = snc.sub(number1, number2)
    print("The result is: ",result)
    resultScientific, power = snc.toScientificNotation(result, 0)
    print("The scientific representation of the result is {} x 10^{}".format(resultScientific, power))
    
if oper == "*":
    result = snc.mul(number1, number2)
    print("The result is: ",result)
    resultScientific, power = snc.toScientificNotation(result, 0)
    print("The scientific representation of the result is {} x 10^{}".format(resultScientific, power))
    
if oper == "/":
    result = snc.div(number1, number2)
    print("The result is: ",result)
    resultScientific, power = snc.toScientificNotation(result, 0)
    print("The scientific representation of the result is {} x 10^{}".format(resultScientific, power))