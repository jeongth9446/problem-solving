#include <stdio.h>

int main(void) {
    int a, b;
    scanf("%d %d", &a, &b);
    
    printf("%.10lf\n", (double)a/(double)b);
    return 0;
}