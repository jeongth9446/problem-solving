#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <cmath>
#include <string.h>

int main(void) {
	
	int arr[10] = { 0 };
	int sum = 0;
	int flag = 0;
	for (int i = 0; i < 9; i++) {
		scanf("%d", &arr[i]);
		sum += arr[i];
	}

	for (int i = 0; i < 9 && !flag; i++) {
		for (int j = 0; j < 9 && !flag; j++) {
			if (i != j) {
				if (sum - arr[i] - arr[j] == 100) {
					arr[i] = 0;
					arr[j] = 0;
					flag = 1;
				}
			}
		}
	}

	for (int i = 0; i < 9; i++) {
		for (int j = i + 1; j < 9; j++) {
			if (arr[i] > arr[j]) {
				int tmp = arr[i];
				arr[i] = arr[j];
				arr[j] = tmp;
			}
		}
	}
	for (int i = 2; i < 9; i++) {
		printf("%d\n", arr[i]);
	}
	return 0;

}