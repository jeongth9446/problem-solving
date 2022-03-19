//14697_방 배정하기.cpp

#include <stdio.h>

int main(void) {
	int a, b, c, n;
	int flag = 0;
	scanf("%d %d %d %d", &a, &b, &c, &n);

	for (int i = 0; i <= 300; i++) {
		for (int k = 0; k <= 300; k++) {
			for (int l = 0; l <= 300; l++) {
				if (i * a + k * b + l * c == n) flag = 1;
			}
		}
	}
	printf("%d\n", flag);
	return 0;

}