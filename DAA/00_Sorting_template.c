#include <stdio.h>
#include<stdlib.h>
#include<time.h>
int main()
{
	srand(time(0)); 				//set the sed to time(0) to generate random seeds evertime the code runs
	int n,i,j;
	double cpu_exe_time;
	clock_t s,e;
	printf("\nEnter the size of the array: ");
	scanf("%d",&n);
	int arr[n];
	for(i=0;i<n;i++)
		arr[i]=rand()%100;
		
	s=clock();
	for(j=0;j<1000;j++)	 			//use upto 1000 to avoid integer overflow
	for(i=0;i<1000;i++)      			//Delay loops
	{
		//sorting Function()
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
