import collections


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        str_value = '(' + str(self.start) + ',' + str(self.end) + ')'
        return str_value
