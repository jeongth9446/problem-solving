
#define _CRT_SECURE_NO_WARNINGS
#define _SILENCE_STDEXT_HASH_DEPRECATION_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <stack>
#include <math.h>


int cam[10][2] = { 0 };
int cam_cnt = 0;
int mapp[10][10] = { 0 };
int n, m;
int min = 9999;
void funcarea(int flag, int x, int y, int dir) {
	if (dir == 1) {
		for (int i = x-1; i > 0; i--) {
			if (mapp[i][y] == 6) break;
			if (mapp[i][y] < 0) mapp[i][y] += flag;
		}
	}
	else if (dir == 2) {
		for (int j = y+1; j < m+1 ; j ++) {
			if (mapp[x][j] == 6) break;
			if (mapp[x][j] < 0) mapp[x][j] += flag;
		}
	}
	else if (dir == 3) {
		for (int i = x + 1; i < n+1; i++) {
			if (mapp[i][y] == 6) break;
			if (mapp[i][y] < 0) mapp[i][y] += flag;
		}
	}
	else if (dir == 4) {
		for (int j = y -1; j > 0; j--) {
			if (mapp[x][j] == 6) break;
			if (mapp[x][j] < 0) mapp[x][j] += flag;
		}
	}
}

int func_cnt() {
	int t = 0;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			if (mapp[i][j] == -10) {
				t++;
			}
		}
	}
	return t;
}
int func(int k) {

	if (k == cam_cnt) {
		if (min > func_cnt()) {
			min = func_cnt();
		}
	}
	else {
		if (mapp[cam[k][0]][cam[k][1]] == 5) {
			funcarea(1, cam[k][0], cam[k][1], 1);
			funcarea(1, cam[k][0], cam[k][1], 2);
			funcarea(1, cam[k][0], cam[k][1], 3);
			funcarea(1, cam[k][0], cam[k][1], 4);
			func(k + 1);
			funcarea(-1, cam[k][0], cam[k][1], 1);
			funcarea(-1, cam[k][0], cam[k][1], 2);
			funcarea(-1, cam[k][0], cam[k][1], 3);
			funcarea(-1, cam[k][0], cam[k][1], 4);
		}
		else if (mapp[cam[k][0]][cam[k][1]] == 4) {
			funcarea(1, cam[k][0], cam[k][1], 1);
			funcarea(1, cam[k][0], cam[k][1], 2);
			funcarea(1, cam[k][0], cam[k][1], 3);
			func(k + 1);
			funcarea(-1, cam[k][0], cam[k][1], 1);
			funcarea(1, cam[k][0], cam[k][1], 4);
			func(k + 1);
			funcarea(-1, cam[k][0], cam[k][1], 2);
			funcarea(1, cam[k][0], cam[k][1], 1);
			func(k + 1);
			funcarea(-1, cam[k][0], cam[k][1], 3);
			funcarea(1, cam[k][0], cam[k][1], 2);
			func(k + 1);
			funcarea(-1, cam[k][0], cam[k][1], 4);
			funcarea(-1, cam[k][0], cam[k][1], 1);
			funcarea(-1, cam[k][0], cam[k][1], 2);
		}
		else if (mapp[cam[k][0]][cam[k][1]] == 3) {
			funcarea(1, cam[k][0], cam[k][1], 1);
			funcarea(1, cam[k][0], cam[k][1], 2);
			func(k + 1);
			funcarea(-1, cam[k][0], cam[k][1], 1);
			funcarea(1, cam[k][0], cam[k][1], 3);
			func(k + 1);
			funcarea(-1, cam[k][0], cam[k][1], 2);
			funcarea(1, cam[k][0], cam[k][1], 4);
			func(k + 1);
			funcarea(-1, cam[k][0], cam[k][1], 3);
			funcarea(1, cam[k][0], cam[k][1], 1);
			func(k + 1);
			funcarea(-1, cam[k][0], cam[k][1], 4);
			funcarea(-1, cam[k][0], cam[k][1], 1);
		}
		else if (mapp[cam[k][0]][cam[k][1]] == 2) {
			funcarea(1, cam[k][0], cam[k][1], 1);
			funcarea(1, cam[k][0], cam[k][1], 3);
			func(k + 1);
			funcarea(-1, cam[k][0], cam[k][1], 1);
			funcarea(-1, cam[k][0], cam[k][1], 3);
			funcarea(1, cam[k][0], cam[k][1], 2);
			funcarea(1, cam[k][0], cam[k][1], 4);
			func(k + 1);
			funcarea(-1, cam[k][0], cam[k][1], 2);
			funcarea(-1, cam[k][0], cam[k][1], 4);
		}
		else if (mapp[cam[k][0]][cam[k][1]] == 1) {
			funcarea(1, cam[k][0], cam[k][1], 1);
			func(k + 1);
			funcarea(-1, cam[k][0], cam[k][1], 1);
			funcarea(1, cam[k][0], cam[k][1], 2);
			func(k + 1);
			funcarea(-1, cam[k][0], cam[k][1], 2);
			funcarea(1, cam[k][0], cam[k][1], 3);
			func(k + 1);
			funcarea(-1, cam[k][0], cam[k][1], 3);
			funcarea(1, cam[k][0], cam[k][1], 4);
			func(k + 1);
			funcarea(-1, cam[k][0], cam[k][1], 4);
		}
	}
	return 0;
}
int main(void) {
	


	scanf("%d %d", &n, &m);

	for (int j = 0; j <= m + 1; j++) {
		mapp[0][j] = 6;
	}
	for (int i = 1; i <= n; i++) {
		mapp[i][0] = 6;
		for (int j = 1; j <= m; j++) {
			scanf("%d", &mapp[i][j]);
			if (mapp[i][j] == 0) mapp[i][j] = -10;
			else if (mapp[i][j] != 6) {
				cam[cam_cnt][0] = i;
				cam[cam_cnt][1] = j;
				cam_cnt++;
			}
		}
		mapp[i][m + 1] = 6;
	}
	for (int j = 0; j <= m + 1; j++) {
		mapp[n+1][j] = 6;
	}

	func(0);

	printf("%d\n", min);
	return 0;

}