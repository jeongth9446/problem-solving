#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>


int main(void) {

	int a, b;
	scanf("%d %d", &a, &b);

	if (a%10 < b%10) {
		a = b;
	}
	else if (a % 10 == b % 10) {
		if (a / 10 % 10 < b / 10 % 10) {
			a = b;
		}
		else if (a / 10 % 10 == b / 10 % 10) {
			if (a / 100 < b / 100) {
				a = b;

			}
		}
	}
	while (a > 0) {
		printf("%d", a % 10);
		a /= 10;
	}
	printf("\n");
	return 0;

}
