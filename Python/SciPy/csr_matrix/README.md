# csr_matrix

Compressed Sparse Row Matrix
희소행렬을 효율적으로 저장하는 방법.



## 희소행렬(sparse matrix)

행렬의 값이 대부분 '0'인 행렬을 희소행렬이라 한다.

cf. 밀집행렬(dense matrix)



## 변환 방법

```python
import numpy as np
from scipy.sparse import csr_matrix


arr = np.array([[0, 1, 0, 2], 
                [0, 3, 4, 5], 
                [0, 0, 0, 0], 
                [6, 0, 0, 7], 
                [0, 8, 0, 0]])

csr_mat = csr_matrix(arr)

print(csr_mat)
'''
(0, 1)        1
(0, 3)        2
(1, 1)        3
(1, 2)        4
(1, 3)        5
(3, 0)        6
(3, 3)        7
(4, 1)        8
'''
```



## Attributes

- `indptr` : 행렬의 '0'이 아닌 원소의 행의 시작 위치
- `indices` : 행렬의 '0'이 아닌 원소의 열의 위치
- `data` : 행렬의 '0'이 아닌 원소 값

![img](https://t1.daumcdn.net/cfile/tistory/99C845445F69BC8A32)

`indptr`의 경우

첫번째 행 [0, a, 0, b]는 '0'이 아닌 원소의 배열의 0 위치에서 시작.
두번째 행 [0, c, d, e]는 2 위치에서 시작.
세번째 행 [0, 0, 0, 0]는 5 위치에서 시작.
네번째 행 [f, 0, 0, g]는 5 위치에서 시작(세번째 행에 0밖에 없으므로).
다섯번째 행 [0, h, 0, 0]는 7 위치에서 시작.
마지막으로 원소의 개수 8에서 끝난다.



## References

https://rfriend.tistory.com/551 ([Python] Numpy 희소행렬을 SciPy 압축 희소 열 행렬 (Compressed sparse row matrix)로 변환하기)

