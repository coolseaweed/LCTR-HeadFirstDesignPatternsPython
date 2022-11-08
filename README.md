# Head First Design Patterns

### 객체지향 원칙
- 바뀌는 부분은 캡슐화한다.
- 상속보다는 구성(Component)을 활용한다.
- 구현보다는 인터페이스에 맞춰서 프로그래밍한다.
- 상호작용하는 객체 사이에서는 가능하면 `느슨한 결합`을 사용해야 한다.
- 클래스는 확장에는 열려있어야 하지만 변경에는 닫혀 있어야 한다. `(OCP: Open-Closed Principle)`
- 추상화된 것에 의존하게 만들고 구상 클래스에 의존하지 않게 만든다.
- 최소 지식 원칙에 따라 객체 사이의 상호작용은 될 수 있으면 아주 가까운 객체 사이에서만 허용하는 편이 좋다.
- `할리우드 원칙` 을 활용해서 의존성 부패를 방지한다.
- 어떤 클래스가 바뀌는 이유는 하나뿐이여야만 한다.

---
### [CHAPTER 1. 전략 패턴 (Strategy Pattern)](https://github.com/coolseaweed/head_first_design_patterns_python/tree/main/chapter_01)
전략패턴은 알고리즘군을 정의하고 캡슐화해서 각각의 알고리즘 군을 수정해서 쓸 수 있게 해준다. 전략패턴을 사용하면 클라이언트로부터 알고리즘을 분리해서 독립적으로 변경 할 수 있다.

### [CHAPTER 2. 옵저버 패턴 (Observer Pattern)](https://github.com/coolseaweed/head_first_design_patterns_python/tree/main/chapter_02)
한 객체의 상태가 바뀌면 그 객체에 의존하는 다른 객체에게 연락이가고 자동으로 내용이 갱신되는 방식으로 일대다 (one-to-many) 의존성을 정의한다.

### [CHAPTER 3. 데코레이터 패턴 (Decorator Pattern)](https://github.com/coolseaweed/head_first_design_patterns_python/tree/main/chapter_03)
객체에 추가 요소를 동적으로 더할 수 있다. 데코레이터를 사용하면 서브클래스를 만들 때보다 훨씬 유연하게 기능을 확장할 수 있다.

### [CHAPTER 4. 팩토리 패턴 (Factory Pattern)](https://github.com/coolseaweed/head_first_design_patterns_python/tree/main/chapter_04)
**팩토리 매소드 패턴 (Factory Method Pattern)**: 객체를 생성할 때 필요한 인터페이스를 만든다. 어떤 클래스의 인스턴스를 만들지는 서브클래스에서 결정한다. 팩토리 메소드를 사용하면 인스턴스 만드는 일을 서브클래스에 맡길 수 있다.

**추상 팩토리 패턴 (Abstract Factory Pattern)**: 구상 클래스에 의존하지 않고도 서로 연관되거나 의존적인 객체로 이루어진 제품군을 생성하는 인터페이스를 제공한다. 구상 클래스는 서브클래스에서 만든다.

### [CHAPTER 5. 싱글턴 패턴 (Singleton Pattern)](https://github.com/coolseaweed/head_first_design_patterns_python/tree/main/chapter_05)
**싱글턴 패턴 (Singleton Pattern)**: 클래스 인스턴스를 하나만 만들고, 그 인스턴스로의 전역 접근을 제공한다.

### [CHAPTER 6. 커맨드 패턴 (Command Pattern)](https://github.com/coolseaweed/head_first_design_patterns_python/tree/main/chapter_06)
요청 내역을 객체로 캡슐화해서 객체를 서로 다른 요청 내역에 따라 매개변수화할 수 있다. 이러면 요청을 큐에 저장하거나 로그로 기록하거나 작업 취소 기능을 사용할 수 있다.


### [CHAPTER 7. 어댑터 & 퍼사드 패턴 (Adapter & Facade Pattern)](https://github.com/coolseaweed/head_first_design_patterns_python/tree/main/chapter_07)
**어댑터 패턴 (Adapter Pattern)**: 특정 클래스 인터페이스를 클라이언트에서 요구하는 다른 인터페이스로 변환한다. 인터페이스가 호환되지 않아 같이 쓸 수 없었던 클래스를 사용할 수 있게 도와준다.
**퍼사드 패턴 (Facade Pattern)**: 서브시스템에 있는 일련의 인터페이스를 통합 인터페이스로 묶어 준다. 또한 고수준 인터페이스도 정의하므로 서브시스템을 더 편리하게 사용할 수 있다.

### [CHAPTER 8. 템플릿 패턴 (Template Pattern)](https://github.com/coolseaweed/head_first_design_patterns_python/tree/main/chapter_08)
알고리즘의 골격을 정의한다. 템플릿 메소드를 사용하면 알고리즘의 일부 단계를 서브클래스에서 구현할 수 있으며, 알고리즘의 구조는 그대로 유지하면서 알고리즘의 특정 단계를 서브클래스에서 재정의할 수도 있다.


### [CHAPTER 9. 반복자 & 컴포지트 패턴 (Iterator & Composite Pattern)](https://github.com/coolseaweed/head_first_design_patterns_python/tree/main/chapter_09)
**반복자 패턴 (Iterator Pattern)**: 컬렉션의 구현 방법을 노출하지 않으면서 집합체 내의 모든 항목에 접근하는 방법을 제공한다.

**컴포지트 패턴 (Composite Pattern)**: 객체를 트리구조로 구성해서 부분-전체 계층구조를 구현한다. 컴포지트 패턴을 사용하면 클라이언트에서 개별 객체와 복합 객체를 똑같은 방법으로 다룰 수 있다.


### [CHAPTER 10. 상태 패턴 (State Pattern)](https://github.com/coolseaweed/head_first_design_patterns_python/tree/main/chapter_10)
내부 상태가 바뀜에 따라 객체의 행동이 바뀔 수 있도록 해준다. 마치 객체의 클래스가 바뀌는 것 같은 결과를 얻을 수 있다.


### [CHAPTER 11. 프록시 패턴 (Proxy Pattern)](https://github.com/coolseaweed/head_first_design_patterns_python/tree/main/chapter_11)
특정 객체로의 접근을 제어하는 대리인(특정 객체를 대변하는 객체)을 제공한다.


### [CHAPTER 12. 복합 패턴 (Combining Pattern)](https://github.com/coolseaweed/head_first_design_patterns_python/tree/main/chapter_12)
2개 이상의 패턴을 결합해서 일반적으로 자주 등장하는 문제들의 해법을 제공한다.



---

### [Q&A](https://github.com/coolseaweed/head_first_design_patterns_python/tree/main/QnA)

