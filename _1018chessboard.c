#include <stdio.h>
#include <stdbool.h>
#include <string.h>

/// 만약 크기 제한이 없으면 어떻게 해야 되나
/// 동적할당으로 바꿔서 해보기 **
// B 1 W 0
int main()
{
  bool flag = false;
  int M, N;
  scanf("%d %d", &N, &M);
  char board[N][M];
  char result_board1[8][10], result_board2[8][10];
  int A = N > M ? N : M;
  int result1[A];
  int result2[A];
  int count1, count2;

  for (int j = 0; j < N; j++)
    scanf("%s", board[j]);

  for (int i = 0; i < 4; i++)
  {

    strcpy(&result_board1[i * 2], "BWBWBWBW");
    strcpy(&result_board1[2 * i + 1], "WBWBWBWB");
    strcpy(&result_board2[2 * i], "WBWBWBWB");
    strcpy(&result_board2[2 * i + 1], "BWBWBWBW");
    // result_board2[2 * i][2 * j] = "W";
    // result_board2[2 * i + 1][2 * j + 1] = "B";
  }

  for (int i = 0; i <= N - 8; i++)
  { /// N-8은 세로 최소값
    count1 = 0;
    count2 = 0;
    for (int j = 0; j <= M - 8; j++)
    { /// M-8은 가로 최소값
      for (int k = i; k < i + 8; k++)
      {
        for (int n = j; n < j + 8; n++)
        {
          if (board[k][n] != result_board1[k][n])
            count1++;
          if (board[k][n] != result_board2[k][n])
            count2++;
        }
      }
      result1[j] = count1;
      result2[j] = count2;
    }
    printf("aaaaaaaaaaaaaaaaaaaaa%d\n", i);
  }

  for (int i = 0; i <= A - 8; i++)
  {
    printf("%d\n", result1[i]);
    printf("%d\n", result2[i]);
  }
  // 홀수인 경우

  // 짝수인 경우

  // printf("\n");
  // bool x = false;
  // if (x == 1) // x != 0 // x
  // {
  //   printf("x is true.");
  // }
  // else
  // {
  //   printf("x is false.");
  // }
}