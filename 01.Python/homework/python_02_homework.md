# Homework

서울 3반 이우섭



## 1. mutable & immutable

- mutable
  - list, set, dictionary
- immutable
  - string, tuple, range



## 2. 홀수 list

```list(range(1, 51))[::2]```



## 3. dictionary 생성

`{이우섭: 27, 이태용: 21, 정희진: 22, 이지원: 23}`



## 4. 반복문으로 네모 출력

```for i in range(m):
    for j in range(n):
        if j == n - 1:
            print('*')
        else:
            print('*', end='')```
```



## 5. 조건 표현식

`print('입실 불가') if temp >= 37.5 else print('입실 가능')`'



## 6. list 평균값

```total = 0
for i in scores:
    total = total + i
scores_average = total / len(scores)
print(scores_average)```
```