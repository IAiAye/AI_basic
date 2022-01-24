def tag_func(tag, text):
    tag = tag
    text = text

    def inner_func():
        return "<{0}>{1}<{0}>".format(tag, text)

    return inner_func


h1_func = tag_func("title", "This is Python Class")
p_func = tag_func("p", "Data Academy")

print(h1_func)
print(p_func)
