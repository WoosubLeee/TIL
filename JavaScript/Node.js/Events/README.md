# Events

Node.js는 event 기반 비동기 방식의 서버프레임워크이다. Node.js에서는 기본적으로 아래의 세 가지 함수와 객체를 이용해서 event 처리를 하게된다.

- `EventEmitter` : Node.js의 모든 event 처리가 정의된 기본객체이다. event를 사용하기 위해서는 이 객체를 재정의해서 사용할 수 있다.
- `on()` : event를 연결하는 메소드다.
- `emit()` : event를 발생시킨다.



## event를 가진 객체 만들기

```js
// 1. 이벤트가 정의되어있는 events 모듈 생성
var EventEmitter = require('events');

// 2. 생성된 이벤트 모듈을 사용하기 위해 custom_object로 초기화
var custom_object = new EventEmitter();

// 3. events 모듈에 선언되어 있는 on( ) 함수를 재정의 하여 'call' 이벤트를 처리 
custom_object.on('call', ()=> {
    console.log('called events!');
});

// 4. call 이벤트를 강제로 발생
custom_object.emit('call');
```



## References

https://javafa.gitbooks.io/nodejs_server_basic/content/chapter7.html (event 사용하기)

