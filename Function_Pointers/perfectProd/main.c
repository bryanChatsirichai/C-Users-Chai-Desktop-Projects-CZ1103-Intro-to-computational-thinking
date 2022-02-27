#include <stdio.h>
int perfectProd1(int num);
void perfectProd2(int num, int *prod);
int main()
{
 int number, result=0;

 printf("Enter a number: \n");
 scanf("%d", &number);
 printf("Calling perfectProd1() \n");
 printf("perfectProd1(): %d\n", perfectProd1(number));

 printf("Calling perfectProd2() \n");
 perfectProd2(number, &result);
 printf("perfectProd2(): %d\n", result);
 return 0;
}
int perfectProd1(int num){
    int  i,j,sum,product=1;
    /* Iterate from 1 to end */
    for(i = 1; i<= num; i ++)
    {
        sum = 0; //every new range restart sum test

        /* Check whether the current number i is Perfect number or not */
        for(j=1; j < i; j++) //note does not end at the same amount
        {

            if(i % j == 0 ) //add all the factors except itself
            {
                //printf("The factor of %d are %d\n",i,j); factor of num
                sum = sum + j;
                //printf(" the sum is %d\n ", sum);
            }
        }
        if(sum == i)
        {
          printf("call by value perfect numbers: %d\n",i);
          product = product * i;
        }

    }
    return product;

    }

void perfectProd2(int num, int *prod)
{
 int start,sum,factors,product = 1;
 for(start = 1; start <= num; start++)
 {
    sum = 0;
    for(factors = 1; factors < start; factors ++)
    {
        if (start % factors == 0)
        {
        sum = sum + factors;
        }
    }
    if (sum == start)
    {
        printf("call by reference Perfect number: %d\n",start);
        product = product * sum;
    }
    *prod = product;
 }
}

