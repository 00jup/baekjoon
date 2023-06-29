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
  printf("\n\n");
}
void Array_print(int N, int M, int *Mat)
{

  for (int i = 0; i < N; i++)
  {
    for (int j = 0; j < M; j++)
    {
      printf("%4d", Mat[i * M + j]);
    }
    printf("\n");
  }
  printf("\n\n");
}

int *matrixMulti(int N, int M, int L, int *A, int *B)
{

  int *Mat = (int *)malloc(N * L * sizeof(int));

  for (int i = 0; i < N; i++)
  {
    for (int j = 0; j < L; j++)
    {
      *(Mat + i * M + j) = 0;
      for (int k = 0; k < M; k++)
      {
        *(Mat + i * M + j) += A[i * M + k] * B[k * M + j];
      }
      printf("Mat[%d][%d] Mat[i][j] %d Mat address : %p \n", i, j, *(Mat + i * M + j), Mat);
      printf("\n");
    }
  }

  return Mat;
}

int main()
{
  int N, M, L;
  printf("input N M L\n      ");
  scanf("%d %d %d", &N, &M, &L);
  int a[3][3] = {1, 2, 3, 4, 5, 6, 7, 8, 9};

  Array_print(3, 3, a);

  int *A = (int *)malloc(N * M * sizeof(int));
  int *B = (int *)malloc(L * M * sizeof(int));
  int *S = (int *)malloc(N * L * sizeof(int));

  input(N, M, A);
  Array_print(N, M, A);

  input(M, L, B);
  Array_print(M, L, B);

  S = matrixMulti(N, M, L, A, B);

  // printf("\n S address %p\n", matrixMulti(N, M, L, A, B)); ////////////////////////// ---> A
  printf("\n S address %p\n", S); ////////////////////////// ---> A-30
  printf("%d\n", *S);
  printf("%d\n", *(S + 1));
  printf("%d\n", *(S + 2));
  printf("%d\n", *(S + 3));
  printf("%d\n", *(S + 4));
  printf("%d\n", *(S + 5));
  printf("%d\n", *(S + 6));
  printf("%d\n", *(S + 7));
  printf("%d\n", *(S + 8));
  Array_print(N, L, S);

  free(A);
  free(B);
  free(S);
  return 0;
}
