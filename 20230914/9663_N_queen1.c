#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, i, j;

    scanf("%d", &n);
    int **chess = (int **)malloc(n * sizeof(int *));
    for (i = 0; i < n; i++)
    {
        chess[i] = (int *)malloc(n * sizeof(int));
    }

    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            scanf("%d", &chess[i][j]);
            while (chess[i][j] != 0 && chess[i][j] != 1)
            {
                scanf("%d", &chess[i][j]);
            }
        }
    }

    printf("\n");
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            printf("%d ", chess[i][j]);
        }
        printf("\n");
    }
}