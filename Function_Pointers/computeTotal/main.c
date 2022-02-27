#include <stdio.h>
void computeTotal(int numOfLines);
int main()
{
 int numOfLines;
 printf("Enter number of lines: \n");
 scanf("%d", &numOfLines);

 computeTotal(numOfLines);
 return 0;
}
void computeTotal(int numOfLines)
{
 int lines=1,x,amout,input,total;
 while(lines <= numOfLines)
  {
   total = 0; //reset after each interation
   printf("Enter line %d\n",lines);
   scanf(" %d",&x); // control amount of input
   for (amout = 1 ; amout <= x; amout++ )
   {
     scanf(" %d",&input);
     total=total+input;
   }
   lines ++; //lines increment
    printf("Total: %d\n",total);
  }


}
