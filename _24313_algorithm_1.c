#include <stdio.h>

int main()
{
  int a1, a0, c, n0;
  scanf("%d %d", &a1, &a0);
  scanf("%d", &c);
  scanf("%d", &n0);
  if (a1 * n0 + a0 <= c * n0 && c - a1 >= 0)
    printf("1\n");
  else
    printf("0\n");
}
