#include <stdio.h>

int main()
{
  int x, y, w, h;
  scanf("%d %d %d %d", &x, &y, &w, &h);
  if (w - x < h - y)
  {
    if (w - x <= x && w - x <= y)
    {
      printf("%d", (w - x));
    }
    else if (x < y)
    {
      printf("%d", x);
    }
    else
    {
      printf("%d", y);
    }
  }
  else
  {
    if (h - y <= x && h - y <= y)
    {
      printf("%d", (h - y));
    }
    else if (x < y)
    {
      printf("%d", x);
    }
    else
    {
      printf("%d", y);
    }
  }
}