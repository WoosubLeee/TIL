# LCS

## Subsequence vs Substring

LCS는 주로 **최장 공통 부분수열(Longest Common Subsequence)**을 말하지만, **최장 공통 문자열(Longest Common Substring)**을 말하기도 한다. 차이점을 살펴보면:

![img](https://media.vlpt.us/images/emplam27/post/14e1f11d-d3de-4dd3-8f41-3e7f9697770f/%EB%91%98%20%EC%B0%A8%EC%9D%B4.png)



## Longest Common Subsequence

### 점화식

```python
for i in range(len(string_A)):
    for j in range(len(string_B)):
        if i == 0 or j == 0:  # 마진 설정
            LCS[i][j] = 0
        elif string_A[i] == string_B[j]:
            LCS[i][j] = LCS[i - 1][j - 1] + 1
        else:
            LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])
```

1. 문자열A, 문자열B의 **한글자씩** 비교해본다.

2. 두 문자가 **같다면 `LCS[i - 1][j - 1]` 값을 찾아 `+1`** 한다.

   ![img](https://media.vlpt.us/images/emplam27/post/b36ca562-0a49-4aec-8072-ca4d65fa8e87/%EA%B3%BC%EC%A0%951-1.png)

   위 문제를 예로 들면, 그림의 초록색 부분인 문자열 **GBC** 와 **AB**를 비교하는 과정이다. `string_A[i]`인 **C**와 `string_B[j]`인 **B**가 서로 다르므로,

   **GBC**와 **A**의 LCS, **GB**와 **AB**의 LCS 중 최댓값이 **GBC**와 **AB**의 LCS가 된다.

   ![img](https://media.vlpt.us/images/emplam27/post/f44bccfc-9da2-4da1-80a0-c3ae9c1e9cbe/%EA%B3%BC%EC%A0%951.png)

3. 두 문자가 **다르다면 `LCS[i - 1][j]`와 `LCS[i][j - 1]` 중에 큰값을 표시**한다.

   ![img](https://media.vlpt.us/images/emplam27/post/d1f4ac83-a0a0-4daa-809b-3eb6b600565c/%EA%B3%BC%EC%A0%952-1.png)

   그림의 초록색 부분 중 숫자 2가 적힌 부분인 문자열 **GBC**와 **ABC**를 비교하는 과정이다. `string_A[i]`인 **C**와 `string_B[j]`인 **C**가 서로 같으므로,

   **GB**와 **AB**의 LCS에 문자열 **C**를 추가한 것이 새 LCS가 된다.

   ![img](https://media.vlpt.us/images/emplam27/post/b03df3d9-0cd0-4511-9d30-ac669f996dc5/%EA%B3%BC%EC%A0%952-2.png)

4. 위 과정을 반복.

5. 결과

   ![image-20220206154723916](README.assets/image-20220206154723916.png)



## References

https://velog.io/@emplam27/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-LCS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Longest-Common-Substring%EC%99%80-Longest-Common-Subsequence ([알고리즘] 그림으로 알아보는 LCS 알고리즘 - Longest Common Substring와 Longest Common Subsequence)

