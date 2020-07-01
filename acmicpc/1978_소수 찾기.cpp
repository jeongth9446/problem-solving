#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>


int main(void) {
	int n;

	int arr[1001] = { 0 };
	arr[1] = 1;
	for (int i = 2; i <= 1000; i++) {
		for (int j = i; j <= 1000; j += i) {
			if (arr[j] != 0 && i == j) break;
			if(j != i)
				arr[j] = 1;
		}

	}
	scanf("%d", &n);
	int s = 0;
	while (n--) {
		int k;
		scanf("%d", &k);

		if (arr[k] == 0) s++;
	}
	printf("%d\n", s);
	return 0;

}
