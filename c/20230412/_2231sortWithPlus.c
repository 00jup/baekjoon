#include <stdio.h>
#include <stdbool.h>
#include <string.h>

int main()
{
  int N;
  scanf("%d", &N);
  int M, sum, start, digit = 0;
  int temp;
  int i;
  bool isRight = true;
  while (N)
  {
    N /= 10;
    digit++;
  }
  start = N - (9 * digit);

  for (i = start; i < N; i++)
  {
    temp = start;
    sum = start;
    while (temp > 0)
    {
      sum += (temp % 10);
      temp /= 10;
    }
    if (sum == N)
    {
      printf("%d\n", sum);
      isRight = true;
      break;
    }
    isRight = false;
  }
  if (isRight == false)
    printf("0\n");
  else if (isRight == true)
    printf("%d", sum);
}