Java의 `Collections` 클래스는 **컬렉션(Collection)**을 조작하는 다양한 정적 메서드를 제공합니다. 이 클래스는 컬렉션을 정렬, 검색, 변환 및 동기화하는 데 매우 유용합니다. `Collections` 클래스는 일반적으로 `java.util.List`, `java.util.Set`, `java.util.Map` 등의 컬렉션 타입과 함께 사용됩니다.

### 주요 메서드 및 사용법 정리

### 1. 정렬 (Sorting)

#### 1.1 `Collections.sort(List<T>)`
- **설명**: 리스트를 **자연 순서(오름차순)**로 정렬합니다. `List`의 요소가 `Comparable` 인터페이스를 구현하고 있어야 합니다.
- **예시**:
```java
import java.util.Collections;
import java.util.List;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        List<Integer> numbers = new ArrayList<>();
        numbers.add(5);
        numbers.add(3);
        numbers.add(10);
        
        Collections.sort(numbers);
        System.out.println(numbers);  // [3, 5, 10]
    }
}
```

#### 1.2 `Collections.sort(List<T>, Comparator<? super T>)`
- **설명**: 사용자 정의 **Comparator**로 리스트를 정렬합니다.
- **예시**:
```java
import java.util.Collections;
import java.util.List;
import java.util.ArrayList;
import java.util.Comparator;

public class Main {
    public static void main(String[] args) {
        List<Integer> numbers = new ArrayList<>();
        numbers.add(5);
        numbers.add(3);
        numbers.add(10);
        
        // 내림차순 정렬
        Collections.sort(numbers, Comparator.reverseOrder());
        System.out.println(numbers);  // [10, 5, 3]
    }
}
```

Comparable을 구현한 객체에 대해 정렬 기준을 변경하고자 하는 경우, 다음과 같이 overwrite를 시켜서 변경시킬 수 있다.
```java
Collections.sort(result, new Comparator<Food>() { 
    @Override
    public int compare(Food a, Food b) {
        return Integer.compare(a.getIndex(), b.getIndex());
    }
});
```

### 2. 검색 (Searching)

#### 2.1 `Collections.binarySearch(List<T>, T)`
- **설명**: 정렬된 리스트에서 이진 탐색을 수행해 **특정 요소의 인덱스**를 반환합니다. 리스트는 반드시 정렬되어 있어야 합니다.
- **예시**:
```java
import java.util.Collections;
import java.util.List;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        List<Integer> numbers = new ArrayList<>();
        numbers.add(3);
        numbers.add(5);
        numbers.add(10);
        
        // 정렬된 리스트에서 이진 탐색
        int index = Collections.binarySearch(numbers, 5);
        System.out.println(index);  // 1 (5의 인덱스)
    }
}
```

### 3. 동기화 (Synchronization)

#### 3.1 `Collections.synchronizedList(List<T>)`
- **설명**: 스레드에 안전한 동기화된 리스트를 생성합니다.
- **예시**:
```java
import java.util.Collections;
import java.util.List;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        List<Integer> list = new ArrayList<>();
        List<Integer> syncList = Collections.synchronizedList(list);
        
        syncList.add(1);
        syncList.add(2);
        
        synchronized (syncList) {
            for (int num : syncList) {
                System.out.println(num);  // 1, 2
            }
        }
    }
}
```
- **주의**: 동기화된 컬렉션을 반복할 때는 **외부에서 동기화 블록을 명시적으로 사용**해야 합니다.

#### 3.2 `Collections.synchronizedMap(Map<K, V>)`, `Collections.synchronizedSet(Set<T>)`
- **설명**: 스레드에 안전한 동기화된 `Map`, `Set`을 생성할 수 있습니다.
  
### 4. 불변 컬렉션 (Unmodifiable Collection)

#### 4.1 `Collections.unmodifiableList(List<T>)`
- **설명**: 변경할 수 없는 리스트를 반환합니다. 불변 리스트는 **추가, 삭제, 수정**이 불가능합니다.
- **예시**:
```java
import java.util.Collections;
import java.util.List;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        List<String> list = new ArrayList<>();
        list.add("A");
        list.add("B");
        
        List<String> unmodifiableList = Collections.unmodifiableList(list);
        System.out.println(unmodifiableList);  // [A, B]
        
        // unmodifiableList.add("C");  // UnsupportedOperationException 발생
    }
}
```

#### 4.2 `Collections.unmodifiableMap(Map<K, V>)`, `Collections.unmodifiableSet(Set<T>)`
- **설명**: 불변 Map과 Set도 유사하게 만들 수 있습니다.

### 5. 최소값/최대값 (Min/Max)

#### 5.1 `Collections.min(Collection<T>)`
- **설명**: 컬렉션에서 **최소값**을 반환합니다. 요소는 `Comparable` 인터페이스를 구현해야 합니다.
- **예시**:
```java
import java.util.Collections;
import java.util.List;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        List<Integer> numbers = new ArrayList<>();
        numbers.add(5);
        numbers.add(3);
        numbers.add(10);
        
        int min = Collections.min(numbers);
        System.out.println(min);  // 3
    }
}
```

#### 5.2 `Collections.max(Collection<T>)`
- **설명**: 컬렉션에서 **최대값**을 반환합니다.
- **예시**:
```java
import java.util.Collections;
import java.util.List;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        List<Integer> numbers = new ArrayList<>();
        numbers.add(5);
        numbers.add(3);
        numbers.add(10);
        
        int max = Collections.max(numbers);
        System.out.println(max);  // 10
    }
}
```

### 6. 요소 채우기 (Filling Elements)

#### 6.1 `Collections.fill(List<T>, T)`
- **설명**: 리스트의 모든 요소를 주어진 값으로 **채웁니다**.
- **예시**:
```java
import java.util.Collections;
import java.util.List;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        List<String> list = new ArrayList<>();
        list.add("A");
        list.add("B");
        list.add("C");
        
        Collections.fill(list, "X");
        System.out.println(list);  // [X, X, X]
    }
}
```

### 7. 교체 (Replace)

#### 7.1 `Collections.replaceAll(List<T>, T oldVal, T newVal)`
- **설명**: 리스트에서 특정 값을 새로운 값으로 **교체**합니다.
- **예시**:
```java
import java.util.Collections;
import java.util.List;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        List<String> list = new ArrayList<>();
        list.add("A");
        list.add("B");
        list.add("A");
        
        Collections.replaceAll(list, "A", "X");
        System.out.println(list);  // [X, B, X]
    }
}
```

### 8. 역순 (Reversing)

#### 8.1 `Collections.reverse(List<T>)`
- **설명**: 리스트의 요소들을 **역순**으로 만듭니다.
- **예시**:
```java
import java.util.Collections;
import java.util.List;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        List<Integer> numbers = new ArrayList<>();
        numbers.add(1);
        numbers.add(2);
        numbers.add(3);
        
        Collections.reverse(numbers);
        System.out.println(numbers);  // [3, 2, 1]
    }
}
```

### 9. 빈 컬렉션 (Empty Collections)

#### 9.1 `Collections.emptyList()`, `Collections.emptySet()`, `Collections.emptyMap()`
- **설명**: **비어 있는 불변**의 리스트, 집합, 맵을 반환합니다. 주로 **초기화**나 **예외 처리**에 사용됩니다.
- **예시**:
```java
import java.util.Collections;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<String> emptyList = Collections.emptyList();
        System.out.println(emptyList);  // []
    }
}
```

### 10. 기타 유용한 메서드

#### 10.1 `Collections.copy(List<? super T> dest, List<? extends T> src)`
- **설명**: 한 리스트의 내용을 다른 리스트에 **복사**합니다.
- **예시**:
```java
import java.util.Collections;
import java.util.List;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        List<String> src = new ArrayList<>();
        src.add("A");
        src.add("B");
        
        List<String> dest = new ArrayList<>(src.size());
        Collections.addAll(dest, new String[src.size()]);  // 크기 확보
        Collections.copy(dest, src);
        
        System.out.println(dest);  // [A, B]
    }
}
```

#### 10.2 `Collections.shuffle(List<T>)`
- **설명**: 리스트의 요소를 **무작위로 섞습니다**.
- **예시**:
```java
import java.util.Collections;
import java.util.List;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        List<Integer> numbers = new ArrayList<>();
        numbers.add(1);
        numbers.add(2);
        numbers.add(3);
        
        Collections.shuffle(numbers);
        System.out.println(numbers);  // [무작위 순서]
    }
}
```

### 정리
- `Collections` 클래스는 정렬, 검색, 동기화, 불변 컬렉션 생성 등 **컬렉션을 조작**하는 다양한 유틸리티 메서드를 제공합니다.
- 주로 `List`, `Set`, `Map` 등의 컬렉션과 함께 사용되며, 여러 컬렉션 작업을 간편하게 할 수 있습니다.