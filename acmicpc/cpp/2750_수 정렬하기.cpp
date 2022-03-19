#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>


int main(void) {

	int n;

	int arr[1000];

	scanf("%d", &n);

	for (int i = 0; i < n; i++)
		scanf("%d", &arr[i]);

	for (int i = 0; i < n; i++) {
		for (int j = i + 1; j < n; j++) {
			if (arr[i] > arr[j]) {
				int t = arr[i];
				arr[i] = arr[j];
				arr[j] = t;

			}
		}
	}

	for (int i = 0; i < n; i++)
		printf("%d\n", arr[i]);

	return 0;

	
}