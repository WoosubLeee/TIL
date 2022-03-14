# Parametric search

## What is parametric search?

Parametric search는 Binary search와 매우 유사하다.

- 최적화 문제(문제의 상황을 만족하는 특정 변수의 최솟값, 최댓값을 구하는 문제)를 결정 문제(decision problem)로 바꾸어 푸는 것이다.
- 예를 들어 범위 내에서 조건을 만족하는 가장 큰 값을 찾으라는 최적화 문제라면 이분 탐색으로 결정 문제를 해결하면서 범위를 좁혀갈 수 있다.

### 예시

#### 문제)

자동차를 운전할 수 있는 사람 중 나이가 가장 어린 사람을 찾고자 한다. 이 때 자동차를 운전할 수 있는 나이는 19세 이상이다.

#### 풀이)

사람이 나열되어있고 이 사람들은 나이순으로 정렬되어있다. 이제 문제를 **결정 문제**로 바꾸어보자.

-> 자동차를 운전할 수 있나요?

![img](https://t1.daumcdn.net/cfile/tistory/99A1BC3359BA935F1A)

운전할 수 없는 경우 binary search와 같이 `mid + 1`을 하여 오른쪽 부분을 탐색한다.

![img](https://t1.daumcdn.net/cfile/tistory/9973833359BA935F0A)

운전할 수 있는 경우 왼쪽 부분을 탐색한다.

![img](https://t1.daumcdn.net/cfile/tistory/99AC663359BA936038)

![img](https://t1.daumcdn.net/cfile/tistory/993E783359BA93613F)

### 시간 복잡도

O(logN)



## 관련 문제

[BOJ 1654 랜선 자르기](https://www.acmicpc.net/problem/1654)



## References

