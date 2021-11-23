# `fs`

JS에서 입력값을 받기 위해 `fs` 모듈을 사용할 수 있다.

`fs`는 file system을 의미하는데, 이를 이용해 표준입력(stdin) 파일을 동기적으로 불러올 수 있다. 백준에서는 Node.js의 입출력에 대하여 아래와 같은 예시를 제공하고 있다.

```js
// fs 모듈을 불러온다
var fs = require('fs');
// 백준의 input 파일 경로는 '/dev/stdin'이다
// 띄어쓰기(' ')로 구분된 단어를 가지는 배열을 반환
// 인코딩을 명시적으로 넘기지 않은 경우에는 raw Buffer가 반환되므로
// toString() 함수를 호출하여 string으로 변환하여야 한다
var input = fs.readFileSync('/dev/stdin').toString().split(' ');

// options으로 인코딩을 string 자료형으로 넘기는 경우, string을 반환한다.
var input2 = fs.readFileSync(0, "utf8").split("\n");

var a = parseInt(input[0]);
var b = parseInt(input[1]);
console.log(a+b);
```



## References

https://velog.io/@bigsaigon333/Javascript%EB%A1%9C-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%A4%80%EB%B9%84%ED%95%98%EA%B8%B01-%EC%9E%85%EC%B6%9C%EB%A0%A5 (JavaScript로 코딩테스트 준비하기(1) - 입출력)

