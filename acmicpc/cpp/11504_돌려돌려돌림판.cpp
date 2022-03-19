
#include <stdio.h>

int main()
{
    int t;
    scanf("%d", &t);
    
    while(t--) {
        int n, m;
        int arr[201];
        scanf("%d %d", &n, &m);
        int x = 0, y = 0, res = 0;
        
        for(int i = 0; i < m; i ++) {
            int k;
            scanf("%d", &k);
            x = x*10 + k;
        }
        for(int i = 0; i < m; i ++) {
            int k;
            scanf("%d", &k);
            y = y*10 + k;
        }
        for(int i = 0; i < n; i ++) {
            scanf("%d", &arr[i]);
            arr[i+n] = arr[i];
        }    
        
        for(int i = 0; i < n; i ++) {
            int s = 0;
            for(int k = 0; k < m; k ++) 
                s = s*10 + arr[k+i];
            if(x <= s && s <= y) res ++;    
        }
        printf("%d\n", res);
    }

    return 0;
}
