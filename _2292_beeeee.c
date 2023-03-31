#include <stdio.h>

int main()
{
  int N, cnt = 1;
  int sum = 1;
  scanf("%d", &N);
  while (N > sum)
  {
    sum = sum + cnt * 6;
    cnt++;
    }
  printf("%d\n", cnt);
}