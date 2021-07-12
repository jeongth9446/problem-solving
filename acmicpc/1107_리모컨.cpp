
#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <map>
#include <stack>
#include <queue>
#include <string>
using namespace std;

struct node {
	int idx;
	int chl;
	bool pm;
};
int main(void) {
	int n, m;
	int malf[10] = { 0 };
	int chk[1000001] = { 0 };
	int chk2[1000001] = { 0 };
	queue<struct node> que;
	scanf("%d %d", &n, &m);
	for (int i = 0; i < m; i++) {
		int t;
		scanf("%d", &t);
		malf[t] = 1;
	}
	chk[100] = 1;
	que.push({ 0, 100, true});
	
	while (que.size()) {
		struct node t = que.front();
		que.pop();
		if (t.chl == n) {

			printf("%d\n", t.idx);
			break;
		}
		else {
			if (t.chl + 1 <= 1000000 && chk[t.chl + 1] != 1 ) {
				que.push({ t.idx + 1, t.chl + 1, true });
				chk[t.chl + 1] = 1;
			}
			if (t.chl - 1 >= 0 && chk[t.chl - 1] != 1) {
				que.push({ t.idx + 1, t.chl - 1, true });
				chk[t.chl - 1] = 1;
			}
			if (t.pm) {
				for (int i = 0; i < 10; i++) {
					if (malf[i] != 1) {
						if (chk[i] != 1) {
							chk[i] = 1;
							que.push({ 1, i, false });
						}
					}
				}
			}
			else {
				for (int i = 0; i < 10; i++) {
					if (malf[i] != 1) {
						if (t.chl * 10 + i <= 1000000 && chk2[t.chl * 10 + i] != 1) {
							chk2[t.chl * 10 + i] = 1;
							que.push({ t.idx + 1, t.chl * 10 + i, false });
						}
					}
				}
			}
		}
	}

	return 0;

}