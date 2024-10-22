Java에서 `Scanner` 클래스는 다양한 데이터 타입의 입력을 쉽게 받을 수 있는 도구입니다. `Scanner`는 파일, 문자열, 키보드 입력 등 다양한 입력 소스에서 데이터를 읽어올 수 있습니다.

### 1. `Scanner` 객체 생성
`Scanner`를 사용하려면 먼저 `java.util.Scanner` 패키지를 import하고 `Scanner` 객체를 생성해야 합니다.

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); // 키보드 입력을 받기 위한 Scanner 객체 생성
    }
}
```

### 2. 다양한 데이터 타입 입력받기
`Scanner`는 다양한 메서드를 제공하여 다양한 데이터 타입의 입력을 받을 수 있습니다.

- **문자열 입력 (`nextLine`과 `next`)**
  - `nextLine()`: 한 줄 전체를 입력받습니다. 사용자가 엔터를 누를 때까지 모든 문자열을 포함합니다.
  - `next()`: 공백(스페이스, 탭, 줄바꿈 등) 전까지의 문자열을 입력받습니다.

  ```java
  System.out.print("문자열 입력 (nextLine): ");
  String line = scanner.nextLine();

  System.out.print("문자열 입력 (next): ");
  String word = scanner.next();
  ```

- **정수 입력 (`nextInt`)**
  - 정수를 입력받을 때 사용합니다.

  ```java
  System.out.print("정수 입력: ");
  int number = scanner.nextInt();
  ```

- **실수 입력 (`nextDouble`)**
  - 실수를 입력받을 때 사용합니다.

  ```java
  System.out.print("실수 입력: ");
  double d = scanner.nextDouble();
  ```

- **논리값 입력 (`nextBoolean`)**
  - `true` 또는 `false` 값을 입력받을 때 사용합니다.

  ```java
  System.out.print("논리값 입력 (true/false): ");
  boolean bool = scanner.nextBoolean();
  ```

### 3. 입력된 값의 유효성 검사
사용자가 올바른 타입의 데이터를 입력하지 않으면 예외(`InputMismatchException`)가 발생할 수 있습니다. 이를 처리하기 위해 `try-catch` 블록을 사용할 수 있습니다.

```java
try {
    System.out.print("정수 입력: ");
    int number = scanner.nextInt();
} catch (InputMismatchException e) {
    System.out.println("잘못된 입력입니다. 정수를 입력하세요.");
}
```

### 4. 다양한 입력 소스
`Scanner`는 키보드 입력 외에도 문자열, 파일 등 다양한 입력 소스에서 데이터를 읽을 수 있습니다.

- **문자열에서 입력받기**

  ```java
  String input = "Hello 123 45.67 true";
  Scanner stringScanner = new Scanner(input);

  String text = stringScanner.next(); // "Hello"
  int num = stringScanner.nextInt(); // 123
  double floatingNum = stringScanner.nextDouble(); // 45.67
  boolean bool = stringScanner.nextBoolean(); // true
  ```

- **파일에서 입력받기**

  ```java
  import java.io.File;
  import java.io.FileNotFoundException;

  public class Main {
      public static void main(String[] args) {
          try {
              Scanner fileScanner = new Scanner(new File("input.txt"));

              while (fileScanner.hasNextLine()) {
                  String line = fileScanner.nextLine();
                  System.out.println(line);
              }

              fileScanner.close();
          } catch (FileNotFoundException e) {
              System.out.println("파일을 찾을 수 없습니다.");
          }
      }
  }
  ```

### 5. 입력 반복 처리
입력을 반복해서 받기 위해서는 `while`이나 `do-while` 루프를 사용할 수 있습니다. 예를 들어, 사용자가 종료 조건을 입력할 때까지 데이터를 반복해서 받을 수 있습니다.

```java
String input;
do {
    System.out.print("명령어를 입력하세요 (종료하려면 'exit'): ");
    input = scanner.nextLine();
    System.out.println("입력한 명령어: " + input);
} while (!input.equals("exit"));
```

### 6. `Scanner` 닫기
`Scanner` 객체를 더 이상 사용하지 않을 때는 `close()` 메서드를 호출하여 자원을 해제해야 합니다.

```java
scanner.close();
```
