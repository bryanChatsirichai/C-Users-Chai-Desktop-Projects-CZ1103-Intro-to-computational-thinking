#include <stdio.h>
#include <stdlib.h>

int main()
{
    int rows, counter,copy,num;


    printf("Enter number of rows \n");
    scanf( "%d", &rows);
    printf("pattern\n");
    for (counter = 1; counter <= rows;counter++)
    {
        for (copy = 1; copy <= counter; copy++)
        {
            num = counter % 3;
            if(num == 0)
            {

                printf("3");
            }
            else
                printf("%d", num);
        }


        printf("\n");
    }
    return 0;
}
