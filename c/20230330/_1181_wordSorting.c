#include <stdio.h>
#include <string.h>
#define col 50
int main()
{
  int N;
  double K;
  scanf("%d", &N);
  char str[N][col];
  char result[N][col];
  char temp[col];
  for (int i = 0; i < N; i++)
    scanf("%s", str[i]);

  for (int j = 0; j < N; j++)
  {
    for (int k = j + 1; k < N; k++)
    {
      printf("%d\n", (int)strlen(str[j]));
      if ((int)strlen(str[j]) < (int)strlen(str[k]))
      {
        strcpy(temp, result[j]);
        strcpy(result[j], str[k]);
        strcpy(str[k], temp);
        printf("%s \n", result[k]);
      }
    }
  }
  // for (int i = 0; i < N; i++)
  //  printf("%s ", result[i]);
  //  printf("\n");
  //  str[j] + 1;?
}