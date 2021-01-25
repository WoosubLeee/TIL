import json


def rotate(data):
    am = []
    pm = []
    # for문을 활용하여 각 날의 체온 정보에 접근
    for i in data:
        # 아침 체온은 am 리스트에 추가
        am.append(i[0])
        # 저녁 체온은 pm 리스트에 추가
        pm.append(i[1])
    # 각 리스트를 dict_data 딕셔너리에 통합
    dict_data = {}
    dict_data['am'] = am
    dict_data['pm'] = pm
    return dict_data


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    temperature_json = open('problem03_data.json', encoding='UTF8')
    temperature_list = json.load(temperature_json)
    print(rotate(temperature_list))
    # => {
    #     'am': [36.7, 36.9, 37.8, 36.7, 36.3, 36.5, 36.8], 
    #     'pm': [36.5, 37.5, 37.8, 36.5, 36.4, 36.5, 36.6]
    # }
