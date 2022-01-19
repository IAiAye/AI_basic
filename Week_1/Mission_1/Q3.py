score = [(100, 100), (95, 90), (55, 60), (75, 80), (70, 70)]

""" 내가 짠 코드
def get_avg(score):
    j = 1
    for i in score:
        avg = sum(i) / 2
        print(f"{j} 번, 평균 : {avg}")
        j += 1
 """


def get_avg(score):
    enumerated_list = enumerate(score)
    for i in enumerated_list:
        print(f"{i[0]}번, 평균 : {sum(i[1])/2}")


get_avg(score)
