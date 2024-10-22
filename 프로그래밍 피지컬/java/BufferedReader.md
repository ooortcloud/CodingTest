Java의 BufferedReader 클래스는 문자 입력 스트림으로부터 텍스트를 효율적으로 읽는 데 사용됩니다. 주로 파일이나 콘솔에서 입력을 읽을 때 사용합니다. BufferedReader의 기본적인 사용법을 설명해 드리겠습니다.

1. BufferedReader 객체 생성:

```java
import java.io.*;

BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
```

이 코드는 콘솔 입력을 위한 BufferedReader를 생성합니다.

2. 파일에서 읽기:

```java
BufferedReader br = new BufferedReader(new FileReader("filename.txt"));
```

3. 한 줄 읽기:

```java
String line = br.readLine();
```

4. 여러 줄 읽기:

```java
String line;
while ((line = br.readLine()) != null) {
    System.out.println(line);
}
```

5. 숫자 읽기:

```java
int n = Integer.parseInt(br.readLine());
```

6. 공백으로 구분된 입력 처리:

```java
String[] parts = br.readLine().split(" ");
```

7. 사용 후 닫기:

```java
br.close();
```

8. 전체 예제:

```java
import java.io.*;

public class BufferedReaderExample {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        System.out.print("이름을 입력하세요: ");
        String name = br.readLine();

        System.out.print("나이를 입력하세요: ");
        int age = Integer.parseInt(br.readLine());

        System.out.println("이름: " + name);
        System.out.println("나이: " + age);

        br.close();
    }
}
```

주의사항:
- BufferedReader는 checked exception인 IOException을 던질 수 있으므로, 이를 처리해야 합니다.
- 리소스 관리를 위해 사용 후 반드시 close() 메소드를 호출해야 합니다. try-with-resources 문을 사용하면 자동으로 닫을 수 있습니다.

BufferedReader는 대량의 텍스트를 읽을 때 효율적이며, 특히 입력 성능이 중요한 경우에 유용합니다.