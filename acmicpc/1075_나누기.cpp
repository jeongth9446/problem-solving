//1075_나누기

#define _CRT_SECURE_NO_WARNINGS
#define _SILENCE_STDEXT_HASH_DEPRECATION_WARNINGS

#include <stdio.h>
#include <cmath>

int main(void) {
	int n, f;
	scanf("%d %d", &n, &f);

	n = (n / 100) * 100;
	
	for (int i = 0; i < 100; i++) {
		if ((n + i) % f == 0) {
			if (i < 10) printf("0");
			printf("%d\n", i);
			return 0;
		}
	}
	return 0;


}