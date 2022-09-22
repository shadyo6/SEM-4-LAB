#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define range 500

void heapSort(int [], int);
void buildHeap(int [], int);
void maxHeapify(int [], int,int);
void swap(int *, int *);

int main(void)
{
    srand(time(0));
    int n,i,j;
    clock_t start,end;
    double cpu_exec_time;

    printf("\nEnter the value of n: ");
    scanf("%d",&n);

    int *arr = (int*)malloc(n*sizeof(int));
    if (arr == NULL)
    {
        printf("\nMemory not allocated.\n");
        exit(0);
    }
    
    for(i=0;i<n;i++)
        arr[i] = rand()%range;

    printf("\naArray elements: \n");
    for(i=0;i<n;i++)
        printf("%d\t",arr[i]);
    
    start = clock();
    for(i=0;i<1000;i++)
    for(j=0;j<1000;j++)
        heapSort(arr,n);
    end = clock();
    
    
    //cpu_exec_time = (double) (end - start) / CLK_TCK;    
    cpu_exec_time = (double) (end - start) / CLOCKS_PER_SEC;

    printf("\nSorted array: \n");
    for(i=0;i<n;i++)
        printf("%d\t",arr[i]);
    printf("\nCPU execution time = %lf\n", cpu_exec_time);
    free(arr);
    return 0;
}

void heapSort(int arr[], int n)
{
    int i;
    buildHeap(arr,n);
    
    for(i=n-1; i>=1; i--)
    {
         swap(&arr[0], &arr[i]);
         maxHeapify(arr,i-1,0);
    }
}

void buildHeap(int arr[], int n)
{
    int i;
    for(i=(n-2)/2 ; i>=0 ; i--)
        maxHeapify(arr,n,i);
}
void maxHeapify(int arr[], int n, int i)
{
    int largest=i, left=2*i+1, right=2*i+2;
   
    if(left<n && arr[left]>arr[largest])
        largest = left;
    if(right<n && arr[right] > arr[largest])
        largest = right;
    if(largest != i)
    {
        swap(&arr[largest] ,&arr[i]);
        maxHeapify(arr,n,largest);
    }
}

void swap(int *p, int *q)
{
    int t = *p;
    *p = *q;
    *q = t;
}
