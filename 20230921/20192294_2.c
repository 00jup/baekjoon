#include <stdio.h>

int main()
{
    double w, h, area, perimeter;
    printf("사각형의 높이(H): ");
    scanf("%lf", &h);
    printf("사각형의 넓이(W): ");
    scanf("%lf", &w);

    area = w * h;
    perimeter = 2 * (w + h);

    printf("사각형의 둘레 = %.1lf\n", perimeter);
    printf("사각형의 면적 = %.2lf\n", area);
}