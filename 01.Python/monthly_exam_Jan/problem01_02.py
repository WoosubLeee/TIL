import json


def average(scores):
    total_score = 0
    # problem01_01과 같은 방법으로 total 점수를 구한다.
    for score in scores:
        total_score += score
    # total 점수를 scores 리스트의 길이로 나눠 평균을 구한다.
    avg_score = total_score/len(scores)
    return avg_score


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores_json = open('problem01_data.json')
    scores = json.load(scores_json)
    print(average(scores)) 
    # => 82.5