#include <stdio.h>
#include <stdlib.h>
#define infinity 999

int u,v,n,i,j,ne=1;
int min,mincost=0,cost[10][10],visited[10]={0};

int main(void)
{
    printf("\nEnter the number of nodes: ");
    scanf("%d",&n);
    
    printf("\nEnter the adjacency matrix: \n");
    for(i=1;i<=n;i++)
        for(j=1;j<=n;j++)
        {
            scanf("%d",&cost[i][j]);
            if(cost[i][j]==0)
                cost[i][j]=infinity;
        }
    
    visited[1]=1;
    while(ne<n)
    {
        min=infinity;
        for(i=1;i<=n;i++)
            for(j=1;j<=n;j++)
                if(cost[i][j] < min && visited[i]!=0)
                {
                    min = cost[i][j];
                    u=i;
                    v=j++;
                }
        
        if(visited[u]==0 || visited[v]==0)
        {
            printf("\nEdge %d:(%d %d) cost : %d",ne++,u,v,min);
            mincost+=min;
            visited[v]=1;
        }
        cost[u][v]=cost[v][u]=infinity;
    }
    printf("\nMinimum cost: %d\n" ,mincost);
    return 0;
}
