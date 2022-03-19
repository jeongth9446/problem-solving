#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <cmath>


int main(void) {
	int n;
	
	scanf("%d", &n);

	for (int i = 1; i <= n; i++) {
		int s = i;
		int k = i;
		while (k != 0) {
			s += k % 10;
			k /= 10;
		}
		if (n == s) {
			printf("%d\n", i);
			return 0;
		}


	}
	printf("%d\n", 0);
	return 0;
}