# Binary search

> 이진 탐색

## What is binary search?

이진 탐색이란 데이터가 **정렬**돼 있는 배열에서 특정한 값을 찾아내는 알고리즘이다.

동작 방식은 다음과 같다.

1. 배열의 중간값을 가져온다.
2. 중간값과 검색값을 비교한다.
   1. (mid = key) 같다면 탐색을 종료한다.
   2. (mid < key) 중간값이 더 작다면 중간값 기준 오른쪽 구간을 대상으로 다시 탐색한다.
   3. (mid > key) 중간값이 더 크다면 중간값 기준 왼쪽 구간을 대상으로 다시 탐색한다.

### Pseudocode

```python
Procedure binary_search
   A ← sorted array
   n ← size of array
   x ← value to be searched

   Set lowerBound = 1
   Set upperBound = n 

   while x not found
      if upperBound < lowerBound 
         EXIT: x does not exists.
   
      set midPoint = lowerBound + ( upperBound - lowerBound ) / 2
      
      if A[midPoint] < x
         set lowerBound = midPoint + 1
         
      if A[midPoint] > x
         set upperBound = midPoint - 1 

      if A[midPoint] = x 
         EXIT: x found at location midPoint
   end while
   
end procedure
```



## References

https://cjh5414.github.io/binary-search/ (이진 탐색(Binary Search) 알고리즘 개념 이해 및 추가 예제)

https://yoongrammer.tistory.com/75 (이진 탐색 (Binary search) 개념 및 구현)

https://www.tutorialspoint.com/data_structures_algorithms/binary_search_algorithm.htm (Data Structure and Algorithms Binary Search)