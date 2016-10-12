# __author__ = 'Scott Businge'

def find_missing(list1, list2):             # function definition
    longer = list(set(list1) - set(list2))
    if len(longer) == 0:
        longer = list(set(list2) - set(list1))  # checks what is in one that is not in another
    if len(list1 + list2) == 0:
        longer = 0
    if list2 == list1:                       # if equal len, returns none
        longer = 0
    if longer != 0:
        return longer[0]                     # returns element
    else:
        return 0
