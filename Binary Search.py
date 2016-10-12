# __author__ = 'Scott Businge'

class ListComprehension(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b


class BinarySearch(ListComprehension):
    def search(self, count):
        return {count}

    while start <= end and not found:
        mid_point = (start + end) / 2

        num = self.__getitem__(mid_point)

        if num == value:
            found = True
            found_index = mid_point
            break
        else:
            if num > value:
                end = mid_point - 1
            else:
                start = mid_point + 1
        count += 1
