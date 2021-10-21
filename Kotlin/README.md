# Kotlin

## Variables

### 선언 방법

#### 1. 변수 선언과 동시에 값 넣기

```kotlin
var myName = "홍길동"
val hisName = "길동홍"
```

입력되는 값으로 타입(문자, 숫자, boolean 등)을 추론한다.

#### 2. 값으로 초기화하지 않고 선언만 하고 사용하기

선언만 할 경우에는 반드시 먼저 변수명 옆에 콜론(`:`) 구분자를 붙여서 타입을 지정해야 한다.

```kotlin
var myAge: Int
myAge = 27
val herAge: Int
herAge = 38
```

### `var`

변경할 수 있는 변수.

### `val`

읽기 전용 변수. 한 번 입력된 값은 변경할 수 없다.

### `const`

상수. `val`과 같이 읽기 전용인 것은 동일하지만, 컴파일 시에 값이 결정되기 때문에 Int, Long과 같은 기본형과 문자열인 String만 입력할 수 있다.



## Data types

| 구분   | 데이터 타입 | 설명                   | 값의 범위 및 예                   |
| ------ | ----------- | ---------------------- | --------------------------------- |
| 숫자형 | Double      | 64비트 실수            |                                   |
| ''     | Float       | 32비트 실수            |                                   |
| "      | Long        | 64비트 정수            | -2E63 ~ 2E63-1                    |
| "      | Int         | 32비트 정수            | -2147483648 ~ 2147483647          |
| "      | Short       | 16비트 정수            | -32.768 ~ 32.767                  |
| "      | Byte        | 8비트 정수             | -128 ~ 127                        |
| 문자형 | Char        | 1개의 문자             | '글'(외따옴표)                    |
| "      | String      | 여러 개의 문자         | "여러 개의 글자입니다."(쌍따옴표) |
| 불린형 | Boolean     | true, false 두 가지 값 | true 또는 false                   |

- 숫자형 :  가독성을 높이기 위해서 언더바(`_`)로 자릿수를 구분해줄 수 있습니다. 다만, 언더바는 개발자가 읽기 쉽게 하기 위한 것으로 컴퓨터는 앞의 값과 동일하게 인식합니다.
  - Double : 소수점이 있는 값

  - Float : Double과 동일한 용도이지만 더 작은 범위. Android Studio는 Double과 구분하기 위해 숫자 끝에 `F`를  붙여줍니다.

    ```kotlin
    var floatValue: Float
    floatValue = 3.141592F
    ```

  - Int : 정수값.

    ```kotlin
    var intValue: Int
    intValue = 2_147_483_647
    ```

  - Long : Int보다 큰 범위의 정수값. Int와 구분하기 위해 숫자 끝에 `L`을 붙여줍니다.

    ```kotlin
    var longValue: Long
    longValue = 2147483647L
    ```

- 문자형

  - Char : 하나의 글자. 외따옴표(`''`)로 감싸서 저장할 수 있다.

    ```kotlin
    var charValue = 'A'
    ```



### 문자형

#### 문자열 템플릿

문자열 내부에서 달러(`$` or `${변수}`) 기호를 넣으면 해당 영역이 문자가 아닌 코드라는 것을 알려줍니다.

```kotlin
var name = "홍길동"
Log.d("BasicSyntax", "제 이름은 $name 입니다.")  // 제 이름은 홍길동 입니다.
Log.d("BasicSyntax", "제 이름은 ${name} 입니다.")
```

추가적인 연산식이 필요한 경우에는 `${코드 블록}` 안에 수식을 입력하는 형태로 사용할 수 있다.

```kotlin
var score = 98
"제 점수는 ${score + 1}점입니다."  // 제 점수는 99점입니다.
```



## Array

### Declaration

Array 객체는 Int, Long, Char 등과 같은 기본 타입 뒤에 `Array`를 붙여서 만든다.

```kotlin
var students = Array(10)
var longArray = LongArray(10)
var charArray = CharArray(10)
var floatArray = FloatArray(10)
var doubleArray = DoubleArray(10)
```

String은 기본 타입이 아니기 때문에 `StringArray`는 없지만 다음과 같이 사용할 수 있다.

```kotlin
var stringArray = Array(10, {item->""})
```

`arrayOf` 함수를 사용해서 값을 직접 할당할 수도 있다.

```kotlin
var numArray = intArrayOf(1, 2, 3, 4)
var dayArray = arrayOf("MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN")
```

### Getting values

```kotlin
array[index]
array.get(index)
```

### Changing values

```kotlin
array[index] = value
array.set(index, value)
```



## Collection

Array와는 다르게 크기를 고정하지 않는다. 크게 세 가지로 List, Map, Set이 있다. Kotlin에서 동적으로 collection를 사용하기 위해서는 mutable이라는 접두어가 붙는다. 접두어가 없는 collection도 있지만 잘 사용하지 않기 때문에 항상 `mutableList`, `mutableMap`, `mutableSet`을 사용한다고 생각해도 된다.

### List

List는 저장되는 데이터에 인덱스를 부여한 collection이며 중복된 값을 입력할 수 있다.

#### Declaration

```kotlin
var mutableList = mutableListOf("MON", "TUE", "WED")
```

##### Generic

```kotlin
var 변수명 = mutableListOf<타입>()
var stringList = mutableListOf<Stirng>()
```

#### Adding values

```kotlin
mutableList.add("THU")
```

#### Getting values

```kotlin
var variable = mutableList.get(1)
```

#### Adjusting values

```kotlin
mutableList.set(1, "수정할 값")
```

#### Deleting values

```kotlin
mutableList.removeAt(1)
```

#### Getting size

```kotlin
mutableList.size
```



### Set

중복을 허용하지 않는 list. 인덱스로 조회 불가.

#### Declaration

```kotlin
var set = mutableSetOf("MON", "TUE", "WED")
var set1 = mutableSetOf<String>()
```

#### Adding values

```kotlin
set.add("JAN")
set.add("FEB")
set.add("JAN")  // 동일한 값은 입력되지 않는다
```

#### Getting values

Set은 인덱스로 조회하는 함수가 없기 때문에 특정 위치의 값을 직접 사용할 수 없다. 다음은 set에 있는 모든 값을 log에 출력하는 코드이다.

```kotlin
Log.d("Collection", "Set 전체 출력 = ${set}")
```

#### Deleting values

```kotlin
set.remove("FEB")
```



### Map

#### Declaration

Map은 key와 value의 쌍으로 입력되는 collection이다. Map의 key는 list의 index와 비슷한데 map에서는 직접 key를 입력해야 한다.

```kotlin
var map = mutableMapOf("키1" to "값1", "키2" to "값2")
var map1 = mutableMapOf<String, String>()
```

#### Adding values

```kotlin
map.put("키3", "값3")
```

#### Getting values

```kotlin
var val1 = map.get("키1")
```

#### Adjusting values

```kotlin
map.put("키1", "수정")
```

#### Deleting values

```kotlin
map.remove("키1")
```



### Immutable collection

크기와 값 모두를 변경할 수 없는 collection이다. Immutable collection은 기존 collection에서 `mutable`이라는 접두어가 제거된 형태로 사용된다.

```kotlin
val DAY_LIST = listOf("월", "화", "수", "목", "금", "토", "일")
```

Immutable collection을 저장할 때는 val로 선언하고 변수명을 대문자로 표시하는 게 좋다.



## 조건문

### `if` 문

#### 변수에 직접 `if` 문 사용하기

`if` 문의 조건식 결과를 변수에 대입할 수 있습니다. 코드 영역이 여러 줄일 경우 마지막 줄을 변수값으로 사용할 수 있다.

```kotlin
var a = 5
var b = 3
var bigger = if (a > b) a else b

var bigger2 = if (a > b) {
    var c = 30
    a  // 마지막 줄의 a 값이 변수 bigger2에 저장됩니다.
} else {
    b
}
```

### `when` 문

다른 언어의 `switch` 문과 비슷하다. 하지만 Kotlin의 `when` 문은 다른 언어와는 다르게 같은 값뿐만 아니라 범위 값도 처리할 수 있고 사용 방법도 더 많다.

```kotlin
when (parameter) {
    비교값1 -> {
        // statement
    }
    비교값2 -> {
        // statement
    }
    else -> {
        // statement
    }
}
```

여러 값을 한 번에 비교하려면 콤마(`,`)로 구분하면 된다.

```kotlin
var now = 9
when (now) {
    8, 9 -> {
        Log.d("when", "현재 시간은 8시 또는 9시입니다.")
    }
}
```

`in`을 이용해 범위값을 비교할 수도 있다.

```kotlin
var ageOfMichael = 19
when (ageOfMichael) {
    in 10..19 -> {
        Log.d("when", "마이클은 10대입니다.")
    }
    !in 10..19 -> {
        Log.d("when", "마이클은 10대가 아닙니다.")
    }
    else -> {
        Log.d("when", "마이클의 나이를 알 수 없습니다.")
    }
}
```

parameter를 생략할 수도 있다.

```kotlin
var currentTime = 6
when {
    currentTime == 5 -> {
        Log.d("when", "현재 시간은 5시입니다.")
    }
    currentTime > 5 -> {
        Log.d("when", "현재 시간은 5시가 넘었습니다.")
    }
    else -> {
        Log.d("when", "현재 시간은 5시 이전입니다.")
    }
}
```



## 연산자

### 비교 연산자



### 논리 연산자

| 연산자 | 의미             |
| ------ | ---------------- |
| `&&`   | 논리곱           |
| `||`   | 논리합           |
| `!`    | 부정 단항 연산자 |



## 반복문

### `for` 문

```kotlin
for (반복할 범위) {
    // 실행 코드
}

for (변수 in 시작값..종료값) {
    // 실행 코드
}

for (index in 1..10) {
    Log.d("For", "현재 숫자는 ${index}")
}
```

#### `until`

마지막 숫자 제외하기. `..` 대신에 `until`을 사용하면 종료값 이전까지만 반복한다.

```kotlin
for (변수 in 시작값 until 종료값) {
    // 실행 코드
}
```

#### `step`

`for`문의 블록을 `step` 수만큼 건너뛰면서 실행한다.

```kotlin
for (num in 1..10 step 3) {
    Log.d("For", "${num}")  // 1, 4, 7, 10
}
```

#### `downTo`

큰 수에서 작은 수로 감소시키면서 실행할 수 있다. `step`도 사용 가능하다.

```kotlin
for (index in 10 downTo 0) {
    Log.d("For", "현재 숫자는 ${index}")
}
```

#### Array, Collection 내 elements 반복하기

```kotlin
var arrayMonth = arrayOf("JAN", "FEB", "MAR", "APR", "MAY", "JUN")
for (month in arrayMonth) {
    Log.d("for", "현재 월은 ${month}입니다.")
}
```



### `while` 문

```kotlin
while (조건식) {
    // 실행 코드
}
```

#### `do`

`do` 블록 안의 코드를 한 번 실행한 후 `while` 문이 실행됩니다.

```kotlin
var game = 1
val match = 6
do {
    Log.d("while", "${game}게임 이겼습니다. 우승까지 ${match-game}게임 남았습니다.")
    game += 1
} while (game < match)
```



### 반복문 제어

#### `break`

#### `continue`



## 함수

```kotlin
fun 함수명(parameter 이름: 타입): 반환 타입 {
    // 실행 코드
}

fun square(x: Int, y: Int): Int {
    return x * y
}
```

Parameter를 정의할 때 등호(`=`)를 사용해서 기본값을 설정할 수 있다.

```kotlin
fun 함수명(name1: String, name2: Int = 157, name3: Double) {
    // 실행 코드
}
```



## Class

```kotlin
class 클래스명 {
    var 변수
    fun 함수() {
        // 코드
    }
}
```

