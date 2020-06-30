#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>


int main(void) {

	int n, m;


	int t;
	scanf("%d", &t);
	while (t--) {
		scanf("%d %d", &n, &m);

		long long s = 1;
		int nn = 2;
		for (int i = m; i >= m - n + 1; i--) {
			s *= i;
			while (s % nn == 0 && nn <= n) {
				s /= nn++;
			}
		}
		printf("%lld\n", s);
	}
	return 0;
}
