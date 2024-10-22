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

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    // 나이 기준으로 비교
    @Override
    public int compareTo(Person other) {
        // Integer의 compare() 메소드는 '첫 번째 인자 - 두 번째 인자' 값이 반환된다고 보면 된다. (이 경우 최소 힙으로 동작함)
        // 만약 두 인자 순서를 바꿔서 입력하면 최대 힙으로 구현 가능하다.
        return Integer.compare(this.age, other.getAge());
    }

    @Override
    public String toString() {
        return name + " (" + age + ")";
    }
}
```

`compareTo` 메서드는 두 `Person` 객체의 나이를 비교하고, 이를 기반으로 순서를 정합니다.

만약 이름에 대해 사전순으로 비교하고자 한다면 String.compareTo() 메소드를 활용해주면 된다. 다만 이 경우 **String에서 구현된 compareTo()를 호출하는 것이기 때문에, 해당 사항을 명시하기 위해 'this' 키워드를 사용하여 비교해줘야 한다.**

```java
class Person implements Comparable<Person> {
    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    // 이름 사전순으로 비교
    @Override
    public int compareTo(Person other) {
        return this.name.compareTo(other.getName());
    }

    @Override
    public String toString() {
        return name + " (" + age + ")";
    }
}
```

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

Arrays(배열인 경우) 또는 Collections(컬렉션 객체의 경우) 클래스의 'sort()' 메소드를 사용해주면, 해당 객체에 대해 Comparable의 compareTo() 메소드를 구현한 것에 따라 정렬된다.

### 만약 첫 번째 비교 인자가 서로 같다면?

파이썬의 heapq 라이브러리에서는 내부적으로 알아서 그 다음 인자에 대한 비교 연산에 들어간다. 하지만 Java는 다 직접 구현해줘야 한다. 그래도 이 특성은 우선순위 비교가 까다로운 상황의 경우에는 오히려 장점이 될 수 있다. 예를 들어 첫 번째 인자는 최소 힙 그리고 두 번째 인자는 최대 힙 형식으로 작동시켜야 한다면 파이썬에서는 별도의 조치를 취해야 하겠지만, Java에서는 애초에 compareTo() 메소드를 커스텀 오버라이딩을 해야 하다 보니 개발자가 직접 매 경우의 수마다 커스텀하게 우선 순위 기준 부여가 가능하기 때문이다.

```java
class Person implements Comparable<Person> {

    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    @Override
    public int compareTo(Person o) {

        // 나이가 같은 경우 이름을 사전순으로 비교
        if (age == o.getAge())
            return this.name.compareTo(name, o.getName());
        else
            return Integer.compare(this.age, o.getAge())
    }

}
```