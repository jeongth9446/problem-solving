#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int max(int, int, int);

int main(void) {
	int a, b, c;
	int powersum;
	int hypotenuse;
	while (scanf("%d %d %d", &a, &b, &c) && a != 0 && b != 0 && c != 0) {
		hypotenuse = max(a, b, c);
		powersum = a * a + b * b + c * c;
		if (powersum == 2 * hypotenuse * hypotenuse)
			printf("right\n");
		else printf("wrong\n");
	}
	return 0;
}

int max(int x, int y, int z) {
	int result = 0;

	if (result < x) result = x;
	if (result < y) result = y;
	if (result < z) result = z;
	return result;

}