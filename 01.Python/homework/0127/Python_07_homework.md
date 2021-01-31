# Workshop

## 1. pip

`$ pip install faker`

(1) 위 명령어는 faker라는 패키지를 설치하기 위한 명령어이다.

(2) 터미널에서 실행해야 한다.



## 2. Basic Usages

```
# 1 faker 패키지에서 faker 클래스를 import하기 위한 코드이다.
from faker import faker
# 2 Faker는 클래스, fake는 인스턴스이다.
fake = Faker()
# 3 name()은 fake의 메서드이다.
fake.name()
```



## 3. Localization

```
class Faker():

    def __init__(self, locale='en_US'):
        pass
```



## 4. Seeding the Generator

```
fake = Faker('ko_KR')
Faker.seed(4321)
print(fake.name())
>>> 이도윤

fake2 = Faker('ko_KR')
print(fake2.name())
>>> 이지후
```

seed()는 클래스 메서드로
seed() 메서드로 시드를 설정하면 해당 클래스로 만들어진 모든 인스턴스들은 지정된 순서로 이름을 반환하게 된다.

```
fake = Faker('ko_KR')
fake.seed_instance(4321)
print(fake.name())
>>> 이도윤

fake2 = Faker('ko_KR')
print(fake2.name())
>>> 김미숙
```

seed_instance()는 인스턴스 메서드로
seed_instance() 메서드로 시드를 설정하면 해당 인스턴스만 시드에 맞는 지정된 순서의 이름을 반환한다.



# Homework

## 1. Type Class

`int, float, str, bool, complex`



## 2. Magic Method

`__init__` : 생성자 메서드. 인스터스 객체가 생성될 때 인스턴스의 속성을 정의한다.

`__del__` : 소멸자 메서드. 인스턴스 객체가 소멸될 때 호출되는 메서드

`__str__` : 특정 객체가 출력(print())될 때 나올 informal한 내용을 정의하는 메서드

`__repr__` : 특정 객체의 formal한 string representation을 정의하는 메서드



## 3. Instance Method

`.get(key[, default])` : 딕셔너리에서 key를 이용해 value를 반환한다.

`.append(x)` : 리스트에 값을 추가할 수 있다.

`.extend(x)` : 리스트에 iterable을 추가할 수 있다.



## 4. Module import

`from fibo import fibo_recursion as recursion`

