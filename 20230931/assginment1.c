#include <stdio.h>

int main()
{
    float x = 1e39;
    printf("double double size %lu\n", sizeof(long double));
    printf("double double size %lu\n", sizeof(double));

    printf("%f\n", 0.123456789);
    printf("%e\n", 0.123456789);
    printf("%lf\n", 0.123456789);
    printf("x = %e\n", x); // inf 나와야 함

    float value = 0.1;

    printf("%.20f\n", value);

    double y;
    y = (1.0e20 + 50) - 1.0e20;
    printf("%f\n", y);

    // 소리 나오도록
    char beep = 7;
    printf("%c", beep);

    char beef = '\a';
    printf("%c", beef);

    int id, pass;
    printf("아이디와 패스워드를 4개의 숫자로 입력\n");
    printf("id: ____\b\b\b\b");
    scanf("%d", &id);
    printf("pass: ____\b\b\b\b");
    scanf("%d", &pass);
    printf("\a입력된 아이디는 %d 패스워드는 %d\n", id, pass);

    return 0;
}

// printf(num); <- c에서 이런 거 하지마셈