#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int func(int);


int main(void) {
	int n;
	int s = 0;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		if (i == 101)
			i = i;
		if (func(i)) {
			s++;
		}
	}
	printf("%d\n", s);
	return 0;
}


int func(int n) {
	int arr[4];
	int len = 0;
	int gap = -100;
	while (n != 0) {
		arr[len++] = n % 10;
		n /= 10;
	}
	for (int i = 0; i < len-1; i++) {
		if (gap == -100) gap = arr[i + 1] - arr[i];
		else {
			if (arr[i + 1] - arr[i] != gap) {
				return 0;
			}
		}
	}
	return 1;

}