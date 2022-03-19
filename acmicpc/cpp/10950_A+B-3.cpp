#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main(void) {

	int n;
	scanf("%d", &n);

	while (n--) {
		int n, m;
		scanf("%d %d", &n, &m);
		printf("%d\n", n + m);
	}
	return 0;
}
