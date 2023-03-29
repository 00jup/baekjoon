#include <stdio.h>

int main()
{

  int N, M;
  scanf("%d %d", &N, &M);
  char chess[N][M];
  for (int i = 0; i < N; i++)
  {
    scanf("%s", chess[i]);
  } 
  // char chess[50];
  // scanf("%s", chess);

  printf("\n\n\n");
  printf("%s\n\n", chess[0]);
  printf("%s\n\n", *chess);
  printf("%s\n\n", chess[1]);
  // printf("%s\n\n", *(++chess);
  printf("%s\n\n", *(chess + 1));
  printf("%u\n\n`", &chess[0]);
  printf("%c\n\n", chess[0]);
}