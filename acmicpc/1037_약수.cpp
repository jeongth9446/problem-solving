//1037_¾à¼ö

#define _CRT_SECURE_NO_WARNINGS
#define _SILENCE_STDEXT_HASH_DEPRECATION_WARNINGS

#include <stdio.h>

int main(void) {
	int n;
	int list[50] = { 0 };
	scanf("%d", &n);

	if (n % 2 == 1) {
		for (int i = 0; i < n; i++)
			scanf("%d", &list[i]);
		for (int i = 0; i < n; i++) {
			for (int j = i + 1; j < n; j++) {
				if (list[i] < list[j]) {
					int t = list[i];
					list[i] = list[j];
					list[j] = t;
				}
			}
		}
		printf("%d\n", list[n / 2]*list[n / 2]);
	}
	else {
		int max = 0;
		int min = 99999999;

		for (int i = 0; i < n; i++) {
			int t;
			scanf("%d", &t);
			if (max < t) max = t;
			if (min > t) min = t;
		}
		printf("%d\n", max * min);
	}
}