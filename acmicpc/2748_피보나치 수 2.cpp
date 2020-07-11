#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <cmath>
#include <string.h>


int main(void) {

	long long fib[100] = { 0 };
	fib[1] = 1;
	

	int n;
	scanf("%d", &n);

	for (int i = 2; i <= n; i++) {
		fib[i] = fib[i - 1] + fib[i - 2];
	}

	printf("%lld\n", fib[n]);

	return 0;
}