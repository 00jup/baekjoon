#include <stdio.h>

int main()
{
    double num1, num2, num3;
    double sum, average;

    printf("3개의 실수를 입력하시오: ");
    scanf("%lf %lf %lf", &num1, &num2, &num3);

    sum = num1 + num2 + num3;
    average = (num1 + num2 + num3) / 3;

    printf("합계=%.2lf\n", sum);
    printf("평균=%.2lf\n", average);
}