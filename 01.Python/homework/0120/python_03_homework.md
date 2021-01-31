# Workshop



## 1. List의 합 구하기

```
def list_sum(lst):
	total = 0
	for i in lst:
		total += i
    return total
```



## 2. Dictionary로 이루어진 List의 합 구하기

```
def list_sum(lst):
	total = 0
    for i in lst:
        total += i['age']
    return total
```



## 3. 2차원 List의 전체 합 구하기

```def list_sum(lst):
def list_sum(lst):
	total = 0
    for i in lst:
        for j in i:
            total += j
    return total
```



# Homework



## 1. Bulit-in 함수

1. 

`abs()`, `bool()`, `input()`, `range()`, `type()`

2. 

`print(dir(\__builtins__))`



## 2. 정중앙 문자

```
def get_middle_char(word):
	if len(word) % 2:
		return word[len(word) // 2: len(word) // 2 + 1]
	else:
		return word[len(word) // 2 - 1: len(word) // 2 + 1]
```



## 3. 위치 인자와 키워드 인자

(4) 

- 키워드 인자 뒤에는 위치 인자 사용 불가



## 4. 나의 반환값은

None

- result에 return된 값이 없음



## 5. 가변 인자 리스트

```def my_avg(*args):
def my_avg(*args):
	total = 0
    for i in args:
        total += i
    return total
```