# 객체지향 개념 정리

## 1. **Abstract Class** vs **Interface** 파이썬에서 차이점

기본적으로 Python 에서는 Java 와 달리 **Interface** 라는 공식적인 계약을 가지고 있지않다. 또한 Java 는 다중 상속이 없기 때문에 **Interface** 를 사용하지만, Python 에는 다중 상속이 있기 때문에 기본적으로 **Abstract class** 를 사용해서 **Interface** 를 정의한다. **Abstract Class** 와 **Interface** 개념의 차이점은 그 목적이라고 할 수 있다. 

`Abstract Class`: 기본적으로 클래스이며 이를 상속, 확장하여 사용하기 위한 것

`Interface`: Interface 를 구현한 객체들에 대한 동일한 사용방법과 동작을 보장하기 위한 것

java based OOP 에서 말하는 abstract class 와 interface 의 차이는 다음과 같으니 참고해보자

|`Abstract class`|`Interface`|
|:---|:---|
|다중 상속 X|다중 구현 O|
|데이터 멤버 O|데이터 멤버 X|
|생성자 O|생성자 X|
|추상 메소드와 메소드 둘다 존재 가능|추상 메소드만 존재 가능|
|변경자가 접근 O|변경자가 접근 X (모든게 public 이라고 가정)|
|오직 완성된 멤버만 static O|멤버는 static X|

## 2. **Serialize & Deserialize**

**Serialize**: 시스템상의 객체를 바이트(byte)로 변환하는 것

**Deserialize**: 바이트(byte)로 변환된 객체를 다시 시스템에서의 객체로 변환하는 것





---
