#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <cmath>
#include <string.h>

int main(void) {
	int n, m;
	int min = 64;
	scanf("%d %d", &n, &m);

	char board[51][51];

	for (int i = 0; i < n; i++) {
		scanf("%s", board[i]);
	}

	for (int i = 0; i <= n - 8; i++) {
		for (int j = 0; j <= m - 8; j++) {
			int chg = 0;
			for (int k = i; k < i + 8; k++) {
				for (int l = j; l < j + 8; l++) {
					if ((k + l) % 2 == 0 && board[k][l] != 'W')
						chg++;
					
					else if ((k + l) % 2 == 1 && board[k][l] != 'B')
						chg++;
				}
			}
			if (min > chg)
				min = chg;
			chg = 0;
			for (int k = i; k < i + 8; k++) {
				for (int l = j; l < j + 8; l++) {
					if ((k + l) % 2 == 0 && board[k][l] != 'B')
						chg++;

					else if ((k + l) % 2 == 1 && board[k][l] != 'W')
						chg++;
				}
			}
			if (min > chg)
				min = chg;
		}
	}

	printf("%d\n", min);

	return 0;

}