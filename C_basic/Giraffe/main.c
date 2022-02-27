#include <stdio.h>
#define SIZE 9
int main ( ) {
int ar[3][3]= {
{5, 10, 15},
{10, 20, 30},
{20, 40, 60}
};
int i;
int *ptr;
ptr = &ar;
/* using pointer - looping */
for (i=0; i<SIZE; i++)
printf("%d ", *ptr++);
printf("\n");
return 0;
}
