Java의 Arrays 클래스는 배열을 다루는 데 유용한 여러 정적 메소드를 제공합니다. 주요 메소드와 사용법을 소개해 드리겠습니다.

1. 배열 정렬:

```java
int[] numbers = {5, 2, 8, 1, 9};
Arrays.sort(numbers);
// 결과: [1, 2, 5, 8, 9]

// 부분 정렬
Arrays.sort(numbers, 1, 4); // 인덱스 1부터 3까지만 정렬
```

2. 배열 검색:

```java
int[] numbers = {1, 2, 5, 8, 9};
int index = Arrays.binarySearch(numbers, 5);
// 결과: 2 (정렬된 배열에서만 사용 가능)
```

3. 배열 채우기:

```java
int[] numbers = new int[5];
Arrays.fill(numbers, 10);
// 결과: [10, 10, 10, 10, 10]

// 부분 채우기
Arrays.fill(numbers, 1, 4, 20);
// 결과: [10, 20, 20, 20, 10]
```

4. 배열 비교:

```java
int[] array1 = {1, 2, 3};
int[] array2 = {1, 2, 3};
boolean isEqual = Arrays.equals(array1, array2);
// 결과: true
```

5. 배열 복사:

```java
int[] original = {1, 2, 3, 4, 5};
int[] copy = Arrays.copyOf(original, 7);
// 결과: [1, 2, 3, 4, 5, 0, 0]

int[] partialCopy = Arrays.copyOfRange(original, 1, 4);
// 결과: [2, 3, 4]
```

6. 배열을 List로 변환:

```java
String[] array = {"apple", "banana", "orange"};
List<String> list = Arrays.asList(array);
```

7. 배열 출력:

```java
int[] numbers = {1, 2, 3, 4, 5};
System.out.println(Arrays.toString(numbers));
// 출력: [1, 2, 3, 4, 5]

int[][] matrix = {{1, 2}, {3, 4}};
System.out.println(Arrays.deepToString(matrix));
// 출력: [[1, 2], [3, 4]]
```

8. 배열 스트림 생성:

```java
int[] numbers = {1, 2, 3, 4, 5};
IntStream stream = Arrays.stream(numbers);
```

9. 병렬 정렬:

```java
int[] largeArray = new int[10000];
// 배열 채우기
Arrays.parallelSort(largeArray);
```

10. 배열 해시코드:

```java
int[] numbers = {1, 2, 3, 4, 5};
int hashCode = Arrays.hashCode(numbers);
```

11. 다차원 배열 비교:

```java
int[][] array1 = {{1, 2}, {3, 4}};
int[][] array2 = {{1, 2}, {3, 4}};
boolean isEqual = Arrays.deepEquals(array1, array2);
// 결과: true
```

사용 예제:

```java
import java.util.Arrays;

public class ArraysExample {
    public static void main(String[] args) {
        int[] numbers = {5, 2, 8, 1, 9};
        
        System.out.println("원본 배열: " + Arrays.toString(numbers));
        
        Arrays.sort(numbers);
        System.out.println("정렬 후: " + Arrays.toString(numbers));
        
        int searchResult = Arrays.binarySearch(numbers, 8);
        System.out.println("8의 인덱스: " + searchResult);
        
        int[] copy = Arrays.copyOf(numbers, numbers.length);
        System.out.println("복사된 배열: " + Arrays.toString(copy));
        
        System.out.println("원본과 복사본 동일: " + Arrays.equals(numbers, copy));
    }
}
```

Arrays 클래스는 배열 조작에 매우 유용하며, 특히 정렬, 검색, 복사 등의 작업을 효율적으로 수행할 수 있게 해줍니다.