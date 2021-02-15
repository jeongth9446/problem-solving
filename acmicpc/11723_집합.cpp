#include <cstdio>
#include <cstring>
bool S[25];
int main() {
    int Q, num;
    scanf("%d", &Q);
    while(Q--) {
        char order[15];
        scanf("%s", order);
        if(order[2] == 'd') { // add
            scanf("%d", &num);
            S[num] = 1;
        } else if(order[0] == 'r') {
            scanf("%d", &num);
            S[num] = 0;
        } else if(order[0] == 'c') {
            scanf("%d", &num);
            printf("%d\n", S[num]);
        } else if(order[0] == 't') {
            scanf("%d", &num);
            S[num] ^= 1;
        } else if(order[0] == 'a') memset(S, 1, 25);
        else memset(S, 0, 25);
    }
}