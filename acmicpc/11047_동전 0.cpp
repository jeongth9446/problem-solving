#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <cmath>

int main(void) {
	int n, k;
	int coins = 0;

	int A[10];
	scanf("%d %d", &n, &k);

	for (int i = n - 1; i >= 0; i--)
		scanf("%d", &A[i]);

	for (int i = 0; i < n; i++) {
		coins += k / A[i];
		k %= A[i];
	}
	printf("%d\n", coins);
	return 0;
}