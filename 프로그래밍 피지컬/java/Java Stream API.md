## Stream 개념
---
Stream은 Java 8에서 도입된 기능으로, 데이터의 흐름을 표현하는 객체입니다. 컬렉션, 배열 등의 데이터 소스로부터 생성되며, 데이터를 순차적으로 또는 병렬로 처리할 수 있게 해줍니다.

[이 글](https://www.elancer.co.kr/blog/view?seq=255)을 참고하면 Java에서 제공하는 Stream API에 대해 이해하기 수월할 것이다.

## Stream의 주요 특징:
---
1. 파이프라이닝 (Pipelining):
   - 여러 연산을 연결하여 복잡한 데이터 처리 파이프라인을 구성할 수 있습니다.
   - 예: `stream.filter(...).map(...).reduce(...)`

2. 내부 반복 (Internal Iteration):
   - 반복 처리를 Stream 내부에서 처리합니다.
   - 개발자는 "무엇"을 할지만 정의하고, "어떻게" 할지는 Stream에 맡깁니다.

3. 지연 연산 (Lazy Evaluation):
   - 최종 연산이 호출되기 전까지는 중간 연산이 실행되지 않습니다.
   - 이를 통해 효율적인 처리가 가능합니다.

4. 한 번만 사용 (One-time Use):
   - Stream은 한 번 사용하면 닫히며, 재사용할 수 없습니다.
## Stream의 주요 연산:
---
1. Stream 생성:
   - Stream API를 사용하여 data를 가공하기 위해 최초 1회 수행
   - 모든 data가 한번에 memory에 load되지 않는 것이 특징
   - 새 data가 필요할 때마다 추가 load

2. 중간 연산 (Intermediate Operations) 또는 가공:
   - 중간 연산의 입력값과 출력값이 모두 Stream이라는 것이 특징
   - filter(): 조건에 맞는 요소만 선택
   - map(): 각 요소를 변환
   - flatMap(): 각 요소를 스트림으로 변환 후 하나의 스트림으로 평탄화
   - sorted(): 요소 정렬
   - distinct(): 중복 제거
   - limit(): 요소 수 제한
   - skip(): 처음 n개 요소 건너뛰기

3. 최종 연산 (Terminal Operations):
   - 최종 연산이 수행되면 Stream이 닫히고, 더 이상 중간 연산을 진행할 수 없다는 것이 특징
   - 최종 연산을 만나게 될 때, 비로소 기존에 chain을 해둔 중간 연산을 순차적으로 실행하는 `지연연산`을 수행
   - forEach(): 각 요소에 대해 동작 수행
   - collect(): 요소를 컬렉션으로 변환. 'Collectors' 클래스를 활용한다.
	   - Collectors.toList()
	   - Collectors.toSet()
	   - Collectors.toCollection( ... )  << stream을 구체화된 collection으로 변환
	   - Collectors.toMap()
	   - Collectors.toArray()
   - reduce(): 요소를 하나의 결과로 줄임
   - count(): 요소 개수 반환
   - anyMatch(), allMatch(), noneMatch(): 조건 충족 여부 확인
   - findFirst(), findAny(): 조건에 맞는 요소 찾기

### 1. Stream 생성 방법:
```java
// 컬렉션에서 생성
List<String> list = Arrays.asList("a", "b", "c");
Stream<String> stream = list.stream();

// 배열에서 생성
String[] arr = {"a", "b", "c"};
Stream<String> stream = Arrays.stream(arr);

// 직접 생성
Stream<String> stream = Stream.of("a", "b", "c");

// 무한 스트림 생성
Stream<Integer> infiniteStream = Stream.iterate(0, n -> n + 2);
// 제한된 스트림 생성
Stream<Integer> limitedStream = Stream.iterate(1, n -> n * 2).limit(5);
```

### 2. Stream 중간 연산:

1. filter(): 조건에 맞는 요소만 선택

```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
List<Integer> evenNumbers = numbers.stream()
                                   .filter(n -> n % 2 == 0)
                                   .collect(Collectors.toList());
System.out.println(evenNumbers); // 출력: [2, 4, 6, 8, 10]
```

2. map(): 각 요소를 변환

```java
List<String> names = Arrays.asList("John", "Jane", "Adam", "Eve");
List<Integer> nameLengths = names.stream()
                                 .map(String::length)
                                 .collect(Collectors.toList());
System.out.println(nameLengths); // 출력: [4, 4, 4, 3]
```

3. flatMap(): 각 요소를 스트림으로 변환 후 하나의 스트림으로 평탄화

```java
List<List<Integer>> nestedList = Arrays.asList(
    Arrays.asList(1, 2, 3),
    Arrays.asList(4, 5, 6),
    Arrays.asList(7, 8, 9)
);
List<Integer> flattenedList = nestedList.stream()
                                        .flatMap(List::stream)
                                        .collect(Collectors.toList());
System.out.println(flattenedList); // 출력: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

4. sorted(): 요소 정렬

```java
List<Integer> numbers = Arrays.asList(3, 1, 4, 1, 5, 9, 2, 6, 5);
List<Integer> sortedNumbers = numbers.stream()
                                     .sorted()
                                     .collect(Collectors.toList());
System.out.println(sortedNumbers); // 출력: [1, 1, 2, 3, 4, 5, 5, 6, 9]
```

5. distinct(): 중복 제거

```java
List<Integer> numbers = Arrays.asList(1, 2, 2, 3, 3, 4, 5, 5);
List<Integer> distinctNumbers = numbers.stream()
                                       .distinct()
                                       .collect(Collectors.toList());
System.out.println(distinctNumbers); // 출력: [1, 2, 3, 4, 5]
```

6. limit(): 요소 수 제한

```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
List<Integer> firstFive = numbers.stream()
                                 .limit(5)
                                 .collect(Collectors.toList());
System.out.println(firstFive); // 출력: [1, 2, 3, 4, 5]
```

7. skip(): 처음 n개 요소 건너뛰기

```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
List<Integer> afterFive = numbers.stream()
                                 .skip(5)
                                 .collect(Collectors.toList());
System.out.println(afterFive); // 출력: [6, 7, 8, 9, 10]
```

8. peek(): 각 요소에 대해 작업 수행 (주로 디버깅 용도)

```java
List<String> names = Arrays.asList("Alice", "Bob", "Charlie");
List<String> upperCaseNames = names.stream()
                                   .peek(name -> System.out.println("Processing: " + name))
                                   .map(String::toUpperCase)
                                   .collect(Collectors.toList());
System.out.println(upperCaseNames);
// 출력:
// Processing: Alice
// Processing: Bob
// Processing: Charlie
// [ALICE, BOB, CHARLIE]
```

이러한 중간 연산들은 서로 연결하여 복잡한 데이터 처리 파이프라인을 구성할 수 있습니다. 예를 들어:

```java
List<String> result = names.stream()
                           .filter(name -> name.length() > 3)
                           .map(String::toUpperCase)
                           .sorted()
                           .limit(2)
                           .collect(Collectors.toList());
```

### 3. Stream 최종 연산:

1. forEach(): 각 요소에 대해 동작 수행

```java
List<String> names = Arrays.asList("Alice", "Bob", "Charlie");
names.stream().forEach(name -> System.out.println("Hello, " + name));
// 출력:
// Hello, Alice
// Hello, Bob
// Hello, Charlie
```

2. collect(): 요소를 컬렉션으로 변환

```java
List<String> names = Arrays.asList("Alice", "Bob", "Charlie");
Set<String> nameSet = names.stream().collect(Collectors.toSet());
System.out.println(nameSet); // 출력: [Alice, Bob, Charlie]
```

3. reduce(): 요소를 하나의 결과로 줄임

```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
int sum = numbers.stream().reduce(0, (a, b) -> a + b);
System.out.println("Sum: " + sum); // 출력: Sum: 15
```

4. count(): 요소 개수 반환

```java
List<String> names = Arrays.asList("Alice", "Bob", "Charlie", "David");
long count = names.stream().filter(name -> name.length() > 4).count();
System.out.println("Names longer than 4 characters: " + count); // 출력: 2
```

5. anyMatch(), allMatch(), noneMatch(): 조건 충족 여부 확인

```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
boolean anyEven = numbers.stream().anyMatch(n -> n % 2 == 0);
boolean allEven = numbers.stream().allMatch(n -> n % 2 == 0);
boolean noneNegative = numbers.stream().noneMatch(n -> n < 0);

System.out.println("Any even? " + anyEven); // 출력: true
System.out.println("All even? " + allEven); // 출력: false
System.out.println("None negative? " + noneNegative); // 출력: true
```

6. findFirst(), findAny(): 조건에 맞는 요소 찾기

```java
List<String> names = Arrays.asList("Alice", "Bob", "Charlie");
Optional<String> firstNameWithA = names.stream()
                                       .filter(name -> name.startsWith("A"))
                                       .findFirst();
System.out.println(firstNameWithA.orElse("No name found")); // 출력: Alice
```

7. min(), max(): 최솟값, 최댓값 찾기

```java
List<Integer> numbers = Arrays.asList(3, 1, 4, 1, 5, 9, 2, 6);
Optional<Integer> min = numbers.stream().min(Integer::compare);
Optional<Integer> max = numbers.stream().max(Integer::compare);

System.out.println("Min: " + min.orElse(0)); // 출력: Min: 1
System.out.println("Max: " + max.orElse(0)); // 출력: Max: 9
```

8. toArray(): 스트림을 배열로 변환

```java
List<String> names = Arrays.asList("Alice", "Bob", "Charlie");
String[] nameArray = names.stream().toArray(String[]::new);
System.out.println(Arrays.toString(nameArray)); // 출력: [Alice, Bob, Charlie]
```

9. 복잡한 collect() 사용 예시 (그룹화)

```java
List<String> names = Arrays.asList("Alice", "Bob", "Charlie", "David", "Eve");
Map<Integer, List<String>> groupedByLength = names.stream()
    .collect(Collectors.groupingBy(String::length));
System.out.println(groupedByLength);
// 출력: {3=[Bob, Eve], 5=[Alice, David], 7=[Charlie]}
```

10. 통계 연산

```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
IntSummaryStatistics stats = numbers.stream()
    .mapToInt(Integer::intValue)
    .summaryStatistics();
System.out.println("Count: " + stats.getCount());
System.out.println("Sum: " + stats.getSum());
System.out.println("Min: " + stats.getMin());
System.out.println("Max: " + stats.getMax());
System.out.println("Average: " + stats.getAverage());
```

이러한 최종 연산들은 스트림 처리의 결과를 산출하며, 스트림을 소비합니다. 최종 연산 이후에는 해당 스트림을 재사용할 수 없습니다.

### Stream의 장점:
1. 코드의 가독성과 유지보수성 향상
2. 함수형 프로그래밍 스타일 지원
3. 병렬 처리 용이 (parallelStream() 사용)
4. 지연 연산을 통한 효율성 증대

### 주의할 점:
1. 과도한 사용은 오히려 성능 저하를 야기할 수 있습니다.
2. 상태를 가지는 연산 사용 시 주의가 필요합니다.
3. 병렬 스트림 사용 시 동시성 이슈에 주의해야 합니다.

Stream은 Java에서 데이터 처리를 위한 강력하고 유연한 도구입니다. 적절히 사용하면 코드의 품질과 성능을 크게 향상시킬 수 있습니다.