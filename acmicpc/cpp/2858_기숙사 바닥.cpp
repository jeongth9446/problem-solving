//2858_기숙사 바닥
#include <stdio.h>

int main(void) {

	int r, b;
	scanf("%d %d", &r, &b);

	for (int i = 1; i <= 2000000; i++) {
		for (int j = 1; j <= i; j++) {
			if ((i - 2) * (j - 2) == b && 2 * i + 2 * j - 4 == r) {
				printf("%d %d\n", i, j);
				return 0;

			}
		}
	}
	return 0;

}