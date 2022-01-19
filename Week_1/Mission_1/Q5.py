from curses.ascii import isdigit


def find_string(inputs):
    for i in inputs:
        if i.isdigit() is True:
            inputs = inputs.replace(i, " ")
    return inputs.split()


inputs = "cat32dog16cow5"

string_list = find_string(inputs)
print(string_list)
