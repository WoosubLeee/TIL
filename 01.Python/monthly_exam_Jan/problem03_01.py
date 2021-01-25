import json


def check(data):
    count = 0
    # 이중 for문을 활용하여 각 날, 각 시간대의 체온 정보에 접근
    for i in data:
        for j in i:
            # 체온이 37.5도 이상이라면 count에 1 추가
            if j >= 37.5:
                count += 1
                # count가 3에 도달하면 True return
                if count == 3:
                    return True
            else:
                # 37.5도 미만이라면 count 0으로 초기화
                count = 0
    # 반복문 동안 count가 3에 도달한 적이 없다면 False return            
    return False


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    temperature_json = open('problem03_data.json', encoding='UTF8')
    temperature_list = json.load(temperature_json)
    print(check(temperature_list))
    # => True