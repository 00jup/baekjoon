#include <stdio.h>
#include <stdlib.h>

#define MAX_STACK_SIZE 100000 // https://organize-study.tistory.com/60
typedef int element;
typedef struct
{
  element stack[MAX_STACK_SIZE];
  int top;
} stackType;
char result[MAX_STACK_SIZE * 2];

void init_stack(stackType *s)
{
  s->top = -1;
}

int is_empty(stackType *s)
{
  return (s->top == -1);
}

int is_full(stackType *s)
{
  return (s->top == MAX_STACK_SIZE - 1);
}

void push(stackType *s, element item)
{
  if (is_full(s))
  {
    fprintf(stderr, "stack full error\n");
    exit(1);
  }
  else
    s->stack[++(s->top)] = item;
}

element pop(stackType *s)
{
  if (is_empty(s))
  {
    fprintf(stderr, "stack empty error\n");
    exit(1);
  }
  else
    return s->stack[(s->top)--];
}

element peek(stackType *s)
{
  if (is_empty(s))
  {
    fprintf(stderr, "stack empty error\n");
    exit(1);
  }
  else
    return s->stack[s->top];
}

int main()
{
  int totalNum;
  printf("input\n");
  scanf("%d", &totalNum);
  int numArr[totalNum];
  for (int i = 0; i < totalNum; i++)
  {
    scanf("%d", &numArr[i]);
  }
  int idx = 0, num = 1;
  while (idx == totalNum * 2)
  {
    stackType *s;

    if (s->top == -1 || s->stack[s->top] < numArr[idx])
    {
      push(&s, num++); ////////////여기 잘 모르겠다.
      result[idx++] = '+';
      printf("%c", result[idx]);
    }
    else if (s->stack[s->top] == numArr[idx])
    {
      pop(&s);
      result[idx++] = '-';
      printf("%c", result[idx]);
      idx++;
    }
    else
    {
      printf("No\n");
      return 0;
    }
  }
  for (int i = 0; i < idx; i++)
  {
    printf("%c\n", result[i]);
  }
}