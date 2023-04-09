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
    for (char j = 'a'; j <= 'z'; j++)
    {
      if (S[i] == j)
      {
        if (result[j - 97] != -1)
          break;

        result[j - 97] = i;
        break;
      }
    }
    }

  for (int i = 0; i < 26; i++)
    printf("%d ", result[i]);
  printf("\n");
}
