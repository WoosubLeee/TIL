# Buffer

## What is buffer?

버퍼란 임시 저장 공간을 의미한다. 정확히 말하면 A와 B가 서로 입출력을 수행하는데에 있어서 속도 차이를 극복하기 위해 사용하는 임시 저장 공간을 의미한다.

### 동영상 스트리밍 서비스에서의 buffer

<img src="https://t1.daumcdn.net/cfile/tistory/99C2DB405A425EDA30" alt="img" style="zoom: 50%;" />

여기서 저 밝은 회색부분이 버퍼라고 볼 수 있다.

동영상 데이터가 내려 받아지는 속도에 비해 우리가 동영상을 1초씩 진행되며 보는 속도에는 차이가 있다. 만약 우리가 동영상을 보는 속도와 데이터를 내려받는 속도가 같다면 동영상 재생시간이 50분짜리 동영상이라면 50분동안 데이터를 내려받아야 한다. 그러나 이는 비효율적이므로 버퍼라는 임시 저장공간을 두고 동영상 데이터를 버퍼에 최대한 빠른 시간 안에 내려받아 저장해 둔다.

인터넷이 많이 느리던 시절에는 동영상을 버퍼에 다운로드 하는 속도가 동영상을 시청하는 속도를 따라가지 못해 빨간 부분이 회색 부분을 따라잡게 됐고 동영상이 멈추는 일이 빈번했습니다. "그리고 이를 버퍼링 걸린다" 라고들 이야기 했다.



## 입출력에서 사용되는 buffer

프로그래밍이나 운영체제에서 사용하는 버퍼는 거의 대부분 **CPU**와 **보조기억장치** 사이에서 사용되는 임시 저장 공간을 의미한다. 

CPU는 기술이 발전함에 따라 1초에 수십억 bit 그 이상의 데이터를 처리할 수 있다. 그러나 보조기억 장치의 경우 데이터를 주고 받는데에 많은 시간이 필요하다. 물리적인 HDD(하드디스크)의 경우 데이터를 전송할 수 있는 속도는 빨라도 초당 100mb ~ 300mb 이다.

<img src="https://t1.daumcdn.net/cfile/tistory/99B1B9405A425ED933" alt="img" style="zoom: 67%;" />

<img src="https://t1.daumcdn.net/cfile/tistory/99D343405A425ED92C" alt="img" style="zoom: 67%;" />



이 때 버퍼를 사용하게 된다. 버퍼는 CPU 내부에 있는 캐시메모리 보다는 느리지만 보조 기억 장치보다 훨씬 빠른 주기억 장치(RAM)를 이용한다. 보조기억장치는 주기억장치의 버퍼로 마련해둔 공간에 데이터를 열심히 보내 쌓아둔다. CPU는 처리가 빠르므로 밀려있는 다른일을 처리한 후 시간이 남을때 가끔 버퍼를 확인하여 데이터가 모두 쌓였는지 확인하고 모두 쌓였다면 가져다 한꺼번에 처리한다.

그 덕분에 CPU는 100퍼센트의 효율로 연산을 할 수 있다.**이렇게 버퍼라는 것은 속도차가 큰 두 대상이 입출력을 수행할 때 효율성을 위해 사용하는 임시 저장공간이라고 할 수 있겠다.**



## References

https://dololak.tistory.com/84 ([개념정리\] 버퍼(BUFFER)란? 버퍼 개념)