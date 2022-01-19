num_list = [1, 5, 7, 15, 16, 22, 28, 29]


def get_odd_num(num_list):
    odd_list = []
    for i in num_list:
        if i % 2 == 1:
            odd_list.append(i)
    return odd_list


print(get_odd_num(num_list))
