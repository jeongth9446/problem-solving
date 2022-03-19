//2747_ÇÇº¸³ªÄ¡ ¼ö

#define _CRT_SECURE_NO_WARNINGS
#define _SILENCE_STDEXT_HASH_DEPRECATION_WARNINGS

#include <stdio.h>
#include <cmath>

int main(void) {
	int n, a = 1, b = 0, c = 0;

	scanf("%d", &n);


	for (int i = 1; i <= n; i++) {
		c = a + b;
		a = b;
		b = c;

	}


	printf("%d\n", b);
	return 0;

}