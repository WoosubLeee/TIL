# Input

두 가지 방법 1. `readline`, 2. `fs`를 활용하는 방법이 제시되고 있다.



## `Readline`

The `readline` module provides an interface for reading data from a `Readable` stream (such as `process.stdin`) one line at a time.

### Events

#### `rl.close()`

Finishes the `InterfaceConstructor` instance.

```js
let count = 0;

rl.on('line', (input) => {
  console.log(`Recived : ${input}`);
  count += 1;
  if (count === 5) {
    rl.close();
  }
});
```

위 코드를 실행하게 되면 입력을 5번만 받은 후 종료하게 된다.

#### `line`

The `'line'` event is emitted whenever the `input` stream receives an end-of-line input (`\n`, `\r`, or `\r\n`). This usually occurs when the user presses Enter or Return.

```js
rl.on('line', (input) => {
  console.log(`Received: ${input}`);
});
```

### example

#### 기본적인 사용법

```js
//case 1
const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on('line', function (line) {
  console.log(line);
  rl.close();
}).on('close', function () { // rl.close()를 호출하면 콜백인 process.exit()를 호출한다.
  process.exit();
});
```

```js
// case 2
const readline = require('readline');

(async () => {
  let rl = readline.createInterface({ input: process.stdin });

  for await (const line of rl) {
    console.log('Hello Goorm! Your input is', line);
    rl.close();
  }

  process.exit();
})();
```

#### 백준

##### 여러 줄 입력(T가 없는 경우)

```
// input
4
2 3
1 0 0 1
1 1 1 1
0 1 0 1
0 1 1 1
```

```js
const solution = (N, info, data) => {
    console.log(data);
}

const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let N = null;
let info = null;
let count = 0;
const data = [];

rl.on('line', function (line) {
  if (!N) {
    // N이 null이면
    N = +line;
  } else if (!info) {
    // N이 null이 아닌데, info가 null이면
    info = line.split(' ').map((el) => +el);
  } else {
    // N과 info가 null이 아니면
    data.push(line);
    // data.push(line.split('').map((el) => +el));
    // data.push(line.split('').map((el) => el));
    // data.push(line.split(' ').map((el) => +el));
    count += 1; // data를 입력받으면 count를 증가시켜주고
  }
  if (count === N) {
    // count가 N일때 rl.close()를 호출해준다.
    rl.close();
  }
}).on('close', function () {
  // rl.close()를 호출하면 이 콜백함수로 들어오고
  solution(N, info, data); // solution을 호출 한 후
  process.exit(); // 프로세스를 종료한다.
});
```

##### 여러 줄 입력(T가 있는 경우)

```
// input
2
3
1 2 3
4 5 6
7 8 9
2
2 1
5 4
```

```js
const solution = (N, data) => {
  console.log(data);
};

const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let T = null;
let N = null;
let info = null;
let countN = 0;
let countT = 0;
let data = [];

rl.on('line', function (line) {
  if (!T) {
    T = +line;
  } else if (!N) {
    N = +line;
  } else {
    data.push(line);
    // data.push(line.split('').map((el) => +el));
    // data.push(line.split('').map((el) => el));
    // data.push(line.split(' ').map((el) => +el));
    countN += 1; // data를 입력받으면 countN을 증가시켜주고
  }
  if (countN === N) {
    // N만큼 data를 잘 입력 받았으면
    solution(N, data); // solution을 호출하고
    N = null; // T, countT를 제외한 값들을 초기화해준다.
    info = null;
    countN = 0;
    data = [];

    countT += 1; // 그리고 테스트 케이스 하나를 통과했으니 countT를 1 올려준다.
  }
  if (countT === T) {
    // 입력받은 T 만큼 테스트 케이스를 통과하게되면
    rl.close(); // rl.close()를 호출하고
  }
}).on('close', function () {
  process.exit(); // 종료한다.
});
```



## `fs`

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

https://grap3fruit.dev/blog/%EA%B5%AC%EB%A6%84(goorm),-%EB%B0%B1%EC%A4%80(BOJ)-%EC%BD%94%EB%94%A9-%ED%85%8C%EC%8A%A4%ED%8A%B8-JavaScript%EB%A1%9C-%EC%9E%85%EB%A0%A5%EB%B0%9B%EB%8A%94-%EB%B0%A9%EB%B2%95-%EC%A0%95%EB%A6%AC (구름(goorm), 백준(BOJ) 코딩 테스트 JavaScript로 입력받는 방법 정리)

https://velog.io/@yujo/node.js%ED%91%9C%EC%A4%80-%EC%9E%85%EB%A0%A5-%EB%B0%9B%EA%B8%B0 ([Node.js]표준 입력 받기(readline))

https://velog.io/@bigsaigon333/Javascript%EB%A1%9C-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%A4%80%EB%B9%84%ED%95%98%EA%B8%B01-%EC%9E%85%EC%B6%9C%EB%A0%A5 (JavaScript로 코딩테스트 준비하기(1) - 입출력)

