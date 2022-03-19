#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <map>


int main(void) {
	int a[11][11] = { 0 };
	a[0][0] = 1;
	a[1][0] = 1;
	a[1][1] = 1;
	for (int i = 2; i <= 10; i++) {
		for (int j = 0; j <= 10; j++) {
			if (j == 0) a[i][j] = 1;
			else a[i][j] = a[i - 1][j] + a[i - 1][j - 1];
		}
	}
	int b, c;
	scanf("%d %d", &b, &c);

	printf("%d", a[b][c]);
	return 0;
}