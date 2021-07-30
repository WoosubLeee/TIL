# callback

## What is callback function?

매개변수로 넘겨받은 함수는 일단 넘겨받고, 때가 되면 나중에 호출(callback)한다는 것이 callback function의 개념이다.

```js
function checkGang(count, link, good) {
  count < 3 ? link() : good();
}

function linkGang() {
  console.log('1일 3깡은 기본입니다. 아래 링크를 통해 깡을 시청해주세요');
  console.log('https://youtu.be/xqFvYsy4wE4');
}

function goodGang() {
  console.log('오늘 할당량은 모두 채우셨습니다! :)')
}

checkGang(2, linkGang, goodGang);
```

checkGang 함수가 먼저 호출되고, 매개변수로 들어온 count의 값에 따라
linkGang과 goodGang 함수 둘 중 한 가지가 나중에 호출된다.



#### 좀 더 간단하게?

passed as an argument to another function(다른 함수의 인자로써 이용되는 함수)

callback function의 정확한 의미는 아니지만 위와 같은 의미로 쓰더라도 대체로 적용된다.

```js
//hello!
function printHello() {
  print('hello');
}
//bye!
function printBye() {
  print('bye');
}

//특정 함수를 매개변수로 받아서 3초 뒤에 실행하는 함수
function sleepAndExecute(sleepTimeSecond, callback) {
  //sleepTimeSecond 초 만큼 대기
  sleep(sleepTimeSecond);
  //전달된 callback 실행
  callback();
}

//3초 뒤에 hello 출력하기
sleepAndExecute(3, printHello);

//5초 뒤에 bye 출력하기
sleepAndExecute(5, printBye);
```



## Why use callback function?

콜백 함수의 동작 방식은 일종의 식당 자리 예약과 같다. 식당에 자리가 없을 경우, 대기자 명단에 이름을 쓴 다음에 자리가 날 때까지 주변 식당을 돌아다닌다. 만약 식당에서 자리가 생기면 전화로 자리가 났다고 연락이 온다. 그 전화를 받는 시점은 콜백 함수가 호출되는 시점과 같다고 볼 수 있다. 손님 입장에서는 자리가 날 때까지 식당에서 기다리지 않고 근처 가게에서 잠깐 쇼핑을 할 수도 있고 아니면 다른 식당 자리를 알아볼 수도 있다.

자리가 났을 때만 연락이 오기 때문에 미리 가서 기다릴 필요도 없고, 직접 식당 안에 들어가서 자리가 비어 있는지 확인할 필요도 없다. 자리가 준비된 시점, 즉 **데이터가 준비된 시점에서만 사용자가 원하는 동작(자리에 앉는다, 특정 값을 출력한다 등)을 수행**할 수 있다.

ajax 통신을 사용한 코드로 예시를 들어보자.

```js
function getData() {
	var tableData;
	$.get('https://domain.com/products/1', function (response) {
		tableData = response;
	});
	return tableData;
}

console.log(getData()); // undefined
```

**undefined가 출력된 이유** : `$.get()`로 데이터를 요청하고 받아올 때까지 기다려주지 않고 다음 코드인 `return tableData;`를 실행했기 때문이다.

**callback function을 이용한 해결**

```js
function getData(callbackFunc) {
	$.get('https://domain.com/products/1', function (response) {
		callbackFunc(response); // 서버에서 받은 데이터 response를 callbackFunc() 함수에 넘겨줌
	});
}

getData(function (tableData) {
	console.log(tableData); // $.get()의 response 값이 tableData에 전달됨
});
```

위와 같이 callback function을 사용하게 되면 특정 로직이 끝났을 때 원하는 함수를 실행시킬 수 있다.

## 참고자료

https://velog.io/@surim014/JavaScript-callback-%EC%BD%9C%EB%B0%B1%EC%97%90-%EB%8C%80%ED%95%B4-%EC%95%8C%EC%95%84%EB%B3%B4%EC%9E%90 (JavaScript - callback (콜백)에 대해 알아보자)