from decimal import Decimal


def count_significant_figures(number):
    """
   Computes the number of significant figures in a given number.

   Arguments:
   number (float or int): The number for which significant figures will be counted.

   Returns:
   int: The number of significant figures in the given number.

   Examples:
   >>> count_significant_figures(12345)
   5
   >>> count_significant_figures(0.00321)
   3
   >>> count_significant_figures(1000)
   1
   """
    is_leading_zero = True
    is_ending_zero = False
    total = 0
    string_number = str(number)
    if -1 != string_number.rfind('.'):
        prevDot, afterDot = string_number.strip().split(".")
        if int(prevDot) != 0:
            total += len(prevDot)
            is_leading_zero = False
        for i in range(len(afterDot)):
            if int(afterDot) == 0:
                total += 1
                break
            elif afterDot[i] == "0" and is_leading_zero:
                continue
            else:
                is_leading_zero = False
                total += 1
    else:
        for i in range(len(string_number)):
            if is_ending_zero:
                break
            if string_number[i] == "0":
                while i < len(string_number):
                    if string_number[i] != "0":
                        is_ending_zero = False
                        break
                    i += 1
                if i == len(string_number):
                    is_ending_zero = True
                else:
                    total += 1
            else:
                total += 1

    return total


def to_scientific_notation(number, power):
    """
    Converts a given number to scientific notation.

    Arguments:
    number (float): The number to be converted to scientific notation.
    power (int): The exponent (power of ten) to be used in the scientific notation.

    Returns:
    str: A string representing the number in scientific notation (e.g., "6.022e+23").

    Examples:
    >>> to_scientific_notation(62300, 23)
    (Decimal('6.23'), 27)
    """
    is_negative = False
    if number == 0:
        return number, 0
    elif number < 0:
        number = -number
        is_negative = True
    while number >= 10 or number < 1:
        if number >= 10:
            number /= 10
            power += 1
        else:
            number *= 10
            power -= 1
    if is_negative:
        return -number, power
    return number, power


def power(base, powder):
    """
    Calculate the result of raising a base number to the given exponent.

    Parameters:
    base (int or float): The base number to be raised to the power.
    exponent (int or float): The exponent to which the base is raised.

    Returns:
    int or float: The result of base raised to the power.
    """

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


def round_number(number, fig):
    """
    Rounds the given number to the specified number of significant figures.

    Args:
    number (float): The number to be rounded.
    fig (int): The number of significant figures to round to.

    Returns:
    float: The rounded number with the specified number of significant figures.

    Examples:
    >>> round_number(123.456789, 3)
    123
    >>> round_number(0.0023456, 4)
    0.002346
    >>> round_number(9876.54321, 2)
    9900
    """
    number = Decimal(number)

    if str(number).find(".") != -1:
        is_lead_zero = True
        k = 0
        prevDot, afterDot = str(number).strip().split(".")
        if prevDot == "0":
            fig += 1
            while is_lead_zero:
                if afterDot[k] != "0" and k <= len(afterDot):
                    is_lead_zero = False
                    break
                fig += 1
                k += 1
            fig += 1
        else:
            fig += 1
        if len(prevDot) >= fig:
            result = Decimal(str(number)[0:fig])
            if len(prevDot) == fig:
                if str(number)[fig + 1] is not None and int(str(number)[fig + 1]) > 4:
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
    """
    Adds two numbers and rounds the result based on the significant figures in the inputs.

    Args:
    number1 (float): The first number to be added.
    number2 (float): The second number to be added.

    Returns:
    float: The result of the addition, rounded to match the significant figures in the inputs.

    Examples:
    >>> add(123.456, 45.67)
    169.1
    >>> add(0.0025, 0.003)
    0.0055
    >>> add(1000, 5.678)
    1006.0
    """
    sigfig1 = 0
    sigfig2 = 0
    number1 = Decimal(number1)
    number2 = Decimal(number2)

    result = number1 + number2

    if str(number1).find(".") != -1:
        start1, end1 = str(number1).strip().split(".")
        sigfig1 = count_significant_figures(Decimal(end1))

    if str(number2).find(".") != -1:
        start2, end2 = str(number2).strip().split(".")
        sigfig2 = count_significant_figures(Decimal(end2))

    missing_part = len(str(result).strip().split(".")[0])

    if sigfig1 < sigfig2:
        result = round_number(result, sigfig1 + missing_part)
    else:
        result = round_number(result, sigfig2 + missing_part)
    return result


def sub(number1, number2):
    """
    Subtracts two numbers and rounds the result based on the significant figures in the inputs.

    Args:
    number1 (float): The first number to be subtracted from.
    number2 (float): The second number to subtract.

    Returns:
    float: The result of the subtraction, rounded to match the significant figures in the inputs.

    Examples:
    >>> sub(123.456, 45.67)
    77.79
    >>> sub(1000, 5.678)
    994
    """
    sigfig1 = 0
    sigfig2 = 0
    number1 = Decimal(number1)
    number2 = Decimal(number2)

    result = number1 - number2

    if str(number1).find(".") != -1:
        start1, end1 = str(number1).strip().split(".")
        sigfig1 = count_significant_figures(Decimal(end1))

    if str(number2).find(".") != -1:
        start2, end2 = str(number2).strip().split(".")
        sigfig2 = count_significant_figures(Decimal(end2))

    missing_part = len(str(result).strip().split(".")[0])

    if sigfig1 < sigfig2:
        result = round_number(result, sigfig1 + missing_part)
    else:
        result = round_number(result, sigfig2 + missing_part)
    return result


def mul(number1, number2):
    """
    Multiplies two numbers and rounds the result to match the least number of significant figures in the inputs.

    Args:
    number1 (float): The first number to be multiplied.
    number2 (float): The second number to be multiplied.

    Returns:
    float: The result of the multiplication, preserving the significant figures.

    Examples:
    >>> mul(12.34, 5.678)
    70.07
    >>> mul(0.0025, 0.003)
    0.000008
    >>> mul(12345, 0.000123)
    1.52
    """
    number1 = Decimal(number1)
    number2 = Decimal(number2)

    result = number1 * number2

    sigfig1 = count_significant_figures(number1)
    sigfig2 = count_significant_figures(number2)

    if sigfig1 < sigfig2:
        return round_number(result, sigfig1)
    else:
        return round_number(result, sigfig2)


def div(number1, number2):
    """
  Divides two numbers and rounds the result to match the least number of significant figures in the inputs.

  Args:
  number1 (float): The dividend.
  number2 (float): The divisor.

  Returns:
  float: The result of the division, rounded to match the least number of significant figures in the inputs.

  Examples:
  >>> div(12.34, 5.678)
  2.173
  >>> div(0.0025, 0.003)
  0.8
  >>> div(12345, 0.000123)
  100400000
  """
    number1 = Decimal(number1)
    number2 = Decimal(number2)

    result = number1 / number2

    sigfig1 = count_significant_figures(number1)
    sigfig2 = count_significant_figures(number2)

    if sigfig1 < sigfig2:
        return round_number(result, sigfig1)
    else:
        return round_number(result, sigfig2)
