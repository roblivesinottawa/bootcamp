def calculate(**kwargs):
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0),
    }

    is_float = kwargs.get('make_float', False)

    operation_value = operation_lookup[kwargs.get('operation', '')]

    if is_float:
        final = f"{kwargs.get('message', 'the result is')} {float(operation_value)}"
    else:
       final = f"{kwargs.get('message', 'the result is')} {int(operation_value)}" 
    return final


print(calculate(make_float=False, operation='add', message='you just added', first=2, second=4))
