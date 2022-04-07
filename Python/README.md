# Python

## Data structures

### Dictionaries

#### How to check if a dictionary is a subset of another dictionary

```python
# Python 3
if first.items() <= second.items():
    # true only if `first` is a subset of `second`
```

##### References

[Test if dict contained in dict](https://stackoverflow.com/questions/30818694/test-if-dict-contained-in-dict)



## Functions

### `zip()`

`zip()` 함수는 여러 개의 순회 가능한(iterable) 객체를 인자로 받고, 각 객체가 담고 있는 원소를 tuple의 형태로 차례로 접근할 수 있는 반복자(iterator)를 반환합니다.

```python
>>> numbers = [1, 2, 3]
>>> letters = ["A", "B", "C"]
>>> for pair in zip(numbers, letters):
...     print(pair)
...
(1, 'A')
(2, 'B')
(3, 'C')
```

#### unzip

`zip()` 함수로 엮어 놓은 데이터를 다시 해체(unzip)하고 싶을 때도 `zip()` 함수를 사용할 수 있습니다.

```python
>>> pairs = [(1, 'A'), (2, 'B'), (3, 'C')]
>>> numbers, letters = zip(*pairs)
>>> numbers
(1, 2, 3)
>>> letters
('A', 'B', 'C')
```

#### 활용

##### 병렬 처리

```python
>>> for number, upper, lower in zip("12345", "ABCDE", "abcde"):
...     print(number, upper, lower)
...
1 A a
2 B b
3 C c
4 D d
5 E e
```

##### dictionary 변환

```python
>>> keys = [1, 2, 3]
>>> values = ["A", "B", "C"]
>>> dict(zip(keys, values))
{1: 'A', 2: 'B', 3: 'C'}
```

### `getattr(object, name[, default])`

Return the value of the named attribute of *object*. *name* must be a string. For example, `getattr(x, 'foobar')` is equivalent to `x.foobar`. If the named attribute does not exist, *default* is returned if provided, otherwise `AttributeError` is raised.

```python
class sample:
    
    def __init__(self, x):
        self.x = x
    
    def foo(self):
        print('Hello, world!')
        
c = sample('woosub')

getattr(c, 'x') # woosub
getattr(c, 'foo') # sample.foo()
```

### References

[파이썬] 내장 함수 zip 사용법 (https://www.daleseo.com/python-zip/)



## input

### `sys.stdin.readline()`

#### Why use `sys.stdin.readline()` instead of `input()`?

Much faster.

#### How to use

`sys.stdin.readline()`은 한 줄 단위로 입력받기 때문에 개행문자(`\n`)까지 같이 받아진다. 문자열 형태로 저장하려면 `rstrip()`을 사용해 개행문자를 제거해야 한다.

```python
# 한 개의 문자열 or 정수를 입력받을 때
import sys
a = sys.stdin.readline().rstrip() # 한 개의 문자열
a = int(sys.stdin.readline()) # 한 개의 정수
```

```python
# 두 개 이상의 문자열 or 정수를 입력받을 때
a, b = sys.stdin.readline().split() # 두 개의 문자열
a, b = map(int, sys.stdin.readline().split()) # 두 개의 정수
```
### References

https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline ([Python 문법] 파이썬 입력 받기(sys.stdin.readline))

