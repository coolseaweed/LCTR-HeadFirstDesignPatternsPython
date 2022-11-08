
## 프록시 패턴 핵심정리

- 프록시 패턴을 사용하면 어떤 객체의 대리인을 내세워서 클라이언트의 접근을 제어할 수 있다. 접근을 관리하는 방법에는 여러가지가 있다.

- 원격 프록시는 클라이언트와 원격 객체 사이의 데이터 전달을 관리해 준다.

- 가상 프록시는 인스턴스를 만드는 데 많은 비용이 드는 객체로의 접근을 제어한다.

- 보호 프록시는 호출하는 쪽의 권한에 딸라서 객체에 있는 메소드로의 접근을 제어한다.

- 그 외에도 캐싱 프록시, 동기화 프록시, 방화벽 프록시, 지연 복사 프록시와 같이 다양한 변형된 프록시 패턴이 있다.

- 프록시 패턴의 구조는 데코레이터 패턴의 구조와 비슷하지만 그 용도는 다르다.

- 데코레이터 패턴은 객체에 행동을 추가하지만 프록시 패턴은 접근을 제어한다.

- 잡에 내장된 프록시 지원 기능을 사용하면 동적 프록시 클래스를 만들어서 원하는 핸들러에서 호출을 처리하도록 할 수 있다.

- 다른 래퍼 (wrapper) 를 쓸 때와 마찬가지로 프록시를 쓰면 디자인에 포함되는 클래스와 객체의 수가 늘어난다.


## 테스트

### Setup ENV.
- python >= 3.6
```
pip install -r requirements.txt
```

### Gumball Machine (server) x n

```
python chapter_11/main_machine.py <location:str> <num_gumball:int> <ip address:any> <port:int>

# example
python chapter_11/main_machine.py test1 10 localhost 9091
```

### Gumball monitor (client) 
```
python chapter_11/main_monitor.py
-----------------------------------
* machine location: test1
* machine ball count: 1
* machine state: waiting for quarter

* machine location: test2
* machine ball count: 1
* machine state: waiting for quarter

* machine location: test3
* machine ball count: 0
* machine state: sold out
```