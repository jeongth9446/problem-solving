#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main(void) {

	int n;
	int k;
	int c = 0;
	scanf("%d", &n);
	k = n;
	while (++c) {
		k = (k % 10) * 10 + (k / 10 + k % 10)%10;
		
		if (k == n) break;
	}
	printf("%d\n", c);
	return 0;

}
