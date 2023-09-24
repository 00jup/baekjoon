#include <stdio.h>

int main()
{
    double velocity, distance, time;

    printf("빛의 속도는 ");
    scanf("%lf km/s", &velocity);

    printf("태양과 지구와의 거리 ");
    scanf("%lf km", &distance);

    time = distance / velocity;

    printf("도달 시간은 %lf초\n", time);
}