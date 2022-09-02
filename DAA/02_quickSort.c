#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX 100
int A[MAX];

void quickSort(int, int);
int partition(int, int);
void swap(int *,int *);

int partition(int low, int high)
{
    int i=low-1,j=high+1;
    int pivot=A[low];

    while(1)
    {
        do
        {
            i++;
        }while(A[i]<pivot);
        do
        {
            j--;
        }while(A[j]>pivot);

        if(i>=j)
            return j;
        swap(&A[i],&A[j]);
    }
}

void quickSort(int low, int high)
{
    if(low<high)
    {
        int p=partition(low,high);
        quickSort(low,p);
        quickSort(p+1,high);
    }
}

void swap(int *a,int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main()
{
    int n,i,j;
    int low,high;

    clock_t s,e;
    double cpu_exe_t;

    printf("\nPlease enter the size of the array: ");

    scanf("%d",&n);

    for(i=0;i<n;i++)
    {
        A[i]=rand()%100;
    }

    printf("\nThe array elements are: \n");
    for(i=0;i<n;i++)
    {
        printf("%d\t",A[i]);
    }
    s = clock();
    for(j=0;j<1000;j++)
    for(i=0;i<1000;i++)
    {
        low=0;
        high=n-1;
        quickSort(low,high);
    }
    e = clock();
    //cpu_exe_t = (double)(e-s)/CLK_TCK;
    cpu_exe_t = (double)(e-s)/CLOCKS_PER_SEC;

    printf("\nThe sorted array is: \n");
    for(i=0;i<n;i++)
    {
        printf("%d \t", A[i]);
    }
    printf("\nCPU execution time is %lf",cpu_exe_t);

    return 0;
}
