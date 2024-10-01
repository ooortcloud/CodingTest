Java의 `Comparable` 인터페이스는 객체 간 **자연 순서**(natural ordering)를 정의하기 위한 인터페이스입니다. 이 인터페이스를 구현한 클래스는 특정 기준에 따라 객체를 **정렬**할 수 있습니다. `Comparable` 인터페이스를 구현하려면, 클래스는 반드시 `compareTo` 메서드를 정의해야 합니다.

### `Comparable` 인터페이스의 핵심 메서드

```java
int compareTo(T o);
```

- `compareTo` 메서드는 객체 자신과 전달된 객체 `o`를 비교하여 **정수 값**을 반환합니다.
  - 음수 값: 현재 객체가 `o`보다 **작음**.
  - 0: 현재 객체가 `o`와 **같음**.
  - 양수 값: 현재 객체가 `o`보다 **큼**.

### `Comparable` 인터페이스 구현 예시

예를 들어, `Person` 객체를 나이순으로 정렬하는 예시를 만들어 보겠습니다.

```java
class Person implements Comparable<Person> {
    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // 나이 기준으로 비교
    @Override
    public int compareTo(Person other) {
        return Integer.compare(this.age, other.age);
    }

    @Override
    public String toString() {
        return name + " (" + age + ")";
    }
}
```

`compareTo` 메서드는 두 `Person` 객체의 나이를 비교하고, 이를 기반으로 순서를 정합니다.

### 사용 예시

```java
import java.util.Arrays;

public class ComparableExample {
    public static void main(String[] args) {
        Person[] people = {
            new Person("Alice", 30),
            new Person("Bob", 25),
            new Person("Charlie", 35)
        };

        // Comparable 구현에 따라 배열 정렬
        Arrays.sort(people);

        // 결과 출력
        for (Person person : people) {
            System.out.println(person);
        }
    }
}
```

이 코드를 실행하면 `Person` 객체가 나이순으로 정렬됩니다.
```
Bob (25)
Alice (30)
Charlie (35)
```

### 주요 개념 정리

1. **자연 순서 정의**: `Comparable`을 구현하는 클래스는 객체 간의 기본 비교 방법을 제공하며, 이를 **자연 순서**라고 합니다.
   - 예: `String` 클래스는 알파벳 순서, `Integer` 클래스는 숫자 크기에 따라 자연 순서가 정의됩니다.
   
2. **`compareTo` 메서드**: 객체 간 비교를 수행하며, **음수, 0, 양수**로 결과를 반환하여 상대적인 크기를 결정합니다.

3. **정렬 메서드에서 사용**: `Arrays.sort()` 또는 `Collections.sort()`와 같은 정렬 메서드는 `Comparable`을 구현한 객체 배열이나 리스트를 정렬할 수 있습니다.

### `Comparable`과 `Comparator`의 차이

- **`Comparable`**: 클래스 자체에 비교 로직을 포함시킵니다. 객체의 **기본 정렬 기준**을 제공하며, 한 가지 정렬 방법만 가능.
- **`Comparator`**: 별도의 비교 로직을 제공합니다. 여러 기준으로 정렬하고자 할 때 유용합니다. 즉, 특정 기준에 따라 객체를 정렬하고 싶을 때 외부에서 비교 방법을 정의합니다.