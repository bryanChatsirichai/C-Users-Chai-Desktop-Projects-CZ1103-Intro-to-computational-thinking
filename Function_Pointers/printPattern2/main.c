#include <stdio.h>
void printPattern2(int height);
int main()
{
 int height;
 printf("Enter the height: \n");
 scanf("%d", &height);
 printf("printPattern2(): \n");
 printPattern2(height);
 return 0;
}
void printPattern2(int height){
 int y,x,amount;
 for(y=1; y<= height; y++ ) //control the rows
 {
  amount = y; // letters in a row
  for(x=1; x <= y; x++) //control the letters per row
  {
    if (amount % 2 == 0) // even row B first letter then alternate
    {
        printf("B");
    }
    else
    {
        printf("A");
    }
    amount = amount -1 ;
 }
    printf("\n"); //to go next line
 }
}
