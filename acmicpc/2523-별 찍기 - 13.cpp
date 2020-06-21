#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main(void) {

	int n;
	scanf("%d", &n);

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= i; j++) {
			printf("*");
		}
		printf("\n");
	}
	for (int i = n-1; i > 0; i--) {
		for (int j = 1; j <= i; j++) {
			printf("*");
		}
		printf("\n");
	}
}
