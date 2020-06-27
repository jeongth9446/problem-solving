#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>


int main(void) {

	int t;
	int h, w, n;

	scanf("%d", &t);
	while (t--) {
		scanf("%d %d %d", &h, &w, &n);

		int k = (n-1) / h;
		int kk = (n-1) % h + 1;

		if(k +1 < 10)
		printf("%d0%d\n", kk, k+1);
		else
			printf("%d%d\n", kk, k + 1);

	}
	
	return 0;


}
