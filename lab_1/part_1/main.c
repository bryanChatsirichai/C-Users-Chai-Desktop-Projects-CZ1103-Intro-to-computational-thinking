#include <stdio.h>
#include <stdlib.h>

int main()
{
    int student_id,mark;
    printf("Enter student ID: \n");
    scanf("%d", &student_id);
    while(student_id != -1)
    {
        printf("enter marks\n");
        scanf("%d", &mark);
        if (mark <= 100)
        {
            if (mark >= 75)
                printf("Grade = A\n");
            else if (mark >=65 )
                printf("Grades = B \n");
            else if (mark >= 55)
                printf("Grades = C \n");
            else if (mark >= 45)
                printf("Grades = D \n");
            else if (mark >= 0)
                printf("Grades = F \n");
            else
                printf("Out of range\nm");
        }
        printf("Enter student ID: \n");
        scanf("%d", &student_id);

    }
    return 0;


}
