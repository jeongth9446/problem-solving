#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int fibonacci(int n);

int a, b;
int main(void) {

	int chk[50] = { 0 };
	chk[0] = 1;
	chk[1] = 0;
	for (int i = 2; i < 50; i++) {
		chk[i] = chk[i - 1] + chk[i - 2];
	}
	int n, k;
	scanf("%d", &n);
	while (n--) {
		scanf("%d", &k);
		printf("%d %d\n", chk[k], chk[k + 1]);
	}

	
	return 0;
}
