# Workshop



## 1. 무엇이 중복일까

```
def duplicated_letters(word):
    # 데이터 중복을 막기 위해 set 사용
    result = set()
    for char in word:
        # char의 갯수가 2 이상이면 result에 add
        if word.count(char) >= 2:
            result.add(char)
    return list(result)
```



## 2. 소대소대

```
def low_and_up(word):
    result = ''
    for i in range(len(word)):
        # 짝수번째 알파벳은 대문자로 만들고
        if i % 2:
            result += word[i].upper()
        # 홀수번째 알파벳은 그대로 추가
        else:
            result += word[i]
    return result
```



## 3. 숫자의 의미

```
def lonely(numbers):
    result = []
    # 시작할 때 temp는 numbers에 담기지 않을 숫자 -1로 initialize
    temp = -1
    for num in numbers:
        # num이 이전 숫자와 같지 않다면 result에 append하고 temp를 num으로 변경
        if num != temp:
            result.append(num)
            temp = num
    return result
```



# Homework



## 1. Built-in 함수와 메서드

```
import random


ran_num = random.sample(range(100), 5)
print(ran_num)
# >>> [85, 30, 73, 21, 49]

print(sorted(ran_num))
# >>> [21, 30, 49, 73, 85] 정렬된 값을 반환
print(ran_num)
# >>> [85, 30, 73, 21, 49] 원본은 변형 X

ran_num.sort()
print(ran_num)
# >>> [21, 30, 49, 73, 85] 원본을 변형
```



## 2. .extend()와 .append()

```
univ1 = ['서울대', '연세대']
univ1.append('고려대')
print(univ1)

# >>> ['서울대', '연세대', '고려대']
#  list에 값 자체를 추가하기 때문에 string 전체가 추가됨

univ2 = ['서울대', '연세대']
univ2.extend('고려대')
print(univ2)

# >>> ['서울대', '연세대', '고', '려', '대']
#  string을 iterable로 인식하여 한 character씩 각각 추가됨
```





## 3. 복사가 잘 된 건가?

변수 a에 담긴 list의 요소를 변경하였을 때
변수 b에 담긴 list의 요소도 변경되었다.

이는 a와 b가 모두 같은 index를 참조하고 있다고 볼 수 있으므로 담긴 list의 요소가 같다고 볼 수 있다.

