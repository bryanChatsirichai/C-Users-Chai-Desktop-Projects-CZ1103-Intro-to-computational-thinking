
#include <stdio.h>
#define MAX 10
void initialize(int *size, int ar[]);
void insert(int max, int *size, int ar[], int num);
void iremove(int *size, int ar[], int num);
void display(int size, int ar[]);
int main()
{
 int option = 0;
 int num, ar[MAX], size = 0;

 printf("Please select an option: \n");
 printf("(1) Initialize the array \n");
 printf("(2) Insert an integer \n");

 printf("(3) Remove an integer \n");
 printf("(4) Display the numbers stored in the array \n");
 printf("(5) Quit \n");
 do {
 printf("Enter your choice:\n");
 scanf("%d", &option);
 switch (option) {
 case 1:
 initialize(&size, ar);
 break;
 case 2:
 printf("Enter an integer:\n");
 scanf("%d", &num);
 insert(MAX, &size, ar, num);
 break;
 case 3:
 printf("Enter the integer to be removed:\n");
 scanf("%d", &num);
 iremove(&size, ar, num);
 break;
 case 4:
 display(size, ar);
 break;
 default:
 break;
 }
 } while (option < 5);
 return 0;
}
void display(int size, int ar[])
{
 int i=0;
 printf("The %d numbers in the array:\n", size);
 for(i; i < size; i++)
 printf("%d ", ar[i]);
 printf("\n");


}
void initialize(int *size, int ar[])
{
     int total, i=0, num;
     printf("Enter the total number of integers (MAX=%d):\n", MAX);
     scanf("%d", &total);
     (*size) = 0;
     printf("Enter the integers: \n");
     for (i; i < total; i++)
    {
     scanf("%d", &num);
     insert(MAX, size, ar, num);
    }

}
void insert(int max, int *size, int ar[], int num)
{
    int i,j,temp;
    if(*size == max)
        printf("The array is full\n");
    else
    {
        ar[*size] = num;
        (*size)++;

     for(i=0;i <*size; i++)
    {
        for(j= i+1;j<*size; j++)
        {
            if(ar[i] > ar[j])
            {
                temp = ar[i];
                ar[i]= ar[j];
                ar[j] = temp;
            }
        }
    }

    }
}

void iremove(int *size, int ar[], int num)
{

    int i=0,index=-1,remove;
    remove=0;
    if((*size) == 0)
        printf("The array is empty\n");
    else
    {
        for(i;i < (*size) ;i++)
        {
            if(ar[i] == num)
            {
            index = i;
            remove = 1;
            }
        }
        if(remove == 1){
            for(i = index; i < (*size)- 1; i++)
            {
                ar[i] = ar[i + 1];
            }
            *size = *size - 1;
            printf("remove size %d\n",*size);
            }
        else
            printf("The number is not in the array\n");
        }

}
