#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int main(void) {


	int arr[42] = { 0 };
	int k;
	int cnt = 0;

	for (int i = 0; i < 10; i++) {
		scanf("%d", &k);
		arr[k % 42] = -1;
	}
	
	for (int i = 0; i < 42; i++) {
		if (arr[i] ==-1)cnt++;
	}
	printf("%d\n", cnt);
}
