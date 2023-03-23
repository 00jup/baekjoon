#include <stdio.h>
#include <stdlib.h>

void input(int N, int M, int *Mat)
{
  for (int i = 0; i < N; i++)
  {
    for (int j = 0; j < M; j++)
    {
      scanf("%d", (Mat + i * M + j));
    }
  }
  printf("\n");
}
void Array_print(int N, int M, int *Mat) /// 여기 이름은 바꿔주는 게 좋은 건가?
{

  for (int i = 0; i < N; i++)
  {
    for (int j = 0; j < M; j++)
    {
      printf("%4d", *(Mat + i * M + j));
    }
    printf("\n");
  }
  printf("\n");
}

int matrixMulti(int N, int M, int L, int A[][M], int B[][L])
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
        printf("Mat[%d][%d] %d Mat 주소 : %p \n", i, j, Mat[i][j], Mat);
      }
      printf("\n");
    }
  }
  printf("\n\n\n d %p *Mat %d Mat[1][1] %d\n\n", Mat, *Mat, Mat[1][1]);
  return Mat;
}

int main()
{
  int N, M, L;
  printf("N M L 입력\n");
  scanf("%d %d %d", &N, &M, &L); ///////////;;;;;;;;;;;;;;;;;;;;;;;;;

  int *A = (int *)malloc(N * M * sizeof(int));
  int *B = (int *)malloc(L * M * sizeof(int));
  int *S = (int *)malloc(N * L * sizeof(int));
  //---------------------여기를 M N으로 해서 안 됐구나...
  // int S[N][L];

  input(N, M, A);
  Array_print(N, M, A);

  input(M, L, B);
  Array_print(M, L, B);

  S = matrixMulti(N, M, L, A, B);
  printf("\n S 주소 %p\n", S);

  Array_print(N, L, S);

  free(A);
  free(B);
  free(S);
  return 0;
}
