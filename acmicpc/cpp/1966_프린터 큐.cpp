
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
	int imp;
};
int main(void) {

	int t;
	scanf("%d", &t);

	while (t--) {
		int importancy[10] = { 0 };
		int n, m;
		queue<struct node> que;

		scanf("%d %d", &n, &m);
		for (int i = 0; i < n; i++) {
			int k;
			scanf("%d", &k);
			que.push({ i, k });
			importancy[k] ++;
		}
		int cnt = 0;
		
		while (++cnt) {
			int max = 0;
			for (int i = 9; i > 0; i--) {
				if (importancy[i] != 0) {
					max = i;
					break;
				}
			}
			while (que.front().imp < max) {
				que.push(que.front());
				que.pop();
			}
			if (que.front().idx == m) break;
			importancy[que.front().imp]--;
			que.pop();
		}
		printf("%d\n", cnt);

	}
	return 0;

}