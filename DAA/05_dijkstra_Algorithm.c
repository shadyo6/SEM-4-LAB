#include <stdio.h>
#include <stdlib.h>
#define infinity 999

void dijkstra(int,int,int [][10],int []);

int main(void)
{
    int i,j,n,v,cost[10][10],dist[10];
    printf("\nEnter the number of nodes : ");
    scanf("%d",&n);
    printf("\nEnter the cost matrix :\n");
    for(i=1;i<=n;i++)
    {
        for(j=1;j<=n;j++)
        {
            scanf("%d",&cost[i][j]);
            if(cost[i][j]==0)
                cost[i][j]=infinity;
        }
    }
    printf("\nEnter the source matrix :\n");
    scanf("%d",&v);
    dijkstra(v,n,cost,dist);
    printf("\nShortest path :\n");
    for(i=1;i<=n;i++)
        if(i!=v)
            printf("%d->%d,cost=%d\n",v,i,dist[i]);
    return 0;
}

void dijkstra(int v,int n,int cost[10][10],int dist[10])
{
    int flag[10],count,i,u,min,w;
    
    for(i=1;i<=n;i++)
        flag[i]=0,dist[i]=cost[v][i];
    
    count=2;
    while(count<=n)
    {
        min=99;
        for(w=1;w<=n;w++)
            if(!flag[w] && dist[w]<min)
                u=w,min=dist[w];
        
        flag[u]=1;
        count++;
        
        for(w=1;w<=n;w++)
            if(!flag[w] && (dist[u]+cost[u][w]<dist[w]))
                dist[w]=dist[u]+cost[u][w];
    }
}
