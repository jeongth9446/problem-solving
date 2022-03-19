
#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

int main(void) {

	queue<int> q;
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		q.push(i);
	}
	while (q.size() != 1) {
		q.pop();
		int t = q.front();
		q.pop();
		q.push(t);
	}

	printf("%d", q.front());
	return 0;

}