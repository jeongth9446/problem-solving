#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>


int main(void) {

	int n;
	int i;
	int k = 0;
	scanf("%d", &n);

	for (i = 0; i <= 1000000000; i++) {
		(i == 0) ? k = 1 : k += i * 6;
		if (k >= n) break;
	}
	printf("%d\n", i+1);
	return 0;
}
