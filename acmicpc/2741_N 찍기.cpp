#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main(void) {

	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; printf("%d\n", ++i));
	return 0;
}
