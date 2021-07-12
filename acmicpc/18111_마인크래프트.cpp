
#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <map>
#include <stack>
#include <queue>
#include <string>
using namespace std;

int main(void) {
	int n, m, b;
	scanf("%d %d %d", &n, &m, &b);
	int arr[501][501] = { 0 };
	int min = 256;
	int acc = b;
	int max = 0;
	int min_time = 128000000;
	int min_block = 0;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			scanf("%d", &arr[i][j]);
			if (arr[i][j] < min) min = arr[i][j];
			acc += arr[i][j];
		}
	}
	max = acc / (m * n);

	for (int k = max; k >= min; k--) {
		int t = 0;
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= m; j++) {
				if (arr[i][j] > k) t += 2 * (arr[i][j] - k);
				else t += (k - arr[i][j]);
			}
		}
		if (t < min_time) {
			min_time = t;
			min_block = k;
		}

	}
	printf("%d %d\n",min_time, min_block);

	return 0;


}