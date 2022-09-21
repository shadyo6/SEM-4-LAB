#include <stdio.h>
#include <time.h>
#include <stdlib.h>

#define range 500
#define max 500
int A[max];

void insertionSort(int);

int main()
{
	srand(time(0));
	int i,j,n;
	clock_t s,e;
	double cpu_exe_time;

	printf("Enter number of elements: ");
	scanf("%d",&n);

	for(i=0 ; i<n ; i++)
		A[i] = rand()%range;

	printf("\n\nThe array elements are: \n");
	for(i=0 ; i<n ; i++)
		printf("%d  ",A[i]);

	s = clock();
	for(j=0 ; j<1000 ; j++)
	for(i=0 ; i<1000 ; i++)
		insertionSort(n);
	e = clock();

	//cpu_exe_time = (double)(e-s)/CLK_TCK;
	cpu_exe_time = (double)(e-s)/CLOCKS_PER_SEC;
	printf("\n\nOrder of sorted elements: \n");
	for(i=0 ; i<n ; i++)
		printf("%d  ",A[i]);

	printf("\n\nCPU execution time:  %lf \n",cpu_exe_time);
	return 0;
}

void insertionSort(int n)
{
	int min,i,j;
	for(i=1 ; i<n ; i++)
	{
		min = A[i];
		j = i-1;
		while(A[j]>=min && j>=0)
		{
			A[j+1] = A[j];
			j--;
		}
		A[j+1] = min;
	}
}
