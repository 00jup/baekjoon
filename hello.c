#include <stdio.h>

#define square(x) ((x) * (x) * (x) * (x) * (x))

int main()
{

  int n;
  scanf("%d", &n);
  n = square(n);
  printf("%d", n);
  printf("Hello world\n");
}
