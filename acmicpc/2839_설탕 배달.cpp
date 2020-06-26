#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>


int main(void) {

	int n;

	int chk[5001] = { 0 };
	for (int i = 0; i <= 5000; i++)
		chk[i] = 2000;
	
	for (int i = 0; i <= 1000; i++) {
		for (int j = 0; j <= 1666; j++) {
			if (i * 5 + j * 3 > 5000) continue;
			else {
				if (chk[i * 5 + j * 3] > i + j) {
					chk[i * 5 + j * 3] = i + j;
				}
			}
		}
	}
	int k = 0;
	scanf("%d", &n);

	if (chk[n] == 2000)printf("-1\n");
	else printf("%d\n", chk[n]);

	return 0;

}
