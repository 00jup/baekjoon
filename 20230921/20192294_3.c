#include <stdio.h>

int main()
{

    double exchangeRate, won;
    double dollar;
    printf("환율을 입력하시오: ");
    scanf("%lf", &exchangeRate);

    printf("원화 금액을 입력하시오: ");
    scanf("%lf", &won);

    dollar = won / exchangeRate;
    printf("원화 %.0lf원은 %lf달러입니다.\n", won, dollar);
}