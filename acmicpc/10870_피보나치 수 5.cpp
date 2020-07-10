#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <cmath>

int fib(int);

int main(void) {
	int n;

	scanf("%d", &n);

	printf("%d\n", fib(n));

	return 0;
}

int fib(int k) {
	if (k == 0)return 0;
	else if (k == 1) return 1;
	else return fib(k - 1) + fib(k - 2);
	return 0;
}