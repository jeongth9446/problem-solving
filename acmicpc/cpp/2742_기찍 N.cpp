#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main(void) {

	int n;
	scanf("%d", &n);
	for (int i = n; i > 0; printf("%d\n", i--));
	return 0;
}
