#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main(void) {

	int k;
	int s = 0;
	for (int i = 0; i < 5; i++) {
		scanf("%d", &k);
		if (k < 40) k = 40;
		s += k;
	}
	printf("%d\n", s / 5);
	return 0;

}
