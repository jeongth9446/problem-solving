#include <stdio.h>

int main(void) {
    int a, b, c, d, e;
    scanf("%d %d %d %d %d", &a, &b, &c, &d, &e);
    
    int k = a*a + b*b + c*c + d*d + e*e;
    printf("%d\n", k%10);
    return 0;
}