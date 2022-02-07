file_path = "./data-01-test-score.csv"


def read_file(file_path):
    score_list = []
    with open(file_path) as test_scores:

        datas = test_scores.readlines()
        for data in datas:
            data = data.strip()
            score_list.append(data.split(","))

    return score_list


print(read_file(file_path))
