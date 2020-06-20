#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#define MAX_INPUT_LENGTH 1000
#include <string.h>
#include <stdlib.h>



int main(void) {

	int a, b;
	scanf("%d %d", &a, &b);

	printf("%d\n", a * (b % 10));
	printf("%d\n", a * (b / 10 % 10));
	printf("%d\n", a * (b / 100 % 10));
	printf("%d\n", a * b);


	return 0;
}
