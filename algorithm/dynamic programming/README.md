# Dynamic programming

> 동적계획법

## What is dynamic programming?

DP, 즉 Dynamic Programming은 하나의 큰 문제를 여러 개의 작은 문제로 나누어서 그 결과를 저장하여 다시 재활용하며 해결하는 알고리즘 설계 기법이다. 원리는 간단하다. 처음 진행되는 연산은 기록해 두고, 이미 진행했던 연산이라면 다시 연산하는 것이 아니라 기록된 값을 가져오는 것이다.

### Memoization

하위 문제를 해결하고 그 결과값을 저장하여 동일한 연산을 반복하지 않도록 하는 기법을 **Memoization(메모이제이션)**이라고 한다.

### Divide and Conquer(분할 정복)과의 차이점

분할 정복과 동적계획법은 주어진 문제를 작게 쪼개서 다수의 하위 문제를 사용해 큰 문제를 해결한다는 점은 같다. 차이점은, 분할 정복은 하위 문제가 반복해서 일어나지 않고, 동적계획법은 반복해서 발생한다는 것이다.

예를 들어, Merge sort의 경우, 하위 문제로 반복해서 분할하지만, 해당 하위 문제들이 반복해서 발생하지는 않는다.



## 사용 조건

### 1. Overlapping subproblems(겹치는 부분 문제)

하위 문제들이 반복해서 나타나는 경우에 사용이 가능하다.

### 2. Optimal substructure(최적 부분 구조)

하위 문제의 최적 결과 값을 사용해 전체 문제의 최적 결과를 낼 수 있는 경우를 말한다.

만약, A - B까지의 가장 짧은 경로를 찾고자 하는 경우를 예시로 할 때, 중간에 X가 있을 때, A - X / X - B가 많은 경로 중 가장 짧은 경로라면 전체 최적 경로도 A - X - B가 정답이 된다.

![img](https://blog.kakaocdn.net/dn/dfnwTm/btqSsRROqcY/GAZup1WSsVUWsh70ohfWb0/img.png)



## 방식

### Top-Down

`dp[n]`의 값을 찾기 위해 위에서부터 호출을 시작하는 방식이다. 피보나치 수열 문제를 예로 들면:

```python
int fiboData[100] = {0,};

int fibo(int n)
{
  if (n<=2) 
    return 1;
  if (fiboData[n]==0)
    fiboData[n] = fibo(n-1) + fibo(n-2);
  return fiboData[n];
}
```

### Bottom-Up

`dp[0]`부터 시작해 `dp[n]`의 값을 찾는 방식이다.

```python
int fibo(int n)
{
  fibodata[0] = 0;
  fiboData[1] = 1;
  for (int i=2; i<=n; i++)
    fiboData[i] = fiboData[i - 1] + fiboData[i - 2];
  return fiboData[n];
}
```



## References

https://velog.io/@chelsea/1-%EB%8F%99%EC%A0%81-%EA%B3%84%ED%9A%8D%EB%B2%95Dynamic-Programming-DP ([자료구조와 알고리즘] 동적 계획법(Dynamic Programming, DP))

https://hongjw1938.tistory.com/47 (알고리즘 - Dynamic Programming(동적 계획법))