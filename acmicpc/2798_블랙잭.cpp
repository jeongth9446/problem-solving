#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <cmath>


int main(void) {
	int n, m;

	scanf("%d %d", &n, &m);

	int arr[100];
	int s = 0;
	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
	}

	for (int i = 0; i < n; i++) {
		for (int j = i + 1; j < n; j++) {
			for (int k = j + 1; k < n; k++) {
				if (arr[i] + arr[j] + arr[k] <= m && s < arr[i] + arr[j] + arr[k]) {
					s = arr[i] + arr[j] + arr[k];
				}
			}
		}
	}
	printf("%d\n", s);
	return 0;

}