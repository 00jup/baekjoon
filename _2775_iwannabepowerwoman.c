#include <stdio.h>

int count_home(k, n){
  int count = 0;
  if(k==0){
    return n;
  }
  else{
    for(int i = 0; i<n; i++){
      count += count_home(k-1, i);
    }
  }

}
int main()
{
  int T, cnt = 0;
  int *k = (int *)malloc(sizeof(int));
  int *n = (int *)malloc(sizeof(int));
  
  scanf("%d", &T);

  while (T > cnt)
  {
    scanf("%d", k+cnt);
    scanf("%d", n+cnt);
    cnt++;
  }
  
  
}