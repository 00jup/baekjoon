#include <stdio.h>

struct str_size
{
  char a[10];
  int b[4];
  char c;
  int d;
  double e;
  char f;
};
int main()
{
  struct str_size p_1;
  printf("% d \n", sizeof(p_1));
  return 0;
}
