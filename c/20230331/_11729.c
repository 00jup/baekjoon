#include <stdio.h>
#include <math.h>

int hanoi_tower(int n, char from, char tmp, char to)
{
  if (n == 1)
    printf("%c %c\n", from, to);
  else
  {
    hanoi_tower(n - 1, from, to, tmp);
    printf("%c %c\n", from, to);
    hanoi_tower(n - 1, tmp, from, to);
  }
  /// K += 1;
}
int main()
{
  int N;
  double K;
  scanf("%d", &N);
  K = N;
  printf("%d\n", ((int)pow(2.0, K) - 1));
  hanoi_tower(N, '1', '2', '3');
  // printf("\n%d\n", A);
}