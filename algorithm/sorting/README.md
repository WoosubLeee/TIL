# Sorting algorithm

## O(n²)의 시간복잡도

### Bubble sort(버블 정렬)

![img](https://images.velog.io/images/jguuun/post/d02f445e-1936-4333-a703-642c0431db03/Bubble-sort.gif)

![Category:Bubble sort - Wikimedia Commons](https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Sorting_bubblesort_anim.gif/250px-Sorting_bubblesort_anim.gif)

인접한 두 수를 비교하며 정렬해나가는 방법이다. 오름차순으로 정렬하고자 할 경우, 비교시마다 큰 값이 뒤로 이동하여, 한 바퀴 돌 시 가장 큰 값이 맨 뒤에 저장된다.

#### ex)

```python
def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
```

### Selection sort(선택 정렬)

![img](https://images.velog.io/images/jguuun/post/f95f96d8-de50-4f49-b4ae-cea5b07365ce/Selection-Sort-Gif.gif)



한 번 순회를 하면서 가장 작은(or 가장 큰) 값을 찾아 교환해주는 방법

#### ex)

```python
def selection_sort(array):
	n = len(array)
	for i in range(n):
		min_index = i
		for j in range(i + 1, n):
			if array[j] < array[min_index]:
				min_index = j
		array[i], array[min_index] =  array[min_index], array[i]
```

### Insertion sort(삽입 정렬)

![img](https://images.velog.io/images/jguuun/post/fa49ded1-64c6-42fb-813e-947fe3d4b35d/Insertion-sort-example-300px.gif)

정렬된 데이터 그룹을 늘려가며 추가되는 데이터는 알맞은 자리에 삽입하는 방식.

#### ex)

```python
def insertion_sort(array):
	n = len(array)
	for i in range(1, n):
		for j in range(i, 0, - 1):
			if array[j - 1] > array[j]:
				array[j - 1], array[j] = array[j], array[j - 1]
```



## O(n log n)의 시간복잡도

### Merge sort(병합 정렬)

![img](https://images.velog.io/images/jguuun/post/8f6ff9f4-52e7-43df-9664-880830d2f239/Merge-sort-example-300px.gif)

분할 정복과 재귀를 이용한 알고리즘. 반으로 쪼개고 다시 합치는 과정에서 그룹을 만들어 정렬한다.

#### ex)

```python
def merge_sort(array):
	if len(array) <= 1:
		return array
    
	mid = len(array) // 2
	low_arr = merge_sort(array[:mid])
	high_arr = merge_sort(array[mid:])

	merged_arr = []
	l = h = 0
	while l < len(low_arr) and h < len(high_arr):
		if low_arr[l] < high_arr[h]:
			merged_arr.append(low_arr[l])
			l += 1
		else:
			merged_arr.append(high_arr[h])
			h += 1
	merged_arr += low_arr[l:]
	merged_arr += high_arr[h:]
	print(merged_arr)
	return merged_arr
```

### Quick sort(퀵 정렬)

![img](https://images.velog.io/images/jguuun/post/91ff10f7-4b7a-4b26-916f-30d38138b03e/Quicksort-example.gif)

병합 정렬은 균등하게 분할하였다면 퀵 정렬은 Pivot을 설정하고 그 기준으로 정렬을 한다. pivot point를 기준으로 작은 값은 왼쪽, 큰 값은 오른쪽으로 옮기는 방식으로 정렬을 진행한다.

- 다른 정렬 알고리즘보다 빠르며 많은 언어의 정렬 내장 함수로 퀵 정렬을 수행한다.

#### ex)

```python
def quick_sort(array):
	if len(array) <= 1:
		return array
    
	pivot = len(array) // 2
	front_arr, pivot_arr, back_arr = [], [], []
	for value in array:
		if value < array[pivot]:
			front_arr.append(value)
		elif value > array[pivot]:
			back_arr.append(value)
		else:
			pivot_arr.append(value)
	print(front_arr, pivot_arr, back_arr)
	return quick_sort(front_arr) + quick_sort(pivot_arr) + quick_sort(back_arr)
```

### Heap sort(힙 정렬)

![File:Heap sort example.gif - Wikimedia Commons](https://upload.wikimedia.org/wikipedia/commons/f/fe/Heap_sort_example.gif)

#### Heap

완전 이진 트리의 일종으로 우선순위 큐를 위하여 만들어진 자료구조. 최댓값, 최솟값을 쉽게 추출할 수 있는 자료구조.

#### 정렬 방법

최대 heap tree나, 최소 heap tree를 구성해 정렬하는 방법.

- 내림차순 기준
  1. n개의 요소들로 최대 heap을 만든다.
  2. 하나씩 요소(최대값 = 루트 노드)를 heap에서 꺼내서 배열의 뒤부터 저장한다.

#### ex)

```python
def heapify(unsorted, index, heap_size):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index
    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index
    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)
        
def heap_sort(unsorted):
    n = len(unsorted)
    # BUILD-MAX-HEAP (A) : 위의 1단계
    # 인덱스 : (n을 2로 나눈 몫-1)~0
    # 최초 힙 구성시 배열의 중간부터 시작하면 
    # 이진트리 성질에 의해 모든 요소값을 
    # 서로 한번씩 비교할 수 있게 됨 : O(n)
    for i in range(n // 2 - 1, -1, -1):
        heapify(unsorted, i, n)
    # Recurrent (B) : 2~4단계
    # 한번 힙이 구성되면 개별 노드는
    # 최악의 경우에도 트리의 높이(logn)
    # 만큼의 자리 이동을 하게 됨
    # 이런 노드들이 n개 있으므로 : O(nlogn)
    for i in range(n - 1, 0, -1):
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        heapify(unsorted, 0, i)
    return unsorted
```



## References

https://velog.io/@jguuun/%EC%A0%95%EB%A0%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98 (정렬 알고리즘 종류와 설명(파이썬 예제))

https://hsp1116.tistory.com/33

https://gmlwjd9405.github.io/2018/05/10/algorithm-heap-sort.html ([알고리즘] 힙 정렬(heap sort)이란)

