//2160_그림 비교

#include <stdio.h>

int main(void) {
	char board[50][5][8];
	int n;
	int maxt = 40;
	int maxi = 0, maxj = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < 5; j++) {
			scanf("%s", board[i][j]);
		}
	}

	for (int i = 0; i < n; i++) {
		for (int j = i + 1; j < n; j++) {
			int t = 0;
			for (int x = 0; x < 5; x++) {
				for (int y = 0; y < 7; y++) {
					if (board[i][x][y] != board[j][x][y])t++;
				}
			}
			if (maxt > t) {
				maxt = t;
				maxi = i+1;
				maxj = j+1;
			}
		}
	}
	printf("%d %d\n", maxi, maxj);
	return 0;
}