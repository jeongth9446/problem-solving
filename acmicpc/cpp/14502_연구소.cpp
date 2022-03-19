#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <cmath>
#include <string.h>



int map[10][10];
int virusmap[10][10];
int n, m;
int wall(int, int, int);
int viruscnt;
int virusmax;
void virus();
int main(void) {
	scanf("%d %d", &n, &m);

	virusmax = 1000;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			scanf("%d", &map[i][j]);
			virusmap[i][j] = 0;
			if (map[i][j] == 2 || map[i][j] == 1) viruscnt++;
		}
	}

	wall(1, 0, 0);

	printf("%d\n", n * m - virusmax - 3);

	return 0;


}

int wall(int k, int x, int y) {
	for (int i = x; i < n; i++) {
		for (int j = y; j < m; j++) {
			if (!map[i][j]) {
				map[i][j] = 1;
				if (k == 3) {
					virus();
					for (int k = 0; k < n; k++) {
						for (int l = 0; l < m; l++) {
							if (virusmap[k][l]) {
								map[k][l] = 0;
								virusmap[k][l] = 0;
								viruscnt--;
							}

						}
					}
				}
				else {
						wall(k + 1, i, 0);
		

				}
				map[i][j] = 0;
			}
		}
	}
	return 0;
}

void virus() {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (map[i][j] == 2) {
				if (i > 0 && !map[i - 1][j]) {
					map[i - 1][j] = 2;
					viruscnt++;
					virusmap[i - 1][j] = 1;
					virus();
				}
				if (i < n-1 && !map[i+1][j]) {
					map[i + 1][j] = 2;
					viruscnt++;
					virusmap[i + 1][j] = 1;
					virus();
				}
				if (j > 0 && !map[i][j-1]) {
					map[i][j-1] = 2;
					viruscnt++;
					virusmap[i][j-1] = 1;
					virus();
				}
				if (j < m-1 && !map[i][j+1]) {
					map[i][j+1] = 2;
					viruscnt++;
					virusmap[i][j+1] = 1;
					virus();
				}
			}
		}
	}
	if (virusmax > viruscnt)
		virusmax = viruscnt;

	return;
}