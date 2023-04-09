
#include <stdio.h>
#include <string.h>

int main()
{
  char S[100];
  int result[26];

  scanf("%s", S);

  for (int j = 0; j < 26; j++)
    result[j] = -1;

  for (int i = 0; i < strlen(S); i++)
  {
    if (result[S[i] - 'a'] == -1)
    {
      result[S[i] - 'a'] = i; // S[i] - 'a'는 알파벳의 순서
    }
  }

  for (int i = 0; i < 26; i++)
    printf("%d ", result[i]);
  printf("\n");
}
