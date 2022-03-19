
#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <map>
#include <stack>
#include <queue>
#include <string>
using namespace std;

bool mapp[1001][1001];

void dfs(bool* chk, int v, int n);
void bfs(bool* chk, int v, int n);
int main(void) {

	
	int n, m, v;
	scanf("%d %d %d", &n, &m, &v);

	for (int i = 0; i < m; i++) {
		int x, y;
		scanf("%d %d", &x, &y);
		mapp[x][y] = true;
		mapp[y][x] = true;
	}

	bool chk[1001] = { false };
	bool chk2[1001] = { false };
	dfs(chk, v, n);
	printf("\n");
	bfs(chk2, v, n);
	printf("\n");
	return 0;

}

void dfs(bool* chk, int v, int n) {
	if (!chk[v]) {
		printf("%d ", v);
		chk[v] = 1;
		for (int i = 1; i <= n; i++) {
			if (mapp[v][i] ==true) dfs(chk, i, n);
		}
	}
	return;
}

void bfs(bool* chk, int v, int n) {
	queue<int> que;
	que.push(v);

	while (que.size()) {
		int t = que.front();
		que.pop();
		if(!chk[t]) printf("%d ", t);
		chk[t] = true;
		for (int i = 1; i <= n; i++) {
			if (mapp[t][i] && !chk[i]) {
				que.push(i);
			}
		}
	}
	return;
}