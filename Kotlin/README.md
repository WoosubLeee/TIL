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



### 종류

#### `var`

변경할 수 있는 변수.

#### `val`

읽기 전용 변수. 한 번 입력된 값은 변경할 수 없다.

#### `const`

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

#### Declaration

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

#### Getting values

```kotlin
array[index]
array.get(index)
```

#### Changing values

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



### Constructors

#### Primary constructors

```kotlin
class Person constructor(value: String) {
    // 코드
}
```

생성자에 접근 제한자나 다른 옵션이 없다면 `constructor` 키워드를 생략할 수 있다.

```kotlin
class Person(value: String) {
    
}
```

Class의 constructor가 호출되면 `init` 블록의 코드가 실행되고, `init` 블록에서는 생성자를 통해 넘어온 parameters에 접근할 수 있다.

```kotlin
class Person(value: String) {
    init {
        Log.d("class", "생성자로부터 전달받은 값은 ${value}입니다.")
    }
}
```

Parameter 앞에 변수 키워드인 `val`을 붙여주면 `init` 블록 코드 없이도 class scope 전체에서 해당 parameter를 사용할 수 있다.

```kotlin
class Person(val value: String) {
    fun process() {
        print(value)
    }
}
```

#### Secondary constructors

Secondary constructors는 `constructor` 키워드를 마치 함수처럼 class scope 안에 직접 작성할 수 있다. 그리고 `init` 블록을 작성하지 않고 `constructor` 다음에 괄호를 붙여서 코드를 작성한다.

```kotlin
class Person {
    constructor (value: String) {
        Log.d("class", "생성자로부터 전달받은 값은 ${value}입니다.")
    }
}
```

#### Default constructors

Constuctor는 작성하지 않아도 `init` 코드는 사용이 가능하다.

```kotlin
class Student {
    init {
        // 기본 생성자가 없더라도 초기화가 필요하면 여기에 코드를 작성합니다.
    }
}
```



### Class의 사용

```kotlin
var kotlin = Kotlin()
```



### 상속

상속이 되는 부모 class는 `open` 키워드로 만들어야만 한다.

```kotlin
open class 상속될 부모 클래스 {
    // 코드
}
class 자식 클래스: 부모 클래스() {
    // 코드
}

// parameter가 있다면
open class 부모 클래스(value: String)
    // 코드
}
class 자식 클래스(value: Stirng): 부모 클래스(value) {
    // 코드
}
```

부모 class에서 정의된 property와 method를 사용할 수 있다.

#### Override

Override할 때는 property나 method도 class처럼 `open`을 붙여줘야 한다.

```kotlin
open class BaseClass {
    open fun opened() {
        
    }
}
class ChildClass: BaseClass() {
    override fun opened() {
        
    }
}
```



### Extensions

이미 만들어져 있는 class에 메서드를 추가할 수 있다.

```kotlin
fun 클래스.확장할 메서드() {
    // 코드
}
```





## Object

Object를 사용하면 class를 constructor로 인스턴스화 하지 않아도 블록 안의 프로퍼티와 메서드를 호출해서 사용할 수 있다.

```kotlin
object Pig {
    var name: String = "Pinky"
    fun printName() {
        Log.d("class", "Pig의 이름은 ${name}입니다.")
    }
}
```

Object도 도트(`.`) 연산자를 그대로 사용할 수 있다.

```kotlin
Pig.name = "Mikey"
Pig.printName()
```

### Companion object

일반 class에 object 기능을 추가한다.

```kotlin
class Pig {
    companion object {
        var name: String = "None"
        fun printName() {
            Log.d("class", "Pig의 이름은 ${name}입니다.")
        }
    }
    fun walk() {
        Log.d("class", "Pig가 걸어갑니다.")
    }
}
```

`class` 로 선언했기 때문에 일반 함수인 `walk()`는 생성자인 `Pig()`를 호출, 변수에 저장한 후 사용할 수 있다.

```kotlin
// companion object
Pig.name = "Linda"
Pig.printName()

// 비 companion object
val cutePig = Pig()
cutePig.walk()
```



## Data class

간단한 값의 저장 용도.

`class` 앞에 `data` 키워드를 사용해야 하고, parameters 앞에 `var`이나 `val` 키워드는 생략할 수도 있다.

```kotlin
data class 클래스명 (파라미터1: 타입, 파라미터2: 타입)
```

```kotlin
data class UserData(val name: String, var age: Int)
var userData = UserData("Michael", 21)

userData.age = 18
```

#### `toString()`

일반 class에서는 `toString()` 메서드를 호출하면 인스턴스의 주소 값을 반환하지만, data class는 값을 반환하기 때문에 실제 값을 모니터링할 때 좋다.

```kotlin
Log.d("DataClass", "DataUser는 ${dataUser.toString()}")
// DataUser는 DataUser(name=Michael, age=21)
```

#### `copy()`

값을 복사할 수 있다.

```kotlin
var newData = dataUser.copy()
```



## 추상화

실제 구현 단계에서 코드를 작성하도록 메서드의 이름만 작성할 수도 있다.

```kotlin
abstract class Design {
    abstract fun drawText()
    abstract fun draw()
    fun showWindow() {
        // 코드
    }
}

class Implements: Design() {
    fun drawText() {
        // 구현 코드
    }
    fun draw() {
        // 구현 코드
    }
}
```



## Interface

추상화와 다르게 실행 코드가 하나도 없이 메서드 이름만 나열되어 있다.

```kotlin
interface 인터페이스명 {
    var 변수: String
    fun 메서드1()
    fun 메서드2()
}
```

```kotlin
class KotlinImpl: InterfaceKotlin {
    override var variable: String = "init value"
    override fun get() {
        // 코드 구현
    }
    override fun set() {
        // 코드 구현
    }
}
```



## Visibility modifiers

| 접근 제한자 | 제한 범위                         |
| ----------- | --------------------------------- |
| `private`   | 다른 파일에서 접근 불가능         |
| `internal`  | 같은 모듈에 있는 파일만 접근 가능 |
| `protected` | `private`과 같으나 상속 관계에서  |
| `public`    | 모든 파일에서 접근 가능           |

아무 예약어도 붙이지 않을 경우 기본적으로 `public` 접근 제한자가 적용된다.



## Generics

입력되는 값의 타입을 자유롭게 사용하기 위한 설계 도구.

```kotlin
public interface MutableList<E> {
    var list: Array<E>
    ...
}
```

`<E>`라고 되어 있는 부분에 `String`과 같은 특정 타입이 지정되면 class 내부에 선언된 모든 `E`에 `String`이 타입으로 지정된다. 결과적으로 `var list: Array<E>`가 `var list: Array<String>`으로 변경되는 것이다.

```kotlin
fun testGenerics() {
    var list: MutableList<String> = mutableListOf()
    list.add("월")
    list.add("화")
    // list.add(35) // String을 generics로 사용했기 때문에 list에는 String만 담을 수 있다.
}
```



## Null safety

`null`로 인해 프로그램이 멈출 수 있는데 Kotlin에는 이를 방지하기 위한 여러 장치가 있다.



### `?`

`null`값을 허용하기 위해서는 변수를 선언할 때 타입 뒤에 `?`를 입력한다.

```kotlin
var variable: String?
```

```kotlin
var nullable: String?
nullable = null

var notNullable: String
// notNullable = null // 일반 변수에는 null을 입력할 수 없다.
```

함수의 parameter에도 설정이 가능한데, parameter에 대해 따로 `null` 체크를 해야한다. 체크하지 않았을 경우`null`에 대해 오류가 발생할 수 있기 때문이다.

```kotlin
fun nullParameter(str: String?) {
    if (str != null) {
        var length2 = str.length  // 따로 체크하지 않았으면 오류가 발생했을 것이다.
    }
}
```

함수의 return 타입에도 설정 가능하다.

```kotlin
fun nullReturn(): String? {
    return null
}
```



### `?.`(safe call)

nullable인 변수 다음에 `?.`을 사용하면 해당 변수가 `null`일 경우 `?.` 다음의 메서드나 프로퍼티를 호출하지 않는다.

```kotlin
fun testSafeCall(str: String?): Int? {
    // str이 null이면 length를 체크하지 않고 null을 반환한다.
    var resultNull: Int? = str?.length
    return resultNull
}
```



### `?:`(Elvis operator)

변수가 `null`일 때 넘겨줄 기본값을 설정할 수 있다.

```kotlin
fun testElvis(str: String?): Int {
    // length 오른쪽에 ?:을 사용하면 null일 경우 ?: 오른쪽의 값이 반환된다.
    var resultNonNull: Int = str?.length?:0
    return resultNonNull;
}
```



## 지연 초기화

### `lateinit`

Class 안에서 변수만 nullable로 미리 선언하고 초기화는 나중에 해야 할 경우, `?`를 사용해서는 다음과 같이 할 수 있다.

```kotlin
class Person {
    var name: String? = null
    init {
        name ="Lionel"
    }
    fun process() {
        name?.plus(" Messi")
        print("이름의 길이 = ${name?.length}")
        print("이름의 첫 글자 = ${name?.substring(0, 1)}")
    }
}
```

위 같은 경우 safe call이 남용되어 가독성을 떨어뜨린다. 이때, `lateinit`을 사용하면 가독성을 높일 수 있다.

```kotlin
class Person {
    lateinit var name: String
    init {
        name = "Lionel"
    }
    fun process() {
        name.plus("Messi")
        print("이름의 길이 = ${name.length}")
        print("이름의 첫 글자 = ${name.substring(0, 1)}")
    }
}
```

#### `lateinit`의 특징

- `var`로 선언된 class의 프로퍼티에만 사용할 수 있다.
- `null`값은 허용되지 않는다.
- 기본 자료형 `Int`, `Long`, `Double`, `Float` 등은 사용할 수 없다.



### `lazy`

`lazy`는 읽기 전용 변수인 `val`을 사용하는 지연 초기화이다. `val` 변수를 먼저 선언한 후 코드 뒤쪽에 `by lazy` 키워드를 사용하고, `by lazy` 다음에 나오는 중괄호(`{}`)에 초기화할 값을 쓰면 된다.

```kotlin
class Company {
    val person: Person by lazy {
        Person()
    }
    init {
        // lazy는 선언 시에 초기화를 하기 때문에 init이 필요없다.
    }
    fun process() {
        print("person의 이름은 ${person.name}") // 이때(최초 호출 시점)에 초기화된다.
    }
}
```

#### `lazy`의 특징

- 주석에 써 있듯이 선언 시에 초기화 코드를 함께 작성하기 때문에 따로 초기화할 필요가 없다.

- 선언된 **변수**가 최초 호출되는 시점에 초기화된다.



## Scope functions

Scope functions는 코드를 축약해서 표현할 수 있도록 도와주는 함수이다. Scope functions에는 `run`, `let`, `apply`, `also`, `with`가 있다.

Scope functions는 자신을 호출한 대상을 `this` 또는 `it`으로 대체해서 사용할 수 있다.



### `this` vs `it`

#### `this`로 사용되는 scope functions: `run`, `apply`, `with`

Scope functions 안에서 호출한 대상을 `this`로 사용할 수 있습니다. Class 내부의 함수를 사용하는 것과 동일한 효과이기 때문에 `this`는 생략하고 메서드나 프로퍼티를 바로 사용할 수 있습니다.

```kotlin
var list = mutableListOf("Scope", "Function")
list.run {
    val listSize = size // this.size 대신에 this를 생략한 채로 도트 연산자(.) 없이 바로 사용 가능
    println("리스트의 길이 run = $listSize")
}
list.apply {
    val listSize = size
    println("리스트의 길이 apply = $listSize")
}
with (list) {
    val listSize = size
    println("리스트의 길이 with = $listSize")
}
```

#### `it`으로 사용되는 scope functions: `let`, `also`

호출한 대상을 `it`으로 사용할 수 있다. `it`을 생략할 수는 없지만 `target` 등 다른 이름으로 바꿀 수는 있다.

```kotlin
var list = mutableListOf("Scope", "Function")
// it을 target 등과 같이 다른 이름으로 변경 가능하다.
list.let { target ->
    val listSize = target.size
    println("리스트의 길이 let = $listSize")
}
list.also {
    val listSize = it.size
    println("리스트의 길이 also = $listSize")
}
```



### 반환값으로 구분하기

#### 호출 대상인 `this` 자체를 반환하는 scope functions: `apply`, `also`

Scope function 안에서 코드가 모두 완료된 후 자기 자신을 되돌려준다.

```kotlin
var list = mutableListOf("Scope", "Function")

var afterApply = list.apply {
    add("Apply")
    count()
}
println("반환값 apply = $afterApply") // 반환값 apply = [Scope, Function, Apply]

var afterAlso = list.also {
    it.add("Also")
    it.count()
}
println("반환값 also = $afterAlso") // 반환값 also = [Scope, Function, Apply, Also]
```

#### 마지막 실행 코드를 반환하는 scope functions: `let`, `run`, `with`

자기 자신이 아닌 scope의 마지막 코드를 반환한다.

```kotlin
var list = mutableListOf("Scope", "Function")

val lastCount = list.let {
    it.add("Run")
    it.count()
}
println("반환값 let = $lastCount") // 반환값 let = 3

val lastItem = list.run {
    add("Run")
    get(size-1)
}
println("반환값 run = $lastItem") // 반환값 run = Run

val lastItemWith = with(list) {
    add("With")
    get(size-1)
}
println("반환값 with = $lastItemWith") // 반환값 with = With
```

