# `asyncio`

Python에서 asynchronous programming을 하려면 `asyncio` 라이브러리를 사용하면 된다.



## `coroutine`

함수의 `def` 앞에 `async` 키워드를 붙이면 이 함수는 비동기 처리되며, 이러한 비동기 함수를 Python에서는 `coroutine` 이라고 부른다. `async` 함수 내에서 synchronous 하게 동작시키기 위해 `await` 키워드를 사용한다.

```python
import asyncio

async def main():
    print('before wait')
    await asyncio.sleep(1)
    print('after wait 1 second')
```

Note that simply calling a coroutine will not schedule it to be executed. To actually run a coroutine, `asyncio.run()` should be used at the top-level entry point.

```python
asyncio.run(main())

# before wait
# after wait 1 second
```



## `Task`

그렇다면 coroutine 여러 개를 비동기적으로 실행시키려면 어떻게 해야할까? The `asyncio.create_task()` function to run coroutines concurrently as asyncio `Tasks`.

```python
async def main():
    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

    
# started at 17:14:32
# hello
# world
# finished at 17:14:34
```

### 위 코드의 흐름

`create_task()`로 Task가 생성되는 순간 coroutine의 코드들은 비동기적으로 실행되기 시작한다.

```python
# 이 시점에 이미 코드는 실행되기 시작한다.
task1 = asyncio.create_task(say_after(1, 'hello'))
task2 = asyncio.create_task(say_after(2, 'world'))
```

하지만 비동기적으로 실행되기 때문에 실행이 완료되지 않아도 1) 뒤에 더 실행할 코드가 없다면 종료되거나, 2) 해당 coroutine의 반환값을 필요로 할 경우 에러가 발생 하게 된다.

이에 `await` 키워드를 사용해 coroutine이 완료되기를 기다린다.

```python
await task1
await task2
```

### `Future`

A `Future` is a special awaitable object that represents an **eventual result** of an asynchronous operation. `Task` 앞에 `await` 키워드를 앞에 붙여주면 `Future` object를 저장할 수 있고, coroutine의 반환값을 활용할 수 있다.

```python
return_value = await task1
```



## `coroutine`이 아닌 함수 asynchronous하게 이용하기

`await` 뒤에는 awaitable(`coroutine`, `Task`, `Future`)만 올 수 있기 때문에 `coroutine`이 아닌 기존 함수들은 비동기 작업을 위의 방법으로 실행할 수 없다. 하지만 event loop의 `loop.run_in_executor()`을 이용하면 기존 함수도 비동기적으로 사용할 수 있다.

`loop.run_in_executor(executor, func, *args)` : Arrange for *func* to be called in the specified executor. Returns a `Future` object.

**arguments**

- `executor` : `None`을 넣으면, default executor를 배정한다.
- `func` : 실행할 함수
- `*args` : 함수의 인자들

### ex)

```python
import asyncio
import time


async def coroutine_1():
    print('코루틴 1 시작')
    print('코루틴 1 중단')
    
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, time.sleep, 5)
    
    print('코루틴 1 재개')


async def coroutine_2():
    print('코루틴 2 시작')
    print('코루틴 2 중단')
    
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, time.sleep, 5)
    
    print('코루틴 2 재개')

if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    # 두 개의 코루틴이 이벤트 루프에서 돌 수 있게 스케쥴링

    loop.run_until_complete(asyncio.gather(coroutine_1(), coroutine_2()))
```

```
# 응답
코루틴 1 시작
코루틴 1 중단
코루틴 2 시작
코루틴 2 중단
코루틴 2 재개
코루틴 1 재개
```

#### 함수 설명

`loop.run_until_complete()` : `Future`를 인자로 받아 완료될 때까지 실행하고, 그 결과값을 return한다.

`asyncio.gather()` : Run awaitable objects concurrently(asynchronously).



## References

https://docs.python.org/3.8/library/asyncio-task.html

https://www.youtube.com/watch?v=t5Bo1Je9EmE&t=771s&ab_channel=TechWithTim (Python 비동기 프로그래밍-AsyncIO 및 Async / Await)

https://www.daleseo.com/python-asyncio/ ([파이썬] asyncio로 비동기 처리하기)

https://wikidocs.net/21046 (02_비동기 프로그래밍(Async))

https://sjquant.tistory.com/14 (파이썬과 비동기 프로그래밍 #2, 파이썬에서 비동기 프로그래밍 시작하기)