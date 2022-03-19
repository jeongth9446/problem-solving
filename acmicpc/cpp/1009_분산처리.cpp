#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>


int main(void) {

	int mapping_table[10][10] = { 0 };


	for (int i = 1; i < 10; i++) {
		int s = 1;
		for (int j = 1; j < 10; j++) {
			s *= i;
			int flag = 0;
			for (int k = 1; k <= mapping_table[i][0]; k++) {
				if (mapping_table[i][k] == s % 10) {
					flag = 1;
					break;
				}
			}
			if (!flag)
				mapping_table[i][++mapping_table[i][0]] = s % 10;
			else break;

		}
	}
	
	int t;
	scanf("%d", &t);

	while (t--) {

		int a, b;
		scanf("%d %d", &a, &b);
		if (a % 10 == 0)
			printf("10\n", 0);
		else
			printf("%d\n", mapping_table[a % 10][(b - 1) % mapping_table[a % 10][0] + 1]);

	}

	return 0;
}
