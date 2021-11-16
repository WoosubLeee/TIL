# sort

- `sort()`
- `sorted()`
- `sortBy()`
- `sortedBy()`
- `sortWith()`
- `sortedWith()`

For descending order:

- add `Descending()` : `sort`, `sorted`, `sortBy`, `sortedBy`
- add `reverse()` or `reversed()` : `sortWith`, `sortedWith`

**Immutable lists can only use `sorted` type methods.**

### `sort()`

 Sorts a mutable list.

```kotlin
val nums = mutableListOf(3, 1, 7, 2, 8, 6)
	
nums.sort()
// nums: [1, 2, 3, 6, 7, 8]

nums.sortDescending();
// nums: [8, 7, 6, 3, 2, 1]
```

### `sorted()`

Returns another sorted list.

```kotlin
val nums = mutableListOf(3, 1, 7, 2, 8, 6)

val sortedNums = nums.sorted()
// nums: [3, 1, 7, 2, 8, 6]
// sortedNums: [1, 2, 3, 6, 7, 8]

val sortedNumsDescending = nums.sortedDescending()
// sortedNumsDescending: [8, 7, 6, 3, 2, 1]
```

### `sortBy()`

Sort a mutable list by a specific field. We need to pass a selector function as an argument.

```kotlin
val myDates = mutableListOf(
	MyDate(4, 3),
	MyDate(5, 16),
	MyDate(1, 29)
)

myDates.sortBy { it.month }
myDates.forEach { println(it) }
/*
MyDate(month=1, day=29)
MyDate(month=4, day=3)
MyDate(month=5, day=16)
*/

myDates.sortByDescending { it.month }
myDates.forEach { println(it) }
/*
MyDate(month=5, day=16)
MyDate(month=4, day=3)
MyDate(month=1, day=29)
*/
```

### `sortedBy()`

Returns a list by a specific field.

```kotlin
val myDates = mutableListOf(
	MyDate(4, 3),
	MyDate(5, 16),
	MyDate(1, 29)
)

val sortedDates = myDates.sortedBy { it.month }
val sortedDatesDescending = myDates.sortedByDescending { it.month }
myDates.forEach { println(it) }
/*
MyDate(month=4, day=3)
MyDate(month=5, day=16)
MyDate(month=1, day=29)
*/
sortedDates.forEach { println(it) }
/*
MyDate(month=1, day=29)
MyDate(month=4, day=3)
MyDate(month=5, day=16)
*/
sortedDatesDescending.forEach { println(it) }
/*
MyDate(month=5, day=16)
MyDate(month=4, day=3)
MyDate(month=1, day=29)
*/
```

### `sortWith()`

`Comparator`를 parameter로 받아 여러 가지 조건을 섞어 정렬할 수 있다.

```kotlin
val myDates = mutableListOf(
	MyDate(8, 19),
	MyDate(5, 16),
	MyDate(1, 29),
	MyDate(5, 10),
	MyDate(8, 3)
)

myDates.sortWith(compareBy({it.month}, {it.day})
myDates.forEach { println(it) }
/*
MyDate(month=1, day=29)
MyDate(month=5, day=10)
MyDate(month=5, day=16)
MyDate(month=8, day=3)
MyDate(month=8, day=19)
*/
val sortedDatesDescending = myDates.reverse()
sortedDatesDescending.forEach { println(it) }
/*
MyDate(month=8, day=19)
MyDate(month=8, day=3)
MyDate(month=5, day=16)
MyDate(month=5, day=10)
MyDate(month=1, day=29)
*/
```

### `sortedWith()`

```kotlin
val sortedDates = myDates.sortedWith(compareBy { it.month }.thenBy { it.day })
val sortedDatesDescending = myDates.sortedWith(compareBy { it.month }.thenBy { it.day }).reversed()
myDates.forEach { println(it) }
/*
MyDate(month=8, day=19)
MyDate(month=5, day=16)
MyDate(month=1, day=29)
MyDate(month=5, day=10)
MyDate(month=8, day=3)
*/
sortedDates.forEach { println(it) }
/*
MyDate(month=1, day=29)
MyDate(month=5, day=10)
MyDate(month=5, day=16)
MyDate(month=8, day=3)
MyDate(month=8, day=19)
*/
sortedDatesDescending.forEach { println(it) }
/*
MyDate(month=8, day=19)
MyDate(month=8, day=3)
MyDate(month=5, day=16)
MyDate(month=5, day=10)
MyDate(month=1, day=29)
*/
```



## References

https://www.bezkoder.com/kotlin-sort-list/ (Kotlin List sort, sorted, sortBy, sortedBy, sortWith, sortedWith example)

