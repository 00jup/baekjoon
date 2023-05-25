#include <stdio.h>

int main()
{
  int num1 = 1;
  int *p = &num1;
  int x;
  x = *p++;
  printf("x = %d, p = %p\n", x, p);

  x = *++p;
  printf("x = %d, p = %p\n", x, p);

  x = *--p;
  printf("x = %d, p = %p\n", x, p);

  x = (*p)++;
  printf("x = %d, p = %p\n", x, p);
}