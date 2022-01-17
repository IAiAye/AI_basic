from collections import Counter

text = """A press release is the quickest and easiest way to get free publicity. If
well written, a press release can result in multiple published articles about your
firm and its products. And that can mean new prospects contacting you asking you to
sell to them. ….""".lower().split()
print(Counter(text))
print(Counter(text)["a"])
