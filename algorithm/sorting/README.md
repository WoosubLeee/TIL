# Sorting algorithm

## O(n+k)의 시간복잡도

### Counting sort(카운팅 정렬)

![Counting Sort GIF - Counting Sort - Discover &amp; Share GIFs](https://c.tenor.com/zswbYsLbYqEAAAAd/counting-sort.gif)

항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여, 선형 시간에 정렬하는 효율적인 알고리즘.

#### 제한 사항

- 정수나 정수로 표현할 수 있는 자료에 대해서만 적용 가능
- 집합 내의 가장 큰 정수를 알아야 한다.

#### 시간복잡도

O(n+k) : n은 집합 길이, k는 정수의 최댓값

#### ex)

```python
def counting_sort(array):
    max_num = max(array)
    counting_array = [0] * (max_num + 1)

    for i in array:
        counting_array[i] += 1
    
    # 등장 횟수를 누적합으로 바꿔준다.
    for i in range(max_num):
        counting_array[i + 1] += counting_array[i]

    # output array 생성
    output_array = [-1] * len(array)

    # output array에 정렬하기(counting array를 참조)
    for i in array:
        output_array[counting_array[i] - 1] = i
        counting_array[i] -= 1
    return output_array
```



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
def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    
    pivot = start # 피벗은 첫 번째 원소
    left, right = start+1, end
    
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복 
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
            
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
           
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)
```

### Heap sort(힙 정렬)

![File:Heap sort example.gif - Wikimedia Commons](https://upload.wikimedia.org/wikipedia/commons/f/fe/Heap_sort_example.gif)

#### Heap

완전 이진 트리의 일종으로 우선순위 큐를 위하여 만들어진 자료구조. 최댓값, 최솟값을 쉽게 추출할 수 있는 자료구조.

#### 정렬 방법

최대 heap tree나, 최소 heap tree를 구성해 정렬하는 방법.

- 오름차순 기준
  1. n개의 요소들로 최대 heap을 만든다.
  2. 하나씩 요소(최대값 = 루트 노드)를 heap에서 꺼내서 배열의 뒤부터 저장한다.

#### ex)

```python
def heapify(unsorted, index, heap_size):
    largest = index
    left_index = 2 * index
    right_index = 2 * index + 1
    if left_index <= heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index
    if right_index <= heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index
    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)
        
def heap_sort(unsorted):
    n = len(unsorted)
    
    # max heap 생성
    for i in range(n - 1, 0, -1):
        heapify(unsorted, i, n-1)
        
    for i in range(n - 1, 0, -1):
        unsorted[1], unsorted[i] = unsorted[i], unsorted[1]
        heapify(unsorted, 1, i-1)
    return unsorted
```



## References

https://velog.io/@jguuun/%EC%A0%95%EB%A0%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98 (정렬 알고리즘 종류와 설명(파이썬 예제))

https://hsp1116.tistory.com/33

https://gmlwjd9405.github.io/2018/05/10/algorithm-heap-sort.html ([알고리즘] 힙 정렬(heap sort)이란)

