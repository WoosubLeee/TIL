# input, output(Kotlin)

## `BufferedReader`, `BufferedWriter`

```kotlin
import java.io.BufferedReader
import java.io.BufferedWriter
import java.io.InputStreamReader
import java.io.OutputStreamWriter
import java.util.StringTokenizer

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val bw = BufferedWriter(OutputStreamWriter(System.out))
    // 테스트 케이스의 개수를 받고, 그 수만큼 반복문 실행한다.
    repeat(br.readLine().toInt()) {
        // StringTokenizer를 활용해 정수 두 개를 입력받고 더하여 sum에 저장한다.
        val token = StringTokenizer(br.readLine())
        val sum = (token.nextToken().toInt() + token.nextToken().toInt()).toString()
        // Output buffer에 올려놓는다(출력하는 것이 아닌 buffer에만 올려놓는 것이다)
        bw.write(sum + "\n")
    }
    // flush()를 통해 출력한다
    bw.flush()
    // buffer 사용 후에는 꼭 close() 해준다.
    bw.close()
}
```

다음과 같이 축약해서 사용할 수도 있다. Scope function인 `with`를 활용한다.

```kotlin
import java.util.StringTokenizer

fun main() = with(System.`in`.bufferedReader()) {
    repeat(readLine().toInt()) {
        val token = StringTokenizer(readLine())
        val sum = (token.nextToken().toInt() + token.nextToken().toInt()).toString()
        print(sum)
    }
}
```



## References

https://meoru-tech.tistory.com/57 (💡 [Kotlin] 빠른 입출력(I/O) - BufferedReader, BufferedWriter (예제 : BOJ 15552))