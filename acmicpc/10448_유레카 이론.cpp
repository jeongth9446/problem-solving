#include <stdio.h>
#include <stdlib.h>

int main(void) {
	int trinum[50];
	int t, n;
	for (int i = 1; i < 50; i++)
		trinum[i] = i * (i + 1) / 2;
	
	scanf("%d", &t);
	while (t--) {
		int flag = 0;
		scanf("%d", &n);
		for (int i = 1; i < 50 && !flag; i++) {
			for (int j = 1; j < 50 && !flag; j++) {
				for (int k = 1; k < 50 && !flag; k++) {
					if (trinum[i] + trinum[j] + trinum[k] == n) {
						printf("%d\n", 1);
						flag = 1;
					}
				}
			}
		}
		if (!flag) printf("%d\n", 0);
	}
	return 0;

}