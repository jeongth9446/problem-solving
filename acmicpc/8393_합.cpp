#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main(void) {

	int n;
	scanf("%d", &n);
	int s = 0;
		
		
	for (int i = 0; i < n; s += ++i);

	printf("%d\n", s);
	return 0;
}
