
#include <stdio.h>
#include <string.h>
#include <string>
#include <stdlib.h>
#include <iostream>
#include <queue>

using namespace std;

int board[101][101];
int chk[101];
int cnt;
int n;
int dfs(int k) {
	chk[k] = 1;
	cnt++;
	for (int i = 1; i <= n; i++) {
		if (board[k][i] == 1 && chk[i] != 1) {
			dfs(i);
		}
	}
	return 0;
}
int main(void) {
	int m;
	scanf("%d %d", &n, &m);
	for (int i = 0; i < m; i++) {
		int t1, t2;
		scanf("%d %d", &t1, &t2);
		board[t1][t2] = 1;
		board[t2][t1] = 1;
	}
	dfs(1);

	printf("%d\n", cnt-1);
}