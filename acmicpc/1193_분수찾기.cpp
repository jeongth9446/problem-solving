#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>


int main(void) {

	int n;
	int i;
	int k = 0;
	int a, b;
	scanf("%d", &n);

	for (i = 1; i <= 1000000000; i++) {
		k += i;
		if (k >= n) break;
	}

	a = i - (k - n);
	b = i - a + 1;
	
	if (i % 2 == 1) {
		printf("%d/%d\n", b, a);
	}
	else
		printf("%d/%d\n", a, b);
	return 0;

}
