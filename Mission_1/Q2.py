sentence = "way a is there will a is there Where"


def reverse_sentence(sentence):
    reverse_words = sentence.split()[::-1]
    reverse_sentence = " ".join(reverse_words)
    return reverse_sentence


print(reverse_sentence(sentence))
