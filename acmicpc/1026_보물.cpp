#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>


int main(void) {
	int n;
	scanf("%d", &n);

	int a[101], b[101];

	for (int i = 0; i < n; i++) {
		scanf("%d", &a[i]);
	}
	for (int i = 0; i < n; i++) {
		scanf("%d", &b[i]);
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (a[i] < a[j]) {
				int tmp = a[i];
				a[i] = a[j];
				a[j] = tmp;
			}
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (b[i] > b[j]) {
				int tmp = b[i];
				b[i] = b[j];
				b[j] = tmp;
			}
		}
	}
	int s = 0;

	for (int i = 0; i < n; i++) {
		s += a[i] * b[i];
	}
	printf("%d\n", s);

	return 0;
}
