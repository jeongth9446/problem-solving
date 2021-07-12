#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <map>

long long binary_search(long long* cable, int n, int k, long long start, long long end) {
	long long mid = (start + end) /2;
	if (start > end) return end;
	else {
		long long t = 0;
		for (int i = 0; i < k; i++) {
			t += cable[i] / mid;
		}
		if (t < n)
			return binary_search(cable, n, k, start, mid-1);
		return binary_search(cable, n, k, mid + 1, end);

	}

}

int main(void) {
	int k, n;
	long long t;
	long long cable[10000] = { 0 };
	int64_t tot_cable_length = 0;
	scanf("%d %d", &k, &n);
	for (int i = 0; i < k; i++) {
		scanf("%lld", &cable[i]);
		tot_cable_length += cable[i];
	}
	t = tot_cable_length / n;

	printf("%d ", binary_search(cable, n, k, 1, t));


	return 0;

}