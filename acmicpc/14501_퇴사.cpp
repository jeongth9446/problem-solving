#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <cmath>
#include <string.h>

int arr[2][20], chk[20];
int max, sum, n;
int func(int);

int main(void) {
	
	scanf("%d", &n);

	max = 0; sum = 0;

	for (int i = 1; i <= n; i++) {
		scanf("%d %d", &arr[0][i], &arr[1][i]);
		chk[i] = 0;
	}

	for (int i = 1; i <= n; i++)
		func(i);
	
	printf("%d\n", max);
	return 0;
}

int func(int m) {
	if (m > n) return 0;
	if (m + arr[0][m] <= n + 1) {
		chk[m] = 1;
		sum += arr[1][m];
		if (max < sum) max = sum;

		for (int i = m + arr[0][m]; i <= n; i++)
			func(i);

		chk[m] = 0;
		sum -= arr[1][m];
	}
	return 0;
}