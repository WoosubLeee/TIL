# Workshop

## 1. 도형 만들기

```
class Point:
    
    # x와 y를 initialize
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    
    # p1과 p2를 initialize
    def __init__(self, p1, p2):
        # 직사각형의 가로와 세로를 계산
        self.width = p2.x - p1.x
        self.height = p1.y - p2.y
    
    # p1, p2 간 x좌표의 차와 p1, p2 간 y좌표의 차를 곱하여 반환
    def get_area(self):
        return self.width*self.height
    
    # p1, p2 간 x좌표의 차와 p1, p2 간 y좌표의 차를 더해서 반환
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    
    # p1, p2간 x좌표의 차와 p1, p2 간 y좌표의 차가 같은지 반환
    def is_square(self):
        return self.width == self.height
```



# Homework

## 1. Circle 인스턴스 만들기

```
# Circle 클래스의 인스턴스 c1을 initialize하며 반지름과 x, y 좌표를 initialize
c1 = Circle(3, 2, 4)
# area()와 circumference() 함수 활용
print(c1.area())
>>> 28.259999999999998
print(c1.circumference())
>>> 18.84
```



## 2. Dog과 Bird는 Animal이다

```
# Animal 클래스를 상속
class Dog(Animal):
    def __init__(self, name):
        # super()를 사용해 부모 클래스의 __init__ 메서드를 이용
        super().__init__(name)

    def walk(self):
        return f'{self.name}! 달린다!'

    def bark(self):
        return f'{self.name}! 짖는다!'

# Animal 클래스를 상속
class Bird(Animal):
    def __init__(self, name):
        # super()를 사용해 부모 클래스의 __init__ 메서드를 이용
        super().__init__(name)

    def walk(self):
        return f'{self.name}! 걷는다!'
    
    def eat(self):
        return f'{self.name}! 먹는다!'

    def fly(self):
        return f'{self.name}! 푸드덕!'
```



## 3. 오류의 종류

`ZeroDivisionError` : 0으로 나누려할 때 발생하는 에러

`NameError` : 정의되지 않은 변수를 호출

`TypeError` : 자료형이 잘못되었을 경우 ex) int + str

` IndexError` : 존재하지 않는 index로 조회할 경우

`KeyError` : 딕셔너리에 해당 key가 없는 경우

`MoudleNotFoundError` : 해당 모듈이 없는 경우

`ImportError` : 모듈은 찾았으나 존재하지 않는 클래스나 함수를 호출하였을 경우

