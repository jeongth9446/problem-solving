#include <stdio.h>

int factt(int);

int main(void) {
	int n;
	scanf("%d", &n);
	printf("%d\n", factt(n));
	return 0;
}


int factt(int n) {
	if (n == 0) return 1;
	else return factt(n - 1) * n;
}