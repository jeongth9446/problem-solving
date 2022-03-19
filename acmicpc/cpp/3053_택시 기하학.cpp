#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int main(void) {
	int r;

	scanf("%d", &r);

	printf("%lf\n%lf\n", (double)r * (double)r * M_PI, (double)r * (double)r * 2);

	return 0;

}