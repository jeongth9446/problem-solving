#include <stdio.h>

int main(void) {
	int n;
	int t = 1;
	int zeros = 0;
	scanf("%d", &n);

	for (int i = 1; i <= n; i++) {
		t *= i;
		while (t % 10 == 0) {
			t /= 10;
			zeros++;
		}
		t %= 10000;
	}

	printf("%d\n", zeros);
	return 0;

}