#include <stdio.h>
int sumSqDigits1(int num);
void sumSqDigits2(int num, int *result);
int main()
{
 int num, result;
 printf("Enter a number: \n");
 scanf("%d", &num);
 printf("sumSqDigits1(): %d\n", sumSqDigits1(num));
/*sumSqDigits2(num, &result);
 printf("sumSqDigits2(): %d\n", result);*/
 return 0;
}
int sumSqDigits1(int num){
    int count,sum = 0,square,input;
    char end;
    while (end != '\n'){
        scanf("%d",&input);
        sum = sum + (input * input);

    }
    return sum;
}
void sumSqDigits2(int num, int *result)
{
 /* Write your code here */
}
