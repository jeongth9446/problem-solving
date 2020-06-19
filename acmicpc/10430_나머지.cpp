#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#define MAX_INPUT_LENGTH 1000
#include <string.h>
#include <stdlib.h>



int main(void) {

	int A, B, C;

	scanf("%d %d %d", &A, &B, &C);
	printf("%d\n", (A + B) % C);
	printf("%d\n", ((A % C) + (B % C)) % C);
	printf("%d\n", (A * B) % C);
	printf("%d\n", ((A % C)*(B % C)) % C);


	return 0;
}
