# Dequeue(덱)

Dequeue은 Double-Ended Queue의 줄임말로,

양방향으로 데이터를 넣고 뺄 수 있는 자료구조이다. Stack과 Queue의 특성을 모두 갖는, 둘을 조합한 형태의 자료구조라 할 수 있다.

![img](https://media.vlpt.us/images/falling_star3/post/10df11e7-f1b7-4e8d-ae57-7224ab2af1fa/2.JPG)

Dequeue의 4가지 핵심 함수는 다음과 같다.

- 앞으로 넣기
- 뒤로 넣기
- 앞에서 빼기
- 뒤에서 빼기



## Python에서 구현하기

`collections` 모듈에 `deque`라는 클래스로 이미 구현되어 있다.

```python
from collections import deque

d = deque()

# 앞으로 넣기
d.appendleft(0)

# 뒤로 넣기
d.append(0)

# 앞에서 빼기
d.popleft()

# 뒤에서 빼기
d.pop()
```



## References

https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=isaac7263&logNo=221507063144

https://velog.io/@falling_star3/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%8A%A4%ED%83%9DStack%ED%81%90Queue%EB%8D%B1Deque

https://mong9data.tistory.com/50