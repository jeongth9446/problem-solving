#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>


int main(void) {

	char t[1000001];
	int k = 0;
	while (scanf("%s", t) != EOF) {
		k++;
	}
	printf("%d\n", k);

	return 0;
}
