#include <stdio.h>
int allEvenDigits1(int num);
void allEvenDigits2(int num, int *result);
int main()
{
 int number, p=999, result=999;
 printf("Enter a number: \n");
 scanf("%d", &number);
 p = allEvenDigits1(number);
 if (p == 1)
 printf("allEvenDigits1(): yes\n");
 else if (p == 0)
 printf("allEvenDigits1(): no\n");
 else
 printf("allEvenDigits1(): error\n");
 allEvenDigits2(number, &result);
 if (result == 1)
 printf("allEvenDigits2(): yes\n");
 else if (result == 0)
 printf("allEvenDigits2(): no\n");
 else
 printf("allEvenDigits2(): error\n");
 return 0;
}
int allEvenDigits1(int num)
{
    int count,check,even=0,odd=0;
 while(num !=0) //check from the back
 {
    check = num % 10;
    if(check % 2 == 0)
     even ++;
    else
        odd++;
    num = num / 10; // minus last digit
}
    if(odd == 0) //all even
        return 1;
    else //not all even
        return 0;
}
void allEvenDigits2(int num, int *result)
{
     int count,check,even=0,odd=0;
 while(num !=0) //check from the back
 {
    check = num % 10;
    if(check % 2 == 0)
     even ++;
    else
        odd++;
    num = num / 10; // minus last digit
}
    if(odd == 0) //all even
        *result = 1;
    else //not all even
        *result = 0;
}
