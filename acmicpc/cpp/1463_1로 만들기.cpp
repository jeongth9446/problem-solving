
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
	int num;
};
int main(void) {
	queue<struct node> que;
	int n;

	scanf("%d", & n);
	que.push({ 0, n });

	while (1) {
		struct node t;
		t = que.front();
		que.pop();
		if (t.num == 1) {
			printf("%d", t.idx);
			break;
		}
		else {
			if (t.num % 3 == 0) que.push({ t.idx + 1 , t.num / 3 });
			if (t.num % 2 == 0) que.push({ t.idx + 1 , t.num / 2 });
			que.push({ t.idx + 1 , t.num - 1 });
		}
	}


	return 0;

}