#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int main(void) {


	int arr[10] = { 0 };

	int a, b, c;
	int res;
	scanf("%d %d %d", &a, &b, &c);
	res = a * b * c;
	while(res != 0) {
		arr[res % 10] ++;
		res /= 10;
	}
	for (int i = 0; i < 10; i++) {
		printf("%d\n", arr[i]);
	}
	return 0;

}
