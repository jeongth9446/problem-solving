#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {

	int n;

	scanf("%d", &n);

	int arr[10001] = { 0 };

	while (n--) {
		int k;
		scanf("%d", &k);
		arr[k] ++;
	}

	for (int i = 1; i <= 10000; i++) {
		for (int j = 1; j <= arr[i]; j++) {
			printf("%d\n", i);
		}
	}

	return 0;

}