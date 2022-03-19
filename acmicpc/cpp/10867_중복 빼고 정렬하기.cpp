#include <stdio.h>

int main(void) {
	int arr[2001] = { 0 };
	int n;
	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		int t;
		scanf("%d", &t);
		arr[t+1000] = 1;
	}
	for (int i = 0; i <= 2000; i++) {
		if (arr[i] == 1) printf("%d ", i-1000);
	}
	return 0;

}