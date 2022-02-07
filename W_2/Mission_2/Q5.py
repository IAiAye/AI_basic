file_path = "./data-01-test-score.csv"


class ReadSCV:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        score_list = []
        with open(self.file_path) as test_scores:

            while True:
                data = test_scores.readline().replace("\n", "")
                if not data:
                    break
                score_list.append(data.split(","))
        return score_list

    def merge_list(self):
        sum_list = []
        with open(self.file_path) as test_scores:

            while True:
                data = test_scores.readline().replace("\n", "")
                if not data:
                    break
                data_sum = 0
                for i in data.split(","):
                    i = int(i)
                    data_sum += i
                sum_list.append(data_sum / 4)
        return sorted(sum_list)


read_csv = ReadSCV(file_path)
print(read_csv.read_file())
print(read_csv.merge_list())
