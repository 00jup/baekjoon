#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    int n, i, j;

    // 난수 생성을 위한 seed 설정.
    // time(NULL)을 사용하여 현재 시간을 기반으로 seed를 초기화하여 무작위성을 확보한다.
    srand((unsigned int)time(NULL));

    // 사용자로부터 배열의 크기인 n을 입력받는다.
    printf("Enter the size of the array (n x n): ");
    scanf("%d", &n);

    // n x n 크기의 2차원 배열을 동적 할당한다.
    // 이때 array는 int 포인터의 포인터로 선언되며, 각 포인터는 int 포인터를 가리킨다.
    int **array = (int **)malloc(n * sizeof(int *));
    for (i = 0; i < n; i++)
    {
        array[i] = (int *)malloc(n * sizeof(int));
    }

    // 각 배열 요소에 0 또는 1을 무작위로 할당하고 화면에 출력한다.
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            array[i][j] = rand() % 2; // 0 또는 1 중 하나의 값을 무작위로 선택
            printf("%d ", array[i][j]);
        }
        printf("\n");
    }

    // 동적 할당한 메모리를 해제한다.
    // 이는 메모리 누수를 방지하기 위해 필요하다.
    for (i = 0; i < n; i++)
    {
        free(array[i]);
    }
    free(array);

    return 0;
}
