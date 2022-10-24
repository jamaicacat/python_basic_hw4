import math

input_string = input('Input figure parameters: ')
values = input_string.split()
count = len(values)

if count == 1:
    a = float(input_string)

    if a <= 0:
        raise Exception('Radius of the circle can\'t be less than or equal to 0.')

    perimeter = 2 * math.pi * a
    square = math.pi * (a ** 2)

    print(f'Circle: a = {a}; perimeter = {perimeter}, square = {square}')
elif count == 2:
    a, b = map(float, values)

    if a <= 0 or b <= 0:
        raise Exception('Rectangle can\'t have side with length less than or equal to 0.')

    perimeter = 2 * a + 2 * b
    square = a * b

    print(f'Rectangle: a = {a}, b = {b}; perimeter = {perimeter}, square = {square}')
elif count == 3:
    a, b, c = map(float, values)

    if a <= 0 or b <= 0 or c <= 0:
        raise Exception('Triangle can\'t have side with length less than or equal to 0.')

    if a + b < c or a + c < b or b + c < a:
        raise Exception('Triangle with such sides lengths can\'t exist.')

    semi_perimeter = (a + b + c) / 2

    perimeter = semi_perimeter * 2
    square = math.sqrt(semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c))

    print(f'Triangle: a = {a}, b = {b}, c = {c}; perimeter = {perimeter}, square = {square}')

