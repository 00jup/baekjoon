#include <stdio.h>

void input(int N, int M, int Mat[][M])
{
  for (int i = 0; i < N; i++)
  {
    for (int j = 0; j < M; j++)
    {
      scanf("%d", &Mat[i][j]);
      ///////////////////////&&&&&&&&&&&&&&&&&&&&&&&&&
    }
  }
  printf("\n");
}
void Array_print(int N, int M, int Mat[][M]) /// 여기 이름은 바꿔주는 게 좋은 건가?
{

  for (int i = 0; i < N; i++)
  {
    for (int j = 0; j < M; j++)
    {
      printf("%4d", Mat[i][j]);
    }
    printf("\n");
  }
  printf("\n");
}

void matrixMulti(int N, int M, int L, int A[][M], int B[][L])
{

  int Mat[N][L]; // Mat[N][L] = {0}; 못 하는 이유가 동적할당을 하기 위함인가?

  for (int i = 0; i < N; i++)
  {
    for (int j = 0; j < L; j++)
    {
      Mat[i][j] = 0; //////////왜 초기화 해야 되지? --> 아래에서 += 니까
      for (int k = 0; k < M; k++)
      {
        Mat[i][j] += A[i][k] * B[k][j];
        printf("%d = %d + %d \n", Mat[i][j], A[i][k], B[k][j]);
      }
    }
  }
  Array_print(N, L, Mat);
}

int main()
{
  int N, M, L;
  printf("N M L 입력\n");
  scanf("%d %d %d", &N, &M, &L); ///////////;;;;;;;;;;;;;;;;;;;;;;;;;
  int B[N][M], S[N][M];
  int *A[N] = (int *)malloc(M * sizeof(int));

  input(N, M, A);
  Array_print(N, M, A);

  input(M, L, B);
  Array_print(M, L, B);

  matrixMulti(N, M, L, A, B);
}
