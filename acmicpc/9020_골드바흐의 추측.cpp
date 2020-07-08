#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <cmath>

int main(void) {
	int n;

	int arr[10001] = { 0 };
	int arr_prime[10001] = { 0 };

	arr[1] = 1;
	for (int i = 2; i <= 10000; i++) {
		for (int j = i; j <= 10000; j += i) {
			if (arr[j] != 0 && i == j) break;
			if (j != i)
				arr[j] = 1;
		}
	}
	for (int i = 2; i <= 10000; i++) {
		if (arr[i] == 0) {
			arr_prime[++arr_prime[0]] = i;
		}
	}
	int t;
	scanf("%d", &t);
	while (t--) {
		scanf("%d", &n);
		int a, b, gap;
		gap = 10000;

		for (int i = 1; i <= arr_prime[0]; i++) {
			if (arr_prime[i] > n) break;
			for (int j = 1; j <= arr_prime[0]; j++) {
				if (arr_prime[i] + arr_prime[j] > n) break;
				else if (arr_prime[i] + arr_prime[j] == n && gap > abs(arr_prime[i] - arr_prime[j])) {
					a = arr_prime[i];
					b = arr_prime[j];
					gap = abs(arr_prime[i] - arr_prime[j]);
				}

			}
		}

		printf("%d %d\n", a, b);


	}

	return 0;
}