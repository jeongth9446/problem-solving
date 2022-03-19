#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>


int main(void) {
	int n, m;
	int s = 0;
	int min = 0;
	int arr[10001] = { 0 };
	arr[1] = 1;
	for (int i = 2; i <= 10000; i++) {
		for (int j = i; j <= 10000; j += i) {
			if (arr[j] != 0 && i == j) break;
			if (j != i)
				arr[j] = 1;
		}

	}
	scanf("%d %d", &n, &m);

	for (int i = n; i <= m; i++) {
		if (arr[i] == 0) {
			s += i;
			if (min == 0) min = i;

		}
	}
	if (s == 0) printf("-1\n");
	else
	printf("%d\n%d\n", s, min);



	return 0;
}
