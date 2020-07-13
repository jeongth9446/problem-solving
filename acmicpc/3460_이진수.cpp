#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>


int main(void) {
	int t, n;

	scanf("%d", &t);

	while (t--) {
		scanf("%d", &n);
		int c = 0;
		while (n != 0) {
			if (n % 2 == 1) printf("%d ", c);
			n /= 2;
			c++;
		}
		printf("\n");
	}

	return 0;
}

