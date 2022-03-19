#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main(void) {

	int n, a, b;
	scanf("%d", &n);
	
	for (int i = 0; i < n; scanf("%d %d", &a, &b) && printf("Case #%d: %d\n", ++i, a+b));
	return 0;
}
