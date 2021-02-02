# Python 과목평가 대비

#### 주석

- 여러 줄의 주석은
  1. 한 줄 씩 `#`을 사용해서 표현하거나,
  2. `"""` 또는 `'''`(여러줄 문자열, multiline string)으로 표현할 수 있습니다. (multiline은 주로 함수/클래스를 설명(docstring)하기 위해 활용됩니다.)

#### 코드 라인

- 한 줄로 표기할때는 `;`을 작성하여 표기할 수 있다.

#### 할당 연산자

- 같은 값 동시 할당

  `x = y = 10`

#### 식별자

- 식별자의 이름은 영문알파벳(대문자와 소문자), 밑줄(_), 숫자로 구성된다.
- 첫 글자에 숫자가 올 수 없다.
- 길이에 제한이 없다.
- 대소문자(case)를 구별한다.
- 아래의 키워드는 사용할 수 없다. [파이썬 문서](https://docs.python.org/ko/3/reference/lexical_analysis.html#keywords)

```
False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield
```

#### 데이터 타입

- 숫자(Number) 타입

  1. `int`

     - 파이썬에서 표현할 수 있는 가장 큰 수

       - 파이썬은 기존 C 계열 프로그래밍 언어와 다르게 정수 자료형(integer)에서 오버플로우가 없다.
       - 임의 정밀도 산술(arbitrary-precision arithmetic)을 사용하기 때문이다.

       - 오버플로우(overflow)
         - 데이터 타입 별로 사용할 수 있는 메모리의 크기가 제한되어 있다.
         - 표현할 수 있는 수의 범위를 넘어가는 연산을 하게 되면, 기대했던 값이 출력되지 않는 현상, 즉 메모리가 차고 넘쳐 흐르는 현상

       - 임의 정밀도 산술(arbitrary-precision arithmetic)
         - 사용할 수 있는 메모리양이 정해져 있는 기존의 방식과 달리, 현재 남아있는 만큼의 가용 메모리를 모두 수 표현에 끌어다 쓸 수 있는 형태
         - 특정 값을 나타내는데 4바이트가 부족하다면 5바이트, 더 부족하면 6바이트까지 사용할 수 있게 유동적으로 운용

  2. `float`

     - 실수를 컴퓨터가 표현하는 과정에서 부동소수점을 사용하며, 항상 같은 값으로 일치되지 않습니다. (floating point rounding error)

       1. ```
          a = 3.5 - 3.12
          b = 0.38
          
          abs(a - b) <= 1e-10
          >>> True
          ```

       2. ```
          import sys
          abs(a - b) <= sys.float_info.epsilon
          >>> True
          ```

       3. ```
          import math
          math.isclose(a, b)
          >>> True
          ```

     - 컴퓨터식 지수 표현 방식

       - e를 사용할 수도 있다.(e와 E 둘 중 어느 것을 사용해도 무방)

     - `round()`

       - 0~4는 내림, 5는 동일하게 작동하지 않고 반올림 방식에 따라 다릅니다.
       - 짝수에서 5는 내림 / 홀수에서 5는 올림

  3. `complex`

     - 복소수는 허수부를 `j`로 표현합니다.
     - 문자열을 변환할 때, 문자열은 중앙의 + 또는 - 연산자 주위에 공백을 포함해서는 안 됩니다.

- 글자(String) 타입

  - 이스케이프 시퀸스

    | 예약문자 | 내용(의미)      |
    | -------- | --------------- |
    | \n       | 줄 바꿈         |
    | \t       | 탭              |
    | \r       | 캐리지리턴      |
    | \0       | 널(Null)        |
    | \\\      | \\              |
    | \\`      | 단일인용부호(`) |
    | \\"      | 이중인용부호(") |

  - String interpolation

    1. `%-formatting`

       - `%d` : 정수

       - `%f` : 실수

       - `%s` : 문자열

       - ```
         print('Height : %d, Weight : %f, Name : %s' % (72, 173.8, '이우섭'))
         >>> Height : 72, Weight : 173.800000, Name : 이우섭
         ```

    2. `str.format()`

    3. `f-strings`

- 참/거짓(Boolean) 타입

  - 다음은 `False`로 변환됩니다.
    - `0, 0.0, (), [], {}, '', None`

- 형변환

  - 암시적 형변환

    - boolean과 integer는 더할 수 있다.

      - ```
        True + 5
        >>>6
        ```

#### 연산자

- ```
  quotient, remainder = divmod(5, 2)
  >>> quotient = 2, remainder = 1
  ```

- 