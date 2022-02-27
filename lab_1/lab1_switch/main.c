#include <stdio.h>
int main() {
int studentNumber = 0, mark;
printf("Enter Student ID: \n");
scanf("%d", &studentNumber);
while (studentNumber != -1)
{
    printf("Enter Mark: \n");
    scanf("%d", &mark);
    switch (mark)
    {
    case 75 ... 100:
        printf("%c\n", 'A');
        break;
    case 65 ... 74:
        printf("%c\n", 'B');
    break;
    case 55 ... 64:
        printf("%c\n", 'C');
        break;
    case 45 ... 54:
        printf("%c\n", 'D');
    break;
    case 0 ... 44:
        printf("%c\n", 'F');
        break;
    default:
        printf("Invalid entry\n");

    }
    printf("Enter Student ID: \n");
    scanf("%d", &studentNumber);
}
return 0;
}
