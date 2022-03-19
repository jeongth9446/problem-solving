
#include <stdio.h>
#include <string.h>
#include <string>
#include <stdlib.h>
#include <iostream>
#include <queue>

using namespace std;

struct node {
	int len;
	int x;
	int y;
};
int main(void) {
	int n, m;
	int board[100][100];
	int chk[100][100] = { 0 };
	char tmp[100];
	queue <struct node> que;

	scanf("%d %d", &n, &m);

	for (int i = 0; i < n; i++) {
		scanf("%s", &tmp);
		for (int j = 0; j < m; j++) {
			board[i][j] = tmp[j] - '0';
		}

	}
	n--;
	m--;
	que.push({ 1, 0, 0 });
	chk[0][0] = 1;
	while (que.size()) {
		struct node t;
		t = que.front();
		que.pop();
		if (t.x == n && t.y == m) {
			printf("%d\n", t.len);
			break;
		}
		else {
			if (t.x - 1 >= 0 && board[t.x - 1][t.y] == 1 && chk[t.x - 1][t.y] == 0) {
				que.push({ t.len + 1, t.x - 1, t.y });
				chk[t.x - 1][t.y] = 1;
			}
			if (t.x + 1 <= n && board[t.x + 1][t.y] == 1 && chk[t.x + 1][t.y] == 0) {
				que.push({ t.len + 1, t.x + 1, t.y });
				chk[t.x + 1][t.y] = 1;
			}
			if (t.y - 1 >= 0 && board[t.x][t.y-1] == 1 && chk[t.x][t.y-1] == 0) {
				que.push({ t.len + 1, t.x, t.y-1 });
				chk[t.x][t.y-1] = 1;
			}
			if (t.y + 1 <= m && board[t.x][t.y + 1] == 1 && chk[t.x][t.y + 1] == 0) {
				que.push({ t.len + 1, t.x, t.y + 1 });
				chk[t.x][t.y + 1] = 1;
			}
		}

	}
	return 0;

}