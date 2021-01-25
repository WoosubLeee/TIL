import json


def total(scores):
    total_score = 0
    # for문을 활용해 total_score에 scores 리스트 속의 값들을 더한다.
    for score in scores:
        total_score += score
    return total_score


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores_json = open('problem01_data.json')
    scores = json.load(scores_json)
    print(total(scores)) 
    # => 330