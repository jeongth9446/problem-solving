#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int main(void) {

	int n;
	scanf("%d", &n);

	for (int i = 1; i < n * 2; i++) {
		for (int j = 1; j < ((i < n) ? i : abs(n*2-i)); j++)
			printf(" ");
		for (int j = 1; j < ((i < n) ? 2*(n-i+1) : 2*(n - abs(n * 2 - i)+1)); j++)
			printf("*");
		printf("\n");
	}

	return 0;

}
