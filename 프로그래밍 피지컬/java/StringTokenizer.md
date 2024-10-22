StringTokenizer는 Java에서 문자열을 특정 구분자(delimiter)를 기준으로 토큰화하는 데 사용되는 클래스입니다. 주로 입력 문자열을 파싱할 때 유용합니다. StringTokenizer의 기본적인 사용법을 설명해 드리겠습니다.

1. StringTokenizer 객체 생성:

```java
import java.util.StringTokenizer;

// 기본 구분자(공백)를 사용하는 경우
StringTokenizer st = new StringTokenizer("Hello World Java");

// 특정 구분자를 지정하는 경우
StringTokenizer st = new StringTokenizer("apple,banana,grape", ",");
```

2. 토큰 개수 확인:

```java
int tokenCount = st.countTokens();
```

3. 다음 토큰 확인 및 가져오기:

```java
while (st.hasMoreTokens()) {
    String token = st.nextToken();
    System.out.println(token);
}
```

4. 특정 타입으로 토큰 변환:

```java
int number = Integer.parseInt(st.nextToken());
```

5. 전체 예제:

```java
import java.util.StringTokenizer;

public class StringTokenizerExample {
    public static void main(String[] args) {
        String input = "1 2 3 4 5";
        StringTokenizer st = new StringTokenizer(input);

        System.out.println("토큰 수: " + st.countTokens());

        int sum = 0;
        while (st.hasMoreTokens()) {
            int num = Integer.parseInt(st.nextToken());
            sum += num;
        }

        System.out.println("합계: " + sum);
    }
}
```

6. 여러 구분자 사용:

```java
StringTokenizer st = new StringTokenizer("apple,banana;grape:orange", ",;:");
```

7. 구분자도 토큰으로 처리:

```java
StringTokenizer st = new StringTokenizer("key=value", "=", true);
```

주의사항:
- StringTokenizer는 빈 토큰을 무시합니다. 예를 들어, "a,,b"를 ','로 분리하면 "a"와 "b" 두 개의 토큰만 생성됩니다.
- Java 5 이후부터는 String 클래스의 split() 메소드나 정규표현식을 사용하는 것이 더 유연하고 강력할 수 있습니다.
- StringTokenizer는 동기화되지 않으므로 멀티스레드 환경에서 사용시 주의가 필요합니다.

StringTokenizer는 간단한 문자열 파싱 작업에 유용하지만, 더 복잡한 파싱 작업이나 정규표현식이 필요한 경우에는 다른 방법을 고려해 볼 수 있습니다.