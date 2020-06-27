#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>


int main(void) {

	int table[15][15] = { 0 };

	for (int i = 0; i <= 14; i++) {
		table[0][i] = i;
	}
	for (int i = 1; i <= 14; i++) {
		for (int j = 1; j <= 14; j++) {
			for (int k = 1; k <= j; k++) {
				table[i][j] += table[i - 1][k];
			}
		}
	}

	int t;
	int k, n;
	scanf("%d", &t);
	while (t--) {
		scanf("%d %d", &k, &n);
		printf("%d\n", table[k][n]);

	}
	return 0;


}
