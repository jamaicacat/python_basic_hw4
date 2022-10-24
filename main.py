input_string = input()
values = input_string.split()
count = len(values)

if count == 1:
    a = input_string
elif count == 2:
    a, b = values
elif count == 3:
    a, b, c = values
