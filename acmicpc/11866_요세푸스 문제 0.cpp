
#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <map>


int main(void) {
	int n, k;
	int arr[1001];
	int cnt_print = 0;
	int idx = 0;
	scanf("%d %d", &n, &k);

	for (int i = 1; i <= n; i++) {
		arr[i] = i;
	}
	printf("<");
	while (cnt_print != n) {
		int cnt_k = 0;
		while (cnt_k != k) {
			idx++;
			if (idx == n + 1) idx = 1;
			if (arr[idx] != 0) cnt_k++;
		}
		printf("%d", idx);
		arr[idx] = 0;
		cnt_print++;
		if (cnt_print != n) {
			printf(", ");
		}
	}
	printf(">");
	return 0;


}