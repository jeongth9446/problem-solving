#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <map>
#include <stack>
#include <queue>
using namespace std;

int main(void) {
	stack<int> stk;
	queue<char> que;
	int n;
	int p = 1;
	int arr[100001] = { 0 };
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
	}

	for (int i = 0; i < n; i++) {
		while (p <= arr[i]) {
			stk.push(p);
			p++;
			que.push('+');
		}
		if (arr[i] == stk.top()) {
			stk.pop();
			que.push('-');
		}
		else {
			printf("NO\n");
			return 0;
		}
	}

	while (que.size() != 0) {
		printf("%c\n", que.front());
		que.pop();
	}
	return 0;

}