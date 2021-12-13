# ViewModel

## What is ViewModel for?

![img](https://blog.kakaocdn.net/dn/cSKcuQ/btqZtzDBTBM/qTllqo5wizNHkLEkCBzLI1/img.gif)

화면을 가로로 회전하니 증가되었던 값이 초기화되었다. 이런 현상이 발생하는 이유는 바로 lifecycle 때문이다. 화면 회전이 이루어지면 activity가 Destory 됐다가 다시 Create 되기 때문에 기존의 데이터가 날아가는 것이다. `ViewModel` 클래스를 사용하면 화면 회전과 같이 구성을 변경할 때도 데이터를 유지할 수 있다.

