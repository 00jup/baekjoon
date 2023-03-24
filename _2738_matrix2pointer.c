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
      printf("%4d", *(Mat + i * M + j));
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

  int **A=NULL, **B=NULL, **S=NULL;

  int **A = (int **)malloc(N *sizeof(int*));
  int **B = (int **)malloc(M * sizeof(int*));
  int **S = (int **)malloc(M * sizeof(int*));
  for(int i = 0; i<N; i++){
    A[i] = (int*)malloc(sizeof(int) * M);
  }

  input(N, M, A);
  Array_print(N, M, A);

  // input(M, L, B);
  // Array_print(M, L, B);

  //S = matrixMulti(N, M, L, A, B);

  //printf("\n S address %p\n", matrixMulti(N, M, L, A, B)); ////////////////////////// ---> A
  //printf("\n S address %p\n", S);                          ////////////////////////// ---> A-30

  // Array_print(N, L, matrixMulti(N, M, L, A, B));

  free(A);
  free(B);
  free(S);
  return 0;
}
