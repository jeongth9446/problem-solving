#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <cmath>


int main(void) {
	int n;
	scanf("%d", &n);

	int arr[1000];
	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
	}
	for (int i = 0; i < n; i++) {

		for (int j = i; j < n; j++) {
			if (arr[i] > arr[j]) {
				int tmp = arr[i];
				arr[i] = arr[j];
				arr[j] = tmp;
			}
		}
	}
	int s = 0;
	for (int i = 0; i < n; i++) {
		s += arr[i] * (n - i);
	}

	printf("%d\n", s);

	return 0;
}
