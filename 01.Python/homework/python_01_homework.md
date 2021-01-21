# Homework

>서울 3반 이우섭

> 데이터 & 제어문



## 1. Python 예약어

- Python에서 사용할 수 없는 식별자(예약어)
  - `False`, `None`, `True`, `and`, `as`, `assert`, `async`, `await`, `break`, `class`, `continue`, `def`, `del`, `elif`, `else`, `except`, `finally`, `for`, `from`, `global`, `if`, `import`, `in`, `is`, `lambda`, `nonlocal`, `not`, `or`, `pass`, `raise`, `return`, `try`, `while`, `with`, `yield`



## 2. 실수 비교

- `num1 = 0.1 * 3`
  `num2 = 0.3`
  - `round(num1, 1) == num2`



## 3. 이스케이프 시퀸스

1. 줄 바꿈 : `\n`
2. 탭 : `\t`
3. 백슬래시 : `\\`



## 4. String Interpolation

- "안녕, 철수야"
  1. `%-formatting`
     - `print('안녕, %s야' % name)`
  2. `str.format()`
     - `print('안녕, {}야'.format(name))`
  3. `f-strings`
     - `print(f'안녕, {name}야')`



## 5. 형 변환

1. `str(1) = 1`
2. `int('30') = 30`
3. `int(5) = 5`
4. `bool('50') = False`
5. `int('3.5')`
   - String -> float -> int 는 불가능하다



## 6. 네모 출력

- `n = 5`
  `m = 9`
  - `print(('*'*n + '\n') * m)`



## 7. 이스케이프 시퀸스 응용

```
print("\"파일은 c:\\Windows\\Users\\내문서\\Python에 저장이 되었습니다.\"\n나는 생각했다. \'cd를 써서 git bash로 들어가 봐야지.\'")
```



## 8. 근의 공식

- `x1 = (-b + ((b**2 - 4*a*c) ** 0.5)) / 2a`
- `x2 = (-b - ((b**2 - 4*a*c) ** 0.5)) / 2a`

