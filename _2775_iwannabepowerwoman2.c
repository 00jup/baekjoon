#include <stdio.h>

int count_home(int k, int n)
{
  if (n == 1)
    return 1;
  if (k == 0)
    return n;
  return (count_home(k - 1, n) + count_home(k, n - 1));
}
int main()
{
  int k, n;
  int result;

  scanf("%d %d", &k, &n);

  result = count_home(k, n);
  printf("%d\n\n", count_home(k, n));
}