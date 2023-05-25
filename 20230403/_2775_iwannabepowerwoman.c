#include <stdio.h>
#include <stdlib.h>

int count_home(int k, int n)
{
  int count = 0;
  if (k == 0)
  {
    return n;
  }
  else
  {
    for (int i = 0; i < n; i++)
    {
      count += count_home(k - 1, i);
    }
  }
}

int main()
{
  int T, cnt = 0;
  // int *k = (int *)malloc(sizeof(int));
  // int *n = (int *)malloc(sizeof(int));

  scanf("%d", &T);
  int *k = (int *)malloc(sizeof(int) * T);
  int *n = (int *)malloc(sizeof(int) * T);

  for (int i = 0; i < T; i++)
  {
    scanf("%d", &k[i]);
    scanf("%d", &n[i]);
  }
  for (int i = 0; i < T; i++)
  {
    printf("%d\n", count_home(k[i], n[i]));
  }
}