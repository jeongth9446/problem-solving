#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <cmath>


int main(void) {
	
	int n;
	int p = 0;

	scanf("%d", &n);

	for(int i = 666; i <= 1000000000; i++) {
		int k = i;
		int flag = 0;
		int k1 = 0, k2 = 0, k3 = 0;
		while (k != 0) {
			k1 = k2;
			k2 = k3;
			k3 = k % 10;
			k /= 10;
			if (k1 == 6 && k2 == 6 && k3 == 6) flag = 1;
		}
		if (flag) {
			p++;
			if (p == n) {
				printf("%d\n", i);
				return 0;

			}
		}
	}

	return 0;
}