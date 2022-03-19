#include <stdio.h>
#define MAXN (1000*2+10)
char N[MAXN];
char M[MAXN];
int strcompare(const char *a, const char *b){
    int i;
    for (i=0; a[i] && b[i]; i++){
        if (a[i] == b[i]) continue;
        return a[i] - b[i];
    }
    return a[i] - b[i];
}
int strlength(const char * s){
   int i;
   for (i = 0; s[i]; i++);
   return i;
}
int InputData(){
    scanf("%s", N);
    if (strcompare(N, "0") == 0) return 0;
    scanf("%s", M);
    return 1;
}
int compare(const char *a, const char *b){
    int alen = strlength(a);
    int blen = strlength(b);
    if (alen == blen) return strcompare(a, b);
    return alen - blen;
}
void conv(int *dst, char *src, int slen, int dlen){
    for (int i=dlen-1, j=slen-1; j>=0; i--, j--){
        dst[i] = src[j] - '0';
    }
}
int conv2(int *dst, char *src){
    int i;
    for (i=0; src[i]; i++){
        dst[i] = src[i] - '0';
    }
    return i;
}
void add(char *a, char *b){
    int alen = strlength(a);
    int blen = strlength(b);
    int A[MAXN] = {0}, B[MAXN] = {0}, C[MAXN] = {0};
    int clen = ((alen > blen) ? alen : blen) + 1;
    conv(A, a, alen, clen);
    conv(B, b, blen, clen);
    for (int i=clen-1; i>0; i--){
        C[i] += A[i] + B[i];
        if (C[i] < 10) continue;
        C[i] -= 10; C[i-1] += 1;
    }
    for (int i=C[0]==0; i<clen; i++){
        printf("%d", C[i]);
    }
    printf("\n");
}
void sub(char *a, char *b){
    int alen = strlength(a);
    int blen = strlength(b);
    int A[MAXN] = {0}, B[MAXN] = {0}, C[MAXN] = {0};
    int clen = (alen > blen) ? alen : blen;
    conv(A, a, alen, clen);
    conv(B, b, blen, clen);
    for (int i=clen-1; i>=0; i--){
        C[i] += A[i] - B[i];
        if (C[i] >= 0) continue;
        C[i] += 10; C[i-1] -= 1;
    }
    int j;
    for (j=0; (j<clen-1) && (C[j] == 0); j++);
    for (; j<clen; j++){
        printf("%d", C[j]);
    }
    printf("\n");
}
void calculate(char *n, char *m, int nsign, int msign){
    if (nsign == msign){
        if (nsign == -1) printf("-");
        add(n, m);
    }
    else{
        int r = compare(n, m);
        if (r == 0) printf("0\n");
        else if (r > 0) {
            if (nsign == -1) printf("-");
            sub(n, m);
        }
        else{
            if (msign == -1) printf("-");
            sub(m, n);
        }
    }
}
void mul(char *a, char *b, int asign, int bsign){
    if (strcompare(b, "0") == 0){
        printf("0\n");
        return;
    }
    int A[MAXN], B[MAXN], C[MAXN] = {0};
    int alen = conv2(A, a), blen = conv2(B, b);
    int clen = alen + blen;
    for (int i=0; i<alen; i++){
        for (int j=0; j<blen; j++){
            C[i+j+1] += A[i] * B[j];
        }
    }
    for (int i=clen-1; i>0; i--){
        if (C[i] < 10) continue;
        C[i-1] += C[i]/10;
        C[i] %= 10;
    }
    if (asign != bsign) printf("-");
    for (int i=C[0]==0; i<clen; i++){
        printf("%d", C[i]);
    }
    printf("\n");
}
void Solve(){
    int nsign = 1, msign = 1;
    char *n=N, *m=M;
    if (N[0] == '-') {
        n++; nsign=-1;
    }
    if (M[0] == '-') {
        m++; msign=-1;
    }

    //n+m
    calculate(n, m, nsign, msign);
    //n-m
    calculate(n, m, nsign, msign*(-1));
    //n*m
    mul(n, m, nsign, msign);
}
int main(){
 /*   for(;;){
        if (InputData() == 0) break;
        Solve();
    }*/
    InputData();
    Solve();
    return 0;
}