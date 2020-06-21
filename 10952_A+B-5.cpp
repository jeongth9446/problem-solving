#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main(void) {

	int a, b;
	while (scanf("%d %d", &a, &b) && !(a == 0 && b == 0)) printf("%d\n", a + b);
	return 0;

}
