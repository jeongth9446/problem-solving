//4458_첫 글자를 대문자로

#define _CRT_SECURE_NO_WARNINGS
#define _SILENCE_STDEXT_HASH_DEPRECATION_WARNINGS

#include <stdio.h>
#include <cmath>
int main(void) {
	
	int n;
	int arr[8001] = { 0 };
	int sum = 0;
	int max = 8000, min = 0;
	int mode = 0;
	int mode_i = -1;
	int mode_i2 = -1;

	scanf("%d", &n);

	for (int i = 1; i <= n; i++) {
		int t;
		scanf("%d", &t);
		arr[t + 4000] ++;
	}

	for (int i = 0; i <= 8000; i++) {
		sum += arr[i] * (i - 4000);
	}
	printf("%d\n", (int)round((double)sum / n));

	int k = 0;
	for (int i = 0; i <= 8000; i++) {
		
		for (int j = 0; j < arr[i]; j++) {
			k++;
			if ((n + 1) / 2 == k) {
				printf("%d\n", i - 4000);
			}
		}
	}

	for (int i = 0; i <= 8000; i++) {
		if (mode < arr[i]) {
			mode = arr[i];
			mode_i = i;
			mode_i2 = -1;
		}
		else if (mode == arr[i] && mode_i2 == -1) {
			mode_i2 = i;
		}
	}
	if (mode_i2 == -1) printf("%d\n", mode_i-4000);
	else printf("%d\n", mode_i2-4000);

	while (arr[max] == 0) max--;
	while (arr[min] == 0) min++;

	printf("%d\n", max - min);
	return 0;


}