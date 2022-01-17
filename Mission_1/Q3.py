score = [(100, 100), (95, 90), (55, 60), (75, 80), (70, 70)]


def get_avg(score):
    j = 1
    for i in score:
        avg = sum(i) / 2
        print(f"{j} 번, 평균 : {avg}")
        j += 1


get_avg(score)
