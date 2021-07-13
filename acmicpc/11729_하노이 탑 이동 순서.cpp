#include <stdio.h>

int hanoi(int from, int tmp, int to, int n) {
	if (n == 0) return 0;
	hanoi(from, to, tmp, n - 1);
	printf("%d %d\n", from, to);
	hanoi(tmp, from, to, n - 1);
	return 0;
}
int main(void) {
	int n;
	int c = 1;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++) c *= 2;
	printf("%d\n", c - 1);
	hanoi(1, 2, 3, n);

	return 0;
}

