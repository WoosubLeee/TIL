# Workshop



## 1. 숫자의 의미

```
def get_secret_word(lst):
    word = ''
    for val in lst:
        word += chr(val)
    return word
```



## 2. 내 이름은 몇일까?

```
def get_secret_number(name):
    total = 0
    for char in name:
        total += ord(char)
    return total
```



## 3. 강한 이름

```def list_sum(lst):
def get_strong_word(a, b):
    a_total = 0
    for i in a:
        a_total += ord(i)
    b_total = 0
    for i in b:
        b_total += ord(i)

    if a_total > b_total:
        return a
    else:
        return b
```



# Homework



## 1. 이름 공간(Namespace)

LEGB

Local - Enclosed - Global - Built-in



## 2. 매개변수와 인자, 그리고 반환

(3)



## 3. 재귀 함수

- 장점 : 코드가 더 직관적이고 이해하기 쉬운 경우가 있다.
- 단점 : 메모리 스택이 넘치거나(Stack overflow) 프로그램 실행 속도가 늘어지는 단점이 생긴다.