#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {

	int n;
	int k;
	int arr[1000002] = { 0 };
	int arr_minus[10000002] = { 0 };

	scanf("%d", &n);

	while (n--) {
		scanf("%d", &k);
		if (k >= 0) {
			arr[k] = 1;
		}
		else {
			arr_minus[-k] = 1;
		}
	}

	for (int i = 1000000; i > 0; i--) {
		if (arr_minus[i]) printf("%d\n", -i);
	}
	for (int i = 0; i <= 1000000; i++) {
		if (arr[i]) printf("%d\n", i);

	}

	return 0;
}