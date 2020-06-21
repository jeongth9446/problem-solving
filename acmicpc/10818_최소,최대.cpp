#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int main(void) {

	int max, min;
	min = 1000000;
	max = -1000000;
	int n;
	int k;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &k);
		if (k < min) min = k;
		if (k > max) max = k;
	}
	printf("%d %d\n", min, max);

	return 0;

}
