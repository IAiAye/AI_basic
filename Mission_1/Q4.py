dict_first = {"사과": 30, "배": 15, "감": 10, "포도": 10}
dict_second = {"사과": 5, "감": 25, "배": 15, "귤": 25}


def merge_dict(dict_first, dict_second):
    for i in dict_first.keys():
        for j in dict_second.keys():
            if i == j:
                dict_first[i] = int(dict_first[i]) + int(dict_second[j])

    dict_second.update(dict_first)

    return dict_second


print(merge_dict(dict_first, dict_second))
