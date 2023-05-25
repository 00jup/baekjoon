#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define col 50

int compare(const void *first, const void *second)
{
  if (*(int *)first > *(int *)second)
    return 1;
}

int main()
{
  int N;
  double K;
  scanf("%d", &N);
  char str[][];
  char **p;
  str char result[N][col];
  char temp[col];

  for (int i = 0; i < N; i++)
    scanf("%s", str[i]);

  qsort(str, N, sizeof(str[0]), compare);
  for (int i = 0; i < N; i++)
}