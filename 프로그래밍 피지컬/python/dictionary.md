Python에서 딕셔너리(dictionary)는 키(key)와 값(value)을 쌍으로 저장하는 자료형입니다. 딕셔너리는 가변적(mutable)이며, 키는 고유해야 하고 변경할 수 없는(immutable) 자료형이어야 합니다.

### 딕셔너리 사용법

#### 1. 딕셔너리 생성
딕셔너리는 중괄호 `{}`를 사용해 생성할 수 있습니다.

```python
# 빈 딕셔너리 생성
my_dict = {}

# 초기 값을 가진 딕셔너리 생성
my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}
```

#### 2. 값 접근하기
딕셔너리의 값은 키를 사용하여 접근할 수 있습니다.

```python
# 값 가져오기
name = my_dict['name']  # 'Alice'

# get() 메서드를 사용해 값 가져오기
age = my_dict.get('age')  # 25
```

`get()` 메서드를 사용하면, 키가 존재하지 않을 경우 `None`을 반환하거나, 기본값을 지정할 수 있습니다.

```python
# 키가 없을 때 기본값 반환
country = my_dict.get('country', 'Unknown')  # 'Unknown'
```

#### 3. 값 추가 및 수정하기
딕셔너리에 새로운 키-값 쌍을 추가하거나, 기존 값을 수정할 수 있습니다.

```python
# 새로운 키-값 쌍 추가
my_dict['email'] = 'alice@example.com'

# 기존 값 수정
my_dict['age'] = 26
```

#### 4. 값 삭제하기
키를 사용해 특정 항목을 삭제할 수 있습니다.

```python
# del 키워드 사용
del my_dict['city']

# pop() 메서드 사용
email = my_dict.pop('email')
```

#### 5. 딕셔너리 순회
딕셔너리의 키, 값, 혹은 키와 값 쌍을 반복할 수 있습니다.

```python
# 키 순회
for key in my_dict:
    print(key)

# 값 순회
for value in my_dict.values():
    print(value)

# 키와 값 쌍 순회
for key, value in my_dict.items():
    print(f'{key}: {value}')
```

#### 6. 딕셔너리 주요 메서드
- `keys()`: 모든 키를 반환
- `values()`: 모든 값을 반환
- `items()`: 모든 키-값 쌍을 반환
- `clear()`: 모든 항목을 삭제
- `update()`: 다른 딕셔너리의 항목을 추가

```python
# keys() 사용
keys = my_dict.keys()

# values() 사용
values = my_dict.values()

# items() 사용
items = my_dict.items()

# update() 사용
my_dict.update({'country': 'USA', 'phone': '123-456-7890'})

# clear() 사용
my_dict.clear()  # 모든 항목 삭제
```


### dictionary 활용법
#### switch문
python에는 공식적으로 switch-case 문이 존재하지 않는다. 그래서 python 공식 문서에서는 if-elif문 사용을 권장한다. 하지만 dictionary를 응용하면 switch문보다 더 간단히 switch문 기능을 하는 무언가를 만들어낼 수 있다.