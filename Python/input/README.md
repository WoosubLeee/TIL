# input(Python)

## `sys.stdin.readline()`

### Why use `sys.stdin.readline()` instead of `input()`?

Much faster.

### How to use

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



## References

https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline ([Python 문법] 파이썬 입력 받기(sys.stdin.readline))