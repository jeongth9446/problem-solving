#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {

    int a, b;
    a = 0;
    b = 1;
    
    for(int i = 0; i < n; i ++) {
        int t = a + b;
        a = b;
        b = t;
        a %= 1234567;
        b %= 1234567;
    }
    return a;
    
}