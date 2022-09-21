#include <stdio.h>
#include<stdlib.h>
#include<time.h>
int main() {
	int n,i;
	double cpu_exe_time;
	clock_t s,e;
	srand(time(0));
	printf("\nEnter the size of the array: ");
	scanf("%d",&n);
	int arr[n];
	for(i=0;i<n;i++)
		arr[i]=rand()%100;
		
	s=clock();
	for(i=0;i<1000000;i++)      //Delay loops
	{
		
	}
	e=clock();
	//cpu_exe_time=double(e-s)/CLK_TCK;
	cpu_exe_time=double(e-s)/CLOCK_PER_SEC;
	printf("\nThe elements are: ");
	for(i=0;i<n;i++)
		printf("%d\t",arr[i]);
	printf("CPU execution time: %lf",cpu_exe_time);
	return 0;
}
