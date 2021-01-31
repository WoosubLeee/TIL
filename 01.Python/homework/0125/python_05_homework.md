# Workshop



## 1. 평균 점수 구하기

```
import statistics


def get_dict_avg(dict_score):
    return statistics.mean(dict_score.values())
```

statistics의 mean fuction을 활용하여 평균을 구합니다.



## 2. 혈액형 분류하기

```
def count_blood(blood_list):
    for i in blood_list:
        if i not in blood_dict:
            blood_dict[i] = 1
        else:
            blood_dict[i] += 1
    return blood_dict
```



# Homework



## 1. 모음은 몇 개나 있을까?

```
def count_vowels(word):
    count = 0
    for i in 'aeiou':
        count += word.count(i)
    return count
```

for문을 활용해 각 모음이 word에 들어가 있는지 조회합니다.



## 2. 문자열 조작

(4)

한쪽만 지정할 수도 있고, 특정 문자를 지정하지 않으면 공백을 찾아 제거합니다.



## 3. 정사각형만 만들기

```
def only_square_area(list_a, list_b):
    list_square = []
    for a in list_a:
        # list_a와 list_b에서 서로 같은 값에 대해서만 반환값 리스트에 append
        if a in list_b:
            list_square.append(a**2)
    return list_square
```

