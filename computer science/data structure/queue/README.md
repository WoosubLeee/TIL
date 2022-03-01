# Queue

## Circular queue(순환 큐)

Circular queue는 queue 자료구조를 효율적으로 저장하기 위한 방식이다. Queue를 선형으로 구현할 경우, 배열은 크기가 고정되어 있기 때문에 배열의 마지막까지 다 차게되면 더이상 데이터를 담을 수 없게 되는 문제가 발생한다. 

이를 해결하기 위해 순환 큐가 고안되었다. 후단의 위치가 배열의 끝에 도달했을 때, 후단의 위치를 배열의 첫번째 인덱스로 옮기면서 용량의 한계를 해결할 수 있다. 이때, 순환 큐의 full 상태와 empty 상태를 구별하기 위해 배열의 한 칸은 비워둔다.

### 구현

front를 가장 앞 인덱스에서 한 칸 앞에 둔다(ear를 한 칸 뒤에 둘 수도 있는데 이는 선택이다).

![img](https://t1.daumcdn.net/cfile/tistory/991E713359E0297D19)

`rear == front` 비어있는 상태다.

![img](https://t1.daumcdn.net/cfile/tistory/99A4A53359E029D012)

![img](https://t1.daumcdn.net/cfile/tistory/993FCB3359E02A3D12)

![img](https://t1.daumcdn.net/cfile/tistory/99C29B3359E02AE020)

이제 포화 상태이므로 더이상 enqueue가 실행되지 못한다.

![img](https://t1.daumcdn.net/cfile/tistory/99885B3359E02B651F)

![img](https://t1.daumcdn.net/cfile/tistory/991E383359E02BC310)





## References

https://janggom.tistory.com/287

https://likewiki.soksok.co.kr/entry/%ED%81%90-Queue-%ED%81%90%EC%9D%98-%EC%A3%BC%EC%9A%94-%EA%B8%B0%EB%8A%A5-%EC%88%9C%ED%99%98-%ED%81%90