# __author__ = 'Scott Businge'

def max_min(array):                      # function definition
    ans = []                             # list to be checked
    max_num = max(array)
    min_num = min(array)
    for num in array:                    # for loop to iterate over list array
        if max_num == min_num:
            ans.append(len(array))
            return ans                   # returns output

    ans.append(min_num)                  # append to output definitive return
    ans.append(max_num)
    return ans

print(max_min([1, 3, 5, 46, 79, 40]))
