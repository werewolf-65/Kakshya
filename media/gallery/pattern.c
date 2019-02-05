#include <stdio.h>
void main(){
  int i,s,j,a;
  for (i=1;i<=5;i++){
    for (j=1;j<=5;j++){
      for (s=1;s<=i-1;s++){
        printf(" ");
      }
      for(a=5;a>=1;a--){
        printf("*");
      }
    }
    printf("\n");
  }
}
