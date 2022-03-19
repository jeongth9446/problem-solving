#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main(void) {


	int a, x, k;
	scanf("%d %d", &a, &x);

	for (int i = 0; i < a; i++) {
		scanf("%d", &k);
		if (k < x) printf("%d ", k);
	}
	return 0;
}
