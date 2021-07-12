
#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <map>
#include <stack>
#include <queue>
#include <string>
using namespace std;

void clr_ddang(int* ddang, int m, int n, int x, int y);

int main(void) {


	int t;
	scanf("%d", &t);

	while (t--) {
		int ddang[2500] = { 0 };
		int n, m, k;
		int cnt = 0;
		scanf("%d %d %d", &m, &n, &k);
		for (int i = 0; i < k; i++) {
			int x, y;
			scanf("%d %d", &x, &y);
			ddang[x*n + y] = 1;
		}
		for (int i = 0; i < m; i++) {
			for (int j = 0; j < n; j++) {
				if (ddang[i*n+j] == 1) {
					clr_ddang(ddang, m, n, i, j);
					cnt++;
				}
			}
		}
		printf("%d\n", cnt);
	}
	return 0;
}

void clr_ddang(int* ddang, int m, int n, int x, int y) {
	if (x < 0 || x >= m || y < 0 || y >= n) return;
	if (ddang[x * n + y] == 1) {
		ddang[x * n + y] = 0;
		clr_ddang(ddang, m, n, x+1, y);
		clr_ddang(ddang, m, n, x -1, y);
		clr_ddang(ddang, m, n, x, y+1);
		clr_ddang(ddang, m, n, x, y-1);
	}
}
