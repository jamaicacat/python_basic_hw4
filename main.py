import sys
import math

TYPE_TRIANGLE = 'Triangle'
TYPE_RECTANGLE = 'Rectangle'
TYPE_CIRCLE = 'Circle'


def validate_figure_parameters(_figure_type=None, *parameters):
    result = []

    if _figure_type:
        if _figure_type in [TYPE_CIRCLE, TYPE_RECTANGLE, TYPE_TRIANGLE]:
            _count = 0

            if _figure_type == TYPE_CIRCLE:
                _count = 1
            elif _figure_type == TYPE_RECTANGLE:
                _count = 2
            elif _figure_type == TYPE_TRIANGLE:
                _count = 3

            try:
                for elem in range(_count):
                    value = float(parameters[elem])
                    if value > 0:
                        result.append(value)
                    else:
                        print('Figure parameter cannot be less than or equal to 0.')
                        sys.exit()
            except Exception as error:
                raise error
        else:
            raise Exception(f'Unknown figure type: {_figure_type}')
    else:
        print('Figure type was not provided.')
        sys.exit()

    return result


def calculate_figure_perimeter(_figure_type=None, _a=None, _b=None, _c=None):
    if _figure_type:
        if _figure_type == TYPE_CIRCLE:  # radius
            return 2 * math.pi * _a
        elif _figure_type == TYPE_RECTANGLE:  # length & width
            return 2 * (_a + _b)
        elif _figure_type == TYPE_TRIANGLE:  # A, B, C sides ?
            return _a + _b + _c
        else:
            print('Unknown figure type.')
            sys.exit()
    else:
        print('Figure type was not provided.')
        sys.exit()


def calculate_figure_square(_figure_type=None, _a=None, _b=None, _c=None):
    if _figure_type:
        if _figure_type == TYPE_CIRCLE:  # radius
            return math.pi * (_a ** 2)
        elif _figure_type == TYPE_RECTANGLE:  # length & width
            return _a * _b
        elif _figure_type == TYPE_TRIANGLE:  # base & height ?
            return (_a * _b) / 2
        else:
            print('Unknown figure type.')
            sys.exit()
    else:
        print('Figure type was not provided.')
        sys.exit()


def print_figure_total(_figure_type=None, *parameters):
    if _figure_type:
        validated_parameters = validate_figure_parameters(_figure_type, *parameters)
        figure_perimeter = calculate_figure_perimeter(_figure_type, *validated_parameters)
        figure_square = calculate_figure_square(_figure_type, *validated_parameters)

        result_string = f'{_figure_type}:'

        if _figure_type == TYPE_CIRCLE:
            result_string = result_string + f' a = {parameters[0]};'
        elif _figure_type == TYPE_RECTANGLE:
            result_string = result_string + f' a = {parameters[0]}, b = {parameters[1]};'
        elif _figure_type == TYPE_TRIANGLE:
            result_string = result_string + f' a = {parameters[0]}, b = {parameters[1]} c = {parameters[2]};'

        result_string = result_string + f' perimeter = {figure_perimeter}, square: {figure_square}'

        print(result_string)
    else:
        print('Figure type was not provided.')
        sys.exit()

    return None


# использовал форматирование исключительно для того, чтобы показать что смотрел методы строк
print(' Welcome to the perimeter & square calculator! '.center(100, '-'))
print(' You can calculate these parameters for triangles, rectangles and circles. '.center(100, '*'))

input_string = input('Enter figure parameters: ')
values = input_string.split()
count = len(values)

if count == 1:
    a = input_string
    print_figure_total(TYPE_CIRCLE, a)
elif count == 2:
    a, b = values
    print_figure_total(TYPE_RECTANGLE, a, b)
elif count == 3:
    a, b, c = values
    print_figure_total(TYPE_TRIANGLE, a, b, c)
elif count == 0 or count > 3:
    print(f'Can\'t calculate perimeter & square for figure with {count} sides.')
    sys.exit()

print(' Program finished. Bye. '.center(100, '-'))
