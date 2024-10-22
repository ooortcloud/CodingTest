Java의 Math 클래스는 수학적 연산을 수행하는 다양한 정적 메소드를 제공합니다. 주요 메소드들과 사용법을 소개해 드리겠습니다.

1. 기본 연산:

```java
Math.abs(-10);           // 절대값: 10
Math.max(5, 10);         // 최대값: 10
Math.min(5, 10);         // 최소값: 5
Math.pow(2, 3);          // 거듭제곱: 8.0 (2의 3승)
Math.sqrt(16);           // 제곱근: 4.0
Math.cbrt(27);           // 세제곱근: 3.0
```

2. 올림, 내림, 반올림:

```java
Math.ceil(4.3);          // 올림: 5.0
Math.floor(4.7);         // 내림: 4.0
Math.round(4.5);         // 반올림: 5
```

3. 삼각함수:

```java
Math.sin(Math.PI / 2);   // 사인
Math.cos(0);             // 코사인
Math.tan(Math.PI / 4);   // 탄젠트
Math.asin(1);            // 아크사인
Math.acos(0);            // 아크코사인
Math.atan(1);            // 아크탄젠트
```

4. 로그함수:

```java
Math.log(Math.E);        // 자연로그
Math.log10(100);         // 밑이 10인 로그
```

5. 지수와 로그:

```java
Math.exp(1);             // e의 1승
Math.expm1(1);           // e의 1승 - 1 (더 정확한 계산)
Math.log1p(1);           // ln(1+1) (더 정확한 계산)
```

6. 각도 변환:

```java
Math.toDegrees(Math.PI); // 라디안을 도(degree)로: 180.0
Math.toRadians(180);     // 도를 라디안으로: π
```

7. 난수 생성:

```java
Math.random();           // 0.0 이상 1.0 미만의 난수
```

8. 상수:

```java
Math.PI;                 // π (원주율)
Math.E;                  // e (자연로그의 밑)
```

9. 활용 예제:

```java
public class MathExample {
    public static void main(String[] args) {
        // 원의 넓이 계산
        double radius = 5;
        double area = Math.PI * Math.pow(radius, 2);
        System.out.println("원의 넓이: " + area);

        // 삼각형의 빗변 길이 계산 (피타고라스 정리)
        double a = 3, b = 4;
        double c = Math.sqrt(Math.pow(a, 2) + Math.pow(b, 2));
        System.out.println("빗변의 길이: " + c);

        // 난수를 이용한 주사위 굴리기
        int diceRoll = (int)(Math.random() * 6) + 1;
        System.out.println("주사위 결과: " + diceRoll);
    }
}
```

Math 클래스의 모든 메소드는 정적(static)이므로 객체 생성 없이 직접 호출할 수 있습니다. 또한, 대부분의 메소드는 double 형을 반환하므로 필요에 따라 형변환을 해야 할 수 있습니다.