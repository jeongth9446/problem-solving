#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main(void) {

	int arr[3] = { 0 };
	int c = 2000;
	int a, b;

	scanf("%d %d %d", &arr[0], &arr[1], &arr[2]);
	scanf("%d %d", &a, &b);
	for (int i = 0; i < 3; i++) {
		if (c > arr[i]) c = arr[i];
	}

	if (a < b)
		printf("%d\n", c + a - 50);
	else
		printf("%d\n", c + b - 50);

	return 0;
}
