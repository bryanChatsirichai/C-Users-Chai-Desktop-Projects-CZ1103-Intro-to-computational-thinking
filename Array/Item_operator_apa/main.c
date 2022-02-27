/*edit*/

/*custom header*/

  /*end_edit*/
#include <stdio.h>
#define MAX 10
void initialize(int *size, int ar[]);
void insert(int max, int *size, int ar[], int num);
void iremove(int *size, int ar[], int num);
void display(int size, int ar[]);
int main()
{
   int  option = 0;
   int  num, ar[MAX], size = 0;

   printf("Please select an option: \n");
   printf("(1) Initialize the array \n");
   printf("(2) Insert an integer \n");
   printf("(3) Remove an integer \n");
   printf("(4) Display the numbers stored in the array \n");
   printf("(5) Quit \n");
   do {
      printf("Enter your choice: \n");
      scanf("%d", &option);
      switch (option) {
         case 1:
            initialize(&size, ar);
            break;
         case 2:
            printf("Enter an integer: \n");
            scanf("%d", &num);
            insert(MAX, &size, ar, num);
            break;
         case 3:
            printf("Enter the integer to be removed: \n");
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
   int i;

   printf("The %d numbers in the array: \n", size);
   for(i = 0; i < size; i++)
      printf("%d ", ar[i]);
   printf("\n");

}
void initialize(int *size, int ar[])
{
    int total, i, num;
    printf("Enter the total number of integers (MAX=%d): \n", MAX);
    scanf("%d", &total);
    (*size) = 0;
    printf("Enter the integers: \n");
    for (i = 0; i < total; i++)
        {
            scanf("%d", &num);
            insert(MAX, size, ar, num);
        }
}
void insert(int max, int *size, int ar[], int num)
{
    int i,j,temp;
    if (*size == max)
        printf("The array is full\n");
    else{
        ar[*size] = num;
        (*size)++;

        for (i=0; i<*size; i++)
        {
            for (j=i; j<*size; j++)
            {
                if (ar[i]>ar[j])
                {
                    temp =ar[i];
                    ar[i] = ar[j];
                    ar[j] = temp;
                }
            }
        }

    }
}
void iremove(int *size, int ar[], int num)
{
    int i, j, count = 0, test = 0, position;
    if ((*size)==0)
    {
        printf("The array is empty\n");
    }
    else
    {
        for  (i=0; i<(*size); i++) //check if num in array
        {
            if (ar[i] == num)
            {
                test = 1;
                position = i;
            }
        }
        if (test == 1)
        {
            for (j=position; j<(*size)-1; j++)
            {
                ar[j] = ar[j+1];
            }
            ar[(*size)-1] = 0;
            (*size)--; //reduce array size
            printf("The integer is removed\n");
            }

        else{
            printf("The number is not in the array\n");
        }
    }
}
