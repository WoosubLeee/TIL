# Import



## Absolute / Relative import

Absolute imports - import something available on `sys.path`
Relative imports - import something relative to the current module, must be a part of a package

Relative imports는 `__main__` 모듈과 같은 패키지 안에 있어야만 사용이 가능하다.

자료 구조가 아래와 같다고 하자.

```
.
./main.py
./pack/aaa.py
./pack/bbb.py
```

`aaa.py`와 `bbb.py`의 코드는 다음과 같다.

```
# aaa.py

test = True
```

```
# bbb.py

print(__name__)

# Relative import
try:
	# Trying to find moudle in the parent package
	from . import aaa
	print(aaa.test)
	del aaa
except ImportError:
	print('Relative import failed')
	
# Absolute import
try:
	# Trying to find module on sys.path
	import aaa
	print(aaa.test)
except MoudleNotFoundError:
	print('Absolute import failed')
```

`bbb.py`를 실행해보자.

```
$ python pack/bbb.py
__main__
Relative import failed
True
```

`bbb.py`가 `__main__`모듈이므로 같은 패키지 안에 있는 `aaa.py`를 Relative import하는데는 실패하고, Absolute import하는데는 성공하였다.



이번에는 `main.py`를 다음과 같이 작성하여 실행해보자.

```
# main.py
import pack.bbb
```

```
$ python bbb.py
pack.bbb
True
Absolute import failed
```

`main.py`가 `__main__`모듈이므로 하위 패키지 안에 있는 `aaa.py`를 Absolute import하는데는 실패하고, Relative import하는데는 성공하였다.



## Circular import

```
# a.py
import b

def a_method():
	print('a')
	
b.b_method()
```

```
# b.py
import a

def b_method():
	print('b')
	a.a_method()
```

위와 같이 코드가 작성된 상황일 때
`a.py` 혹은 `b.py`를 실행하게 되면
에러가 발생하게 된다.

이는 `a.py`에서 `b.py`를 import하고, `b.py`에서 `a.py`를 import하는 circular import가 발생하고 있기 때문인데, import를 무한히 반복하여 결국 에러가 나는 것이다.

이를 해결하기 위해서는 둘 중 하나의 import를 runtime 안으로 넣어줘야 한다.
(여기부턴 뇌피셜) 코드가 실행될 때는 처음에 compile될 때와 코드가 읽혀지며 실행되는 runtime이 있는데 import를 runtime으로 넣어주면 코드의 method가 실행될 때 import되기 때문에 에러가 발생하지 않게 된다.

```
# b.py
def b_method():
	import a
	print('b')
	a.a_method()
```

위와 같이 작성하면 에러가 발생하지 않는다.