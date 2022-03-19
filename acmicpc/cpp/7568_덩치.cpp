#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <cmath>


int main(void) {
	int n;
	int arr[50][3] = { 0 };
	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		scanf("%d %d", &arr[i][1], &arr[i][2]);
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (arr[i][1] < arr[j][1] && arr[i][2] < arr[j][2]) {
				arr[i][0] ++;
			}
		}
	}
	for (int i = 0; i < n; i++) {
		printf("%d ", arr[i][0] + 1);

	}

	return 0;

}