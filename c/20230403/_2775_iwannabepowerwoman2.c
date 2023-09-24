#include <stdio.h>
#include <stdlib.h>

int c_h(int k, int n)
{
  if (n == 1)
    return 1;
  if (k == 0)
    return n;
  return (c_h(k - 1, n) + c_h(k, n - 1));
}
int main()
{

  int result, T;

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
    printf("%d\n", c_h(k[i], n[i]));
  }
}
// result = c_h(k, n);