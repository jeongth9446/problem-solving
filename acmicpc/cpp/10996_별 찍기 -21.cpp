#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int main(void) {

	int n;
	scanf("%d", &n);

	for (int i = 1; i <= n * 2; i++) {
		for (int j = 1; j <= n; j++) {
			if (i % 2 == 1 && j % 2 == 1) printf("*");
			else if (i % 2 == 1 && j % 2 == 0) printf(" ");
			else if (i % 2 == 0 && j % 2 == 1) printf(" ");
			else printf("*");
		}
		printf("\n");
	}
	return 0;

}
