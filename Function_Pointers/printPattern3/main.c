#include <stdio.h>
void printPattern3(int height);
int main()
{
 int height;
 printf("Enter the height: \n");
 scanf("%d", &height);
 printf("printPattern3(): \n");
 printPattern3(height);
 return 0;
}
void printPattern3(int height)
{
 int x,y,amount,counter;
 for(y=1; y <= height; y++) //control height
 {
    counter = y; //control the inputs
    for(x=1;x <= y; x++) //control row length
    {
        printf("%d",counter);
        counter+=1;
        if (counter > 9) //reset if input > 9
        {
            counter = 0;
        }
    }
    printf("\n");
 }

}
