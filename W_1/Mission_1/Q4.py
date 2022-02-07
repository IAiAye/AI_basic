""" 내가 짠 코드
dict_second = {"사과": 5, "감": 25, "배": 15, "귤": 25}


def merge_dict(dict_first, dict_second):
    for i in dict_first.keys():
        for j in dict_second.keys():
            if i == j:
                dict_first[i] = int(dict_first[i]) + int(dict_second[j])

    dict_second.update(dict_first)

    return dict_second


print(merge_dict(dict_first, dict_second))
"""
from collections import Counter  # Collection 모듈(강의자료 python_datastructure p42 참조)

dict_first = {"사과": 30, "배": 15, "감": 10, "포도": 10}
dict_second = {"사과": 5, "감": 25, "배": 10, "귤": 25}


def merge_dict(dict_first, dict_second):
    counter_first = Counter(dict_first)
    counter_second = Counter(dict_second)
    print(dict(counter_first + counter_second))


merge_dict(dict_first, dict_second)
