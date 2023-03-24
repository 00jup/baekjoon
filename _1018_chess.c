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
}