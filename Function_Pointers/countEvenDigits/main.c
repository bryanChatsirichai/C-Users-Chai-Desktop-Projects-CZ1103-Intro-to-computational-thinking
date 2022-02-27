#include <stdio.h>
int countEvenDigits1(int number);
void countEvenDigits2(int number, int *count);
int main()
{
 int number, result;

 printf("Enter a number: \n");
 scanf("%d", &number);
 printf("countEvenDigits1(): %d\n", countEvenDigits1(number));
 countEvenDigits2(number, &result);
 printf("countEvenDigits2(): %d\n", result);

 return 0;
}
int countEvenDigits1(int number){
    int total_even,digit,counter=0;
    while ( number != 0) //start from the last digit
    {
        digit = number %10; //check last digit
        if (digit % 2 == 0)
        {
            counter++;
        }
        number = number / 10;
    }
 return counter;
}
void countEvenDigits2(int number, int *count){
    int total_even,digit,counter=0;
    while ( number != 0) //start from the last digit
    {
        digit = number %10; //check last digit
        if (digit % 2 == 0)
        {
            counter++;
        }
        number = number / 10;
    }
    *count = counter; //*count means access to value of that address and set = to counter


}
