#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int funcd(int);


int main(void) {

	int check[10100] = { 0 };
	for (int i = 1; i <= 10000; i++) {
		check[funcd(i)] = 1;
	}
	for (int i = 1; i <= 10000; i++) {
		if (check[i] == 0) printf("%d\n", i);
	}

	return 0;
}

int funcd(int n) {
	int k = 0;
	k += n;
	while (n > 0) {
		k += n % 10;
		n /= 10;
	}
	return k;

}