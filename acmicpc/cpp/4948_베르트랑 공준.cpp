#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>


int main(void) {
	int n, m;

	int arr[1000001] = { 0 };
	arr[1] = 1;
	for (int i = 2; i <= 1000000; i++) {
		for (int j = i; j <= 1000000; j += i) {
			if (arr[j] != 0 && i == j) break;
			if (j != i)
				arr[j] = 1;
		}

	}
	while (1)
	{
		scanf("%d", &n);
		if (n == 0) break;
		int cnt = 0;
		for (int i = n+1; i <= n*2; i++) {
			if (arr[i] == 0) cnt++;
		}
		printf("%d\n", cnt);

	}
	
	

	return 0;

}
