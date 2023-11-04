from decimal import Decimal

def countSignificantFigures(number):
    isLeadingZero = True
    isEndingZero = False
    total = 0
    stringNumber = str(number)
    if -1 != stringNumber.rfind('.'):
        prevDot, afterDot = stringNumber.strip().split(".")
        if int(prevDot) != 0:
            total += len(prevDot)
            isLeadingZero = False
        for i in range(len(afterDot)):
            if int(afterDot) == 0:
                total += 1
                break
            elif afterDot[i] == "0" and isLeadingZero:
                continue
            else:
                isLeadingZero = False
                total += 1
    else:
        for i in range(len(stringNumber)):
            if isEndingZero:
                break
            if stringNumber[i] == "0":
                while i < len(stringNumber):
                    if stringNumber[i] != "0":
                        isEndingZero = False
                        break
                    i += 1
                if i == len(stringNumber):
                    isEndingZero = True
                else:
                    total += 1
            else:
                total += 1
                
    return total
    
def toScientificNotation(number, powder):
    while number >= 10 or number < 1:
        if number >= 10:
            number /= 10
            powder += 1
        else:
            number *= 10
            powder -= 1
    
    return number, powder

def power(base, powder):
    value = Decimal(1)
    i = 1
    if powder == 0:
        return 1
    elif powder > 0:
        while i <= powder:
            value *= base
            i += 1
    else:
        powder = -powder
        while i <= powder:
            value /= base
            i += 1
    
    
    return value

def roundnumber(number, fig):
    number = Decimal(number)
    
    
    if str(number).find(".") != -1:
        isleadzero = True
        k = 0
        prevDot, afterDot = str(number).strip().split(".")
        if prevDot == "0":
            fig += 1
            while isleadzero:
                if afterDot[k] != "0":
                    isleadzero = False
                    break
                fig+=  1
                k += 1
        if len(prevDot) >= fig:
            result = Decimal(str(number)[0:fig])
            if len(prevDot) == fig:
                if str(number)[fig + 1] != None and int(str(number)[fig + 1]) > 4:
                    result += 1
                    return Decimal(result)
                else:
                    return result
            if int(str(number)[fig]) > 4:
                result += 1
                result *= power(10, len(prevDot) - fig)
                return Decimal(result)
            else:
                result *= power(10, len(prevDot) - fig)
                return Decimal(result)
        else:
            try:
                result = Decimal(str(number)[0:fig])
                if int(str(number)[fig]) > 4:
                    afterr = str(result).strip().split(".")[1]
                    result += power(10, -len(afterr))
                return Decimal(result)
            except IndexError:
                return Decimal(result)
    else:
        try:
            result = Decimal(str(number)[0:fig])
            if int(str(number)[fig]) > 4:
                result += 1
            if len(str(result)) < len(str(number)):
                result *= power(10, len(str(number)) - len(str(result)))
            return result
        except:
            return number
def add(number1, number2):
    sigfig1 = 0
    sigfig2 = 0
    number1 = Decimal(number1)
    number2 = Decimal(number2)
    
    result = number1 + number2
    
    if str(number1).find(".") != -1:
        start1, end1 = str(number1).strip().split(".")
        sigfig1 = countSignificantFigures(Decimal(end1))
        
    if str(number2).find(".") != -1:
        start2, end2 = str(number2).strip().split(".")
        sigfig2 = countSignificantFigures(Decimal(end2))

    eksik_kisim = len(str(result).strip().split(".")[0])
    
    if sigfig1 < sigfig2:
        result = roundnumber(result, sigfig1 + eksik_kisim)
    else:
        result = roundnumber(result, sigfig2 + eksik_kisim)
    return result

def sub(number1, number2):
    sigfig1 = 0
    sigfig2 = 0
    number1 = Decimal(number1)
    number2 = Decimal(number2)
    
    result = number1 - number2
    
    if str(number1).find(".") != -1:
        start1, end1 = str(number1).strip().split(".")
        sigfig1 = countSignificantFigures(Decimal(end1))
        
    if str(number2).find(".") != -1:
        start2, end2 = str(number2).strip().split(".")
        sigfig2 = countSignificantFigures(Decimal(end2))

    eksik_kisim = len(str(result).strip().split(".")[0])
    
    if sigfig1 < sigfig2:
        result = roundnumber(result, sigfig1 + eksik_kisim)
    else:
        result = roundnumber(result, sigfig2 + eksik_kisim)
    return result

def mul(number1, number2):
    number1 = Decimal(number1)
    number2 = Decimal(number2)
    
    result = number1 * number2
    
    sigfig1 = countSignificantFigures(number1)
    sigfig2 = countSignificantFigures(number2)
    
    if sigfig1 < sigfig2:
        return roundnumber(result, sigfig1)
    else:
        return roundnumber(result, sigfig2)
    
def div(number1, number2):
    number1 = Decimal(number1)
    number2 = Decimal(number2)
    
    result = number1 / number2
    
    print(result)
    
    sigfig1 = countSignificantFigures(number1)
    sigfig2 = countSignificantFigures(number2)
    
    if sigfig1 < sigfig2:
        return roundnumber(result, sigfig1)
    else:
        return roundnumber(result, sigfig2) 
    