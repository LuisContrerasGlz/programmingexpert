"""

Write a generator that accepts a string and an integer called frequency

string[0]

*

frequency

+ string[1] ✶

frequency

+ ... +

string[-2]

✶

frequency

+

string[-1]

* frequency.

Your generator should not store this string, it should generate the next element in the sequence each time its next called.

You should create this generator in both a functional and class based way. Your functional generator should be named generate_string and your class based generator (a.k.a iterator) should be named GenerateString.

You may assume that frequency >= 0

"""


def generate_string(string, frequency):
    for char in string:
        for _ in range(frequency):
            yield char


class GenerateString:
    def __init__(self, string, frequency):
        self.string = string
        self.frequency = frequency

    def __iter__(self):
        self.current_char_index = 0
        self.char_counter = 0
        return self

    def __next__(self):
        if self.char_counter >= self.frequency:
            self.char_counter = 0
            self.current_char_index += 1

        if self.current_char_index >= len(self.string):
            raise StopIteration

        self.char_counter += 1
        return self.string[self.current_char_index]
