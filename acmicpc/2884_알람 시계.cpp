#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main(void) {

	int h, m;

	scanf("%d %d", &h, &m);

	if (m >= 45) m -= 45;
	else {
		m += 15;
		h = (h + 23) % 24;
	}
	printf("%d %d\n", h, m);
	return 0;
}
