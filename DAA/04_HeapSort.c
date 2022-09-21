#include <stdio.h>
#include <stdlib.h>
#include<time.h>

#define range 500
#define max 500
int A[max];

void heapSort(int);
void heapify(int,int);
void swap(int *, int *);

int main(void)
{
    srand(time(0));
    int n,i,j,k;
    clock_t start,end;
    double cpu_exec_time;

    printf("\nEnter the value of n: ");
    scanf("%d",&n);

    for(i=0;i<n;i++)
        A[i] = rand()%range;

    printf("\nArray elements: \n");
    for(i=0;i<n;i++)
        printf("%d\t",A[i]);
    
    start = clock();
    for(i=0;i<1000;i++)
    for(j=0;j<1000;j++)
        heapSort(n);
    end = clock();
    
    
    //cpu_exec_time = (double) (end - start) / CLK_TCK;    
    cpu_exec_time = (double) (end - start) / CLOCKS_PER_SEC;

    printf("\nSorted array: \n");
    for(i=0;i<n;i++)
        printf("%d\t",A[i]);
    printf("\nCPU execution time = %lf\n", cpu_exec_time);
    return 0;
}

void heapSort(int n)
{
    int i;
    for(i=n/2 ; i>0 ; i--)
        heapify(n,i);
    
    for(i=n; i>1; i--)
    {
         swap(&A[i], &A[1]);
         heapify(i-1,1);
    }
}

void heapify(int n, int i)
{
    int largest, left, right;
    largest = i;
    left = 2*i; right = 2*i+1;
    if(left<=n && A[left]>A[largest])
        largest = left;
    if(right<=n && A[right] > A[largest])
        largest = right;
    if(largest != i)
    {
        swap(&A[largest] ,&A[i]);
        heapify(n, largest);
    }
}

void swap(int *p, int *q)
{
    int t = *p;
    *p = *q;
    *q = t;
}
