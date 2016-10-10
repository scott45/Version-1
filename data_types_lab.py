# __author__ = 'Scott Businge'


# def definition
def data_type(value):
    if type(value) is str:
        return len(value)

# in case of no value
    elif value is None:
        return 'no value'

# in case it's boolean
    elif type(value) is bool:
        if value is True:
            return True
        return False

# in case it's int
    elif type(value) is int:
        if value < 100:
            return 'less than 100'
        elif value == 100:
            return 'equal to 100'
        else:
            return 'more than 100'
# if it's a list
    elif type(value) is list:
        if len(value) >= 3:
            return value[2]
        else:
            return None


'''
# comment
used the built in type() function to check the type of argument passed. for examlpe, to to check whether a value is an
 integer, do: if type(value) == int, for strings, do :if type(value) == str, for booleans, do: if value is True/False
'''
