#include <stdio.h>

int main()
{
  int array[9], count, max;
  for (int i = 0; i < 9; i++)
  {
    scanf("%d", &array[i]);
  }
  max = array[0];
  for (int j = 0; j < 9; j++)
  {
    if (max < array[j])
    {
      max = array[j];
      count = j;
    }
  }
  printf("%d\n", max);
  printf("%d\n", count + 1);
}