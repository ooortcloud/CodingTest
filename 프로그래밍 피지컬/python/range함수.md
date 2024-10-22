`range()` 함수는 Python에서 숫자의 시퀀스를 생성할 때 사용되는 매우 유용한 함수입니다. 주로 `for` 루프와 함께 사용되며, 다양한 형태로 숫자 범위를 정의할 수 있습니다. `range()` 함수는 세 가지 주요 인수를 사용할 수 있습니다: `start`, `stop`, `step`. 기본적으로 `range()`는 아래와 같은 형식으로 사용됩니다.

### 1. 기본 사용법

```python
range(stop)
```
- `stop`: 생성할 숫자의 범위를 정의합니다. 이때 `stop` 값은 **포함되지 않습니다**. 즉, `range(stop)`은 0에서 `stop-1`까지의 숫자를 생성합니다.

예시:
```python
for i in range(5):
    print(i)
```
출력:
```
0
1
2
3
4
```

### 2. 시작 값 지정

```python
range(start, stop)
```
- `start`: 숫자가 시작될 값을 정의합니다. 
- `stop`: 마지막 값 **직전**까지의 범위를 지정합니다.

예시:
```python
for i in range(2, 6):
    print(i)
```
출력:
```
2
3
4
5
```

### 3. 단계 값 지정

```python
range(start, stop, step)
```
- `start`: 시작 값.
- `stop`: 마지막 값 **직전**까지의 범위.
- `step`: 숫자 간격을 지정합니다. 양수일 경우 증가, 음수일 경우 감소하는 시퀀스를 생성합니다.

예시:
```python
for i in range(0, 10, 2):
    print(i)
```
출력:
```
0
2
4
6
8
```

### 4. 역순 시퀀스 생성

`step` 값으로 음수를 지정하여 역순으로 숫자를 생성할 수 있습니다.

예시:
```python
for i in range(5, 0, -1):
    print(i)
```
출력:
```
5
4
3
2
1
```

### 5. `range()`의 반환 값

`range()`는 실제 리스트가 아닌 **range 객체**를 반환합니다. 따라서 메모리를 절약하며, 필요할 때만 값을 생성하는 **lazy evaluation** 방식으로 작동합니다. 만약 리스트가 필요하다면 `list()` 함수로 변환할 수 있습니다.

예시:
```python
numbers = list(range(5))
print(numbers)
```
출력:
```
[0, 1, 2, 3, 4]
```

### 요약
- `range(stop)`: 0부터 `stop-1`까지의 숫자.
- `range(start, stop)`: `start`부터 `stop-1`까지의 숫자.
- `range(start, stop, step)`: `step` 간격으로 `start`부터 `stop-1`까지의 숫자.
- 음수 `step`을 사용하여 역순으로 범위를 생성 가능.