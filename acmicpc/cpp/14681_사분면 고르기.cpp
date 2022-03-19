#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main(void) {

	int n, m;

	scanf("%d %d", &n, &m);

	if (n > 0 && m > 0)
		printf("1\n");
	else if (n < 0 && m > 0)
		printf("2\n");
	else if (n < 0 && m < 0)
		printf("3\n");
	else printf("4\n");


	return 0;
}
