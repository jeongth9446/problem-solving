#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main(void) {

	int n;
	int a, b;
	scanf("%d", &n);
	while(n--) {
		scanf("%d %d", &a, &b);
		printf("%d\n", a + b);
	}
}
