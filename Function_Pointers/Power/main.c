#include <stdio.h>
float power1(float num, int p);
void power2(float num, int p, float *result);
int main()
{
 int power;
 float number, result=-1;

 printf("Enter the number and power: \n");
 scanf("%f %d", &number, &power);
 printf("power1(): %.2f\n", power1(number, power));
 power2(number,power,&result);
 printf("power2(): %.2f\n", result);
 return 0;
}
float power1(float num, int p)
{
    int i;float result_1=1;
if (p >= 0) //single line no need {}
    for(i = 1; i <= p; i++)
        result_1 = result_1* p;

else //single line no need {}
    for (i = -1; i >=p; i--)
        result_1 = result_1 * (1/num);

return result_1;

}

void power2(float num, int p, float *result)
{
    int i;float result_2=1;
if (p >= 0) //single line no need {}
    for(i = 1; i <= p; i++)
        result_2 = result_2* p;

else //single line no need {}
    for (i = -1; i >=p; i--)
        result_2 = result_2 * (1/num);

 *result = result_2;
}
