#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
//
// if도 연산에 포함되나 ?
int main()
{
  // char *str = {"pi", "ka", "chu"};
  // char *input = (char *)malloc(5000);
  char input[5000];
  scanf("%s", input);
  int index = strlen(input);

  int i = 0;
  bool flag = false;
  for (int i = 0; i < index; i++)
  {

    printf("%c\n", input[i]);

    if (input[i] == "p")
    {
      if (input[i + 1] == "i")
      {
        flag = true;
        i++;
      }
      else
        i++;
      i++;
    }
    else if (input[i] == "k")
    {
      if (input[i + 1] == "a")
      {
        flag = true;
        i += 2;
      }
      else
        i++;
      i++;
    }
    else if (input[i] == "c")
    {
      if (input[i + 1] == "h")
      {
        if (input[i + 2] == "u")
        {
          flag = true;
          i += 3;
        }
        else
        {
          i += 2;
          break;
        }
        i += 2;
      }
      i++;
    }
  }
  if (flag == true)
    printf("YES\n");

  else if (flag == false)
    printf("NO\n");

  return 0;
}