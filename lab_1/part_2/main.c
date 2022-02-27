#include <stdio.h>
#include <stdlib.h>

int main()

{
    int line,t,nums,count,total;
    double avg;
    printf("Enter number of lines :\n");
    scanf("%d", &line);
    for ( t = 1; t <= line; t++)
    {
        printf("Enter line %d (end with -1)\n", t);
        count = 0; total = 0;

        scanf("%d", &nums);
        while(nums != -1)
        {
            count ++ ;
            total = total + nums;
            scanf("%d", &nums);
        }

        if (total == 0)
            printf("You quit before entering a number\n");
        else
            {
            avg = (double)total / (double)count;
            printf("avg is %.2f\n",avg);
            }
    }

    return 0;
}
